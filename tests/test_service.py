"""
Promotion API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch
from flask_api import status  # HTTP Status Codes
from service.models import db
from service.service import app, init_db
from datetime import datetime


# DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///../db/test.db')
DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)


######################################################################
#  T E S T   C A S E S
######################################################################
class TestPromotionServer(TestCase):
    """ Promotion Server Tests """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        pass

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        """ This runs before each test """
        db.drop_all()  # clean up the last tests
        db.create_all()  # create new tables
        self.app = app.test_client()


    def tearDown(self):
        """ This runs after each test """
        db.session.remove()
        db.drop_all()
        pass

######################################################################
#  T E S T   C A S E S   S T A R T   H E R E 
######################################################################
    def test_index(self):
        """ Test index call """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        
        
    # def _create_promotions(self, count):
    #     """ Factory method to create promotions in bulk """
    #     promotions = []
    #     for _ in range(count):
    #         test_promotion = promotionFactory()
    #         resp = self.app.post(
    #             "/promotions", json=test_promotion.serialize(), content_type="application/json"
    #         )
    #         self.assertEqual(
    #             resp.status_code, status.HTTP_201_CREATED, "Could not create test promotion"
    #         )
    #         new_promotion = resp.get_json()
    #         test_promotion.id = new_promotion["id"]
    #         promotions.append(test_promotion)
    #     return promotions

    
    def test_create_promotion(self):
        """ Create a new promotion """
        test_promotion = {
            "name": "Default",
            "description": "default description",
            "start date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
        resp = self.app.post(
            "/promotions", 
            json=test_promotion, 
            content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # Make sure location header is set
        location = resp.headers.get("Location", None)
        self.assertTrue(location != None)
        # Check the data is correct
        new_promotion = resp.get_json()
        self.assertEqual(new_promotion["name"], test_promotion["name"], "Names do not match")
        self.assertEqual(new_promotion["description"], test_promotion["description"], "Descriptions do not match")
        self.assertEqual(datetime.strptime(new_promotion["start date"], '%a, %d %b %Y %H:%M:%S GMT'), test_promotion["start date"], "Start dates do not match")
        self.assertEqual(datetime.strptime(new_promotion["start date"], '%a, %d %b %Y %H:%M:%S GMT'), test_promotion["end date"], "End dates do not match")
        
        # TODO: When get_account is implemented, uncomment below
        # Check that the location header was correct
        # resp = self.app.get(location, content_type="application/json")
        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # new_promotion = resp.get_json()
        # self.assertEqual(new_promotion["name"], test_promotion["name"], "Names do not match")
        # self.assertEqual(new_promotion["description"], test_promotion["description"], "Descriptions do not match")
        # self.assertEqual(new_promotion["start_date"], test_promotion["start_date"], "Start dates do not match")
        # self.assertEqual(new_promotion["end_date"], test_promotion["end_date"], "End dates do not match")
 
    def test_delete_promotion(self):
        """ Delete a Promotion """
        
        test_promotion = {
            "name": "Default",
            "description": "default description",
            "start date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
        resp = self.app.post(
            "/promotions", 
            json=test_promotion, 
            content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        new_promotion = resp.get_json()
        promotion_id = new_promotion["id"]

        resp = self.app.delete(
            "/promotions/{}".format(promotion_id), content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(resp.data), 0)
        
        # TODO: When get_account is implemented, uncomment below
        
        # make sure they are deleted
        # resp = self.app.get(
        #     "/promotions/{}".format(promotion_id), content_type="application/json"
        # )
        # self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)        

    def test_query_promotion_list_by_category(self):
        """ Query Promotions by Category """
        p1 = {
            "name" : "discount",
            "description" : "discount description",
            "start date" : datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date" : datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
        resp = self.app.post("/promotions", json=p1, content_type="application/json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        p2 = {
            "name" : "buy one get one",
            "description" : "buy one get one description",
            "start date" : datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date" : datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
        resp = self.app.post("/promotions", json=p2, content_type="application/json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        p3 = {
            "name" : "promo code",
            "description" : "promo code description",
            "start date" : datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date" : datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
        resp = self.app.post("/promotions", json=p3, content_type="application/json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        
        promotions = [p1,p2,p3]
        test_name = promotions[0]["name"]
        name_promotions = [promotion for promotion in promotions if promotion["name"] == test_name]
        resp = self.app.get("/promotions", query_string="name={}".format(test_name))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(len(data), len(name_promotions))
        # check the data just to be sure
        for promotion in data:
            self.assertEqual(promotion["name"], test_name)

    def test_update_promotion(self):
        """ Update a Promotion """
        
        test_promotion = {
            "name": "Default",
            "description": "default description",
            "start date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
      # post it in the service
        resp = self.app.post(
            "/promotions", 
            json=test_promotion, 
            content_type="application/json"
        )
       #checking response: when you send a response to the browser, the backend tells the client and I have created a new entry in the database
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        updated_promotion = {
            "name": "New_deal",
            "description": "Good deal",
            "start date": datetime.strptime('2002-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date": datetime.strptime('2003-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }

    def test_update_promotion(self):
        """ Update an existing Promotion """
        # create a promotion to update
        test_promotion = {
            "name": "Default",
            "description": "default description",
            "start date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            "end date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        }
        resp = self.app.post(
            "/promotions", json=test_promotion, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # update the promotion
        new_promotion = resp.get_json()
        new_promotion["description"] = "whatever"
        #when it sends it back to the service, it says I have used this ID and used it on the put request
        resp = self.app.put(
            "/promotion/{}".format(new_promotion["id"]),
            json=new_promotion,
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        #reading the put response and placing it in the updated promotion variable 
        updated_promotion = resp.get_json()
        self.assertEqual(updated_promotion["description"], "whatever")