"""
Models for Promotion

All of the models are stored in this module
"""
import logging, os
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger("flask.app")

# Create the SQLAlchemy object to be initialized later in init_db()
db = SQLAlchemy()

class DataValidationError(Exception):
    """ Used for an data validation errors when deserializing """
    pass


class Promotion(db.Model):
    """
    Class that represents a Promotion
    """

    app = None
    # logger = logging.getLogger(__name__)

    # Table Schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    description = db.Column(db.String(128))
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())

    def __repr__(self):
        return "<Promotion %r id=[%s]>" % (self.name, self.id)

    def create(self):
        """
        Creates a Promotion to the database
        """
        logger.info("Creating %s", self.name)
        self.id = None  # id must be none to generate next primary key
        db.session.add(self)
        db.session.commit()

    def save(self):
        """
        Updates a Promotion to the database
        """
        logger.info("Saving %s", self.name)
        db.session.commit()

    def delete(self):
        """ Removes a Promotion from the data store """
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """ Serializes a Promotion into a dictionary """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start date": self.start_date,
            "end date": self.end_date
        }

    def deserialize(self, data):
        """
        Deserializes a Promotion from a dictionary

        Args:
            data (dict): A dictionary containing the resource data
        """
        try:
            self.name = data["name"]
            self.description = data["description"]
            self.start_date = data["start date"]
            self.end_date = data["end date"]
        except KeyError as error:
            raise DataValidationError("Invalid Promotion: missing " + error.args[0])
        except TypeError as error:
            raise DataValidationError(
                "Invalid Promotion: body of request contained" "bad or no data"
            )
        return self

    @classmethod
    def init_db(cls, app):
        """ Initializes the database session """
        logger.info("Initializing database")
        cls.app = app
        # This is where we initialize SQLAlchemy from the Flask app
        db.init_app(app)
        app.app_context().push()
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def all(cls):
        """ Returns all of the Promotions in the database """
        logger.info("Processing all Promotions")
        return cls.query.all()

    @classmethod
    def find(cls, by_id):
        """ Finds a Promotion by it's ID """
        logger.info("Processing lookup for id %s ...", by_id)
        return cls.query.get(by_id)

    @classmethod
    def find_or_404(cls, by_id):
        """ Find a Promotion by it's id """
        logger.info("Processing lookup or 404 for id %s ...", by_id)
        return cls.query.get_or_404(by_id)

    @classmethod
    def find_by_name(cls, name):
        """ Returns all Promotions with the given name

        Args:
            name (string): the name of the Promotions you want to match
        """
        logger.info("Processing name query for %s ...", name)
        return cls.query.filter(cls.name == name)





############################################################
#  P O S T G R E S   D A T A B A S E   C O N N E C T I O N
############################################################

    # @staticmethod
    # def init_db(dbname='promotions'):
    #     """
    #     Initialized Postgres database connection
    # 
    #     """
    #     # This method will work in the following conditions:
    #     #  1) With DATABASE_URI as an environment variable
    #     #  2) In Bluemix with DB2 bound through VCAP_SERVICES
    #     #  3) With PostgreSQL running on the local server as with Travis CI
    # 
    #     database_uri = None
    # 
    #     if 'DATABASE_URI' in os.environ:
    #         # Get the credentials from DATABASE_URI
    #         Promotion.logger.info("Using DATABASE_URI...")
    #         # current_app.logger.info("Using DATABASE_URI...")
    #         database_uri = os.environ['DATABASE_URI']
    #     elif 'VCAP_SERVICES' in os.environ:
    #         # Get the credentials from the Bluemix environment
    #         Promotion.logger.info("Using VCAP_SERVICES...")
    #         # current_app.logger.info("Using VCAP_SERVICES...")
    #         vcap_services = os.environ['VCAP_SERVICES']
    #         services = json.loads(vcap_services)
    #         creds = services['dashDB For Transactions'][0]['credentials']
    #         database_uri = creds["uri"]
    #     else:
    #         Promotion.logger.info("Using localhost database...")
    #         # current_app.logger.info("Using localhost database...")
    #         database_uri = "postgres://postgres:postgres@localhost:5432/postgres"
    # 
    #     return database_uri