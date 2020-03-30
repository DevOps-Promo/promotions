"""
My Service

Describe what your service does here
"""
from werkzeug.exceptions import NotFound
import os
import sys
import logging
from flask import Flask, jsonify, request, url_for, make_response, abort
from flask_api import status  # HTTP Status Codes

# For this example we'll use SQLAlchemy, a popular ORM that supports a
# variety of backends including SQLite, MySQL, and PostgreSQL
from flask_sqlalchemy import SQLAlchemy
from service.models import Promotion, DataValidationError

# Import Flask application
from . import app

import datetime

######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """ Root URL response """
    return "Reminder: return some useful information in json format about the service here", status.HTTP_200_OK


######################################################################
# CREATE A NEW PROMOTION
######################################################################
@app.route("/promotions", methods=["POST"])
def create_promotions():
    """
    Creates a Promotion
    This endpoint will create a Promotion based the data in the body that is posted
    """
    app.logger.info("Request to create a promotion")
    check_content_type("application/json")
    promotion = Promotion()
    promotion.deserialize(request.get_json())
    promotion.create()
    message = promotion.serialize()
    #location_url = url_for("get_promotions", promotion_id=promotion.id, _external=True)
    location_url = "not implemented"
    return make_response(
        jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}
    )

######################################################################
# DELETE A PROMOTION
######################################################################
@app.route("/promotions/<int:promotion_id>", methods=["DELETE"])
def delete_promotion(promotion_id):
    """
    Delete a Promotion
    This endpoint will delete a Promotion based the id specified in the path
    """
    app.logger.info("Request to delete promotion with id: %s", promotion_id)
    promotion = Promotion.find(promotion_id)
    if promotion:
        promotion.delete()
    return make_response("", status.HTTP_204_NO_CONTENT)

######################################################################
# LIST ALL PROMOTIONS
######################################################################
@app.route("/promotions", methods=["GET"])
def list_promotions():
    """ Returns all of the Promotions """
    app.logger.info("Request for promotions list")
    promotions = []
    name = request.args.get("name")
    if name:
        promotions = Promotion.find_by_name(name)
    else:
        promotions = Promotion.all()

    results = [promotion.serialize() for promotion in promotions]
    return make_response(jsonify(results), status.HTTP_200_OK)

######################################################################
#READ PROMOTION
######################################################################
@app.route("/promotions/<int:promotion_id>", methods=["GET"])
def read_promotions(promotion_id):
    """
    Reads a single promotion
    This endpoint will read an promotion based on it's promotion id
    """
    app.logger.info("Request to read an promotion with id: %s")
    promotion = Promotion.find(promotion_id)
    if not promotion:
        raise NotFound("promotion with id '{}' was not found.".format(promotion_id))
    return make_response(jsonify(promotion.serialize()), status.HTTP_200_OK)

######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################

def init_db():
    """ Initialies the SQLAlchemy app """
    global app
    Promotion.init_db(app)


def check_content_type(content_type):
    """ Checks that the media type is correct """
    if request.headers["Content-Type"] == content_type:
        return
    app.logger.error("Invalid Content-Type: %s", request.headers["Content-Type"])
    abort(415, "Content-Type must be {}".format(content_type))

######################################################################
# UPDATE AN EXISTING Promotion
######################################################################
@app.route("/promotions/<int:promotion_id>", methods=["PUT"])  
def update_promotion(promotion_id): 
    """
    Update a promotion
    This endpoint will update a Promotion based the body that is posted
    """
    app.logger.info("Request to update promotion with id: %s", promotion_id)
    check_content_type("application/json")
    promotion = Promotion.find(promotion_id)
    if not promotion:
        raise NotFound("Promotion with id '{}' was not found.".format(promotion_id))
    promotion.deserialize(request.get_json())
    promotion.id = promotion_id
    promotion.save()
    return make_response(jsonify(promotion.serialize()), status.HTTP_200_OK)

######################################################################
# Cancel AN EXISTING Promotion
######################################################################
@app.route("/promotions/cancel/<int:promotion_id>", methods=["PUT"]) #the app_route requires the user (marketing manager) to specify a promotion_id in the url. 
# When the request is made, the users’ browser makes a 'PUT' request that sends data in json format to your function (this is not necessary for this function since all we need is the promotion_id)
def cancel_promotion(promotion_id): #defining what we're about to do
    """
    Cancel a promotion
    This endpoint will update a Promotion based the body that is posted
    """
    app.logger.info("Request to cancel promotion with id: %s", promotion_id) #creates a log for that promotion_id
    check_content_type("application/json") #checks to see of the content is in the right format
    promotion = Promotion.find(promotion_id) #find the specific promotion_id that we're looking to cancel
    if not promotion: #But if that promotion_id does not exist...
        raise NotFound("Promotion with id '{}' was not found.".format(promotion_id)) #log that it wasn't found
    # promotion.deserialize(request.get_json()) #If no error, it deserializes the PUT request and assigns the info from the PUT request to a promotion object
    # promotion.id = promotion_id #it gives the promotion object the same ID as the one the user specified 
    promotion.end_date = datetime.datetime.now() #it save it to the database
    promotion.save()
    return make_response(jsonify(promotion.serialize()), status.HTTP_200_OK) #returns a response to the user with the ‘updated’ promotion (the serialized promotion object)

######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################
# Need this to run 'Update an Existing Account'
def check_content_type(content_type):
    """ Checks that the media type is correct """
    if request.headers["Content-Type"] == content_type:
        return
    app.logger.error("Invalid Content-Type: %s", request.headers["Content-Type"])
    abort(415, "Content-Type must be {}".format(content_type))