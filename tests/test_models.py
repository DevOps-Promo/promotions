"""
Test cases for <your resource name> Model

"""
import logging
import unittest
import os
from service import app
from service.models import Promotion, DataValidationError, db
from datetime import datetime


DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  P R O M O T I O N   M O D E L   T E S T   C A S E S
######################################################################
class TestPromotion(unittest.TestCase):
    """ Test Cases for <your resource name> Model """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Promotion.init_db(app)
        pass

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        """ This runs before each test """
        db.drop_all()  # clean up the last tests
        db.create_all()  # make our sqlalchemy tables


    def tearDown(self):
        """ This runs after each test """
        db.session.remove()
        db.drop_all()


######################################################################
#  T E S T   C A S E S   S T A R T   H E R E
######################################################################

    def test_create_a_promotion(self):
        """ Create a promotion and assert that it exists """
        promotion = Promotion(
            name = "Default",
            description = "default description",
            start_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            end_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        )
        self.assertTrue(promotion != None)
        self.assertEqual(promotion.id, None)
        self.assertEqual(promotion.name, "Default")
        self.assertEqual(promotion.description , "default description")
        self.assertEqual(promotion.start_date, datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
        self.assertEqual(promotion.end_date, datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))


    def test_add_a_promotion(self):
        """ Create a promotion and add it to the database """
        promotions = Promotion.all()
        self.assertEqual(promotions, [])
        promotion = Promotion(
            name = "Default",
            description = "default description",
            start_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            end_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        )
        self.assertTrue(promotion != None)
        self.assertEqual(promotion.id, None)
        promotion.create()
        # Asert that it was assigned an id and shows up in the database
        self.assertEqual(promotion.id, 1)
        promotions = promotion.all()
        self.assertEqual(len(promotions), 1)

    def test_delete_a_promotion(self):
        """ Delete a Promotion """
        promotion = Promotion(
            name = "Default",
            description = "default description",
            start_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            end_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        )
        promotion.create()
        self.assertEqual(len(Promotion.all()), 1)
        # delete the promotion and make sure it isn't in the database
        promotion.delete()
        self.assertEqual(len(Promotion.all()), 0)