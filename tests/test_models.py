"""
Test cases for the Promotions Model

"""
from werkzeug.exceptions import NotFound
import logging
import unittest
import os
from werkzeug.exceptions import NotFound
from service import app
from service.models import Promotion, DataValidationError, db
from datetime import datetime
from werkzeug.exceptions import NotFound
from service.models import Promotion
from .factories import PromotionFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  P R O M O T I O N   M O D E L   T E S T   C A S E S
######################################################################
class TestPromotion(unittest.TestCase):
    """ Test Cases for the Promotions Model """

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


    def test_find_by_name(self):
        """ Find a Promotion by Name """
        Promotion(name="discount").create()
        Promotion(name="buy one get one").create()
        promotions = Promotion.find_by_name("buy one get one")
        self.assertEqual(promotions[0].name, "buy one get one")

    def test_find_or_404_found(self):
        """ Find or return 404 found """
        p1 = Promotion(
            name = "discount",
            description = "discount description",
            start_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            end_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        )
        p2 = Promotion(
            name = "buy one get one",
            description = "buy one get one description",
            start_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            end_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        )
        p3 = Promotion(
                name = "promo code",
            description = "promo code description",
            start_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'),
            end_date = datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')
        )
        promotions = [p1,p2,p3]
        p1.create()
        p2.create()
        p3.create()

#####################################################################
#READ PROMOTION TEST CASE
#####################################################################

    def test_find_promotion(self):
        """ Find a Promotion by ID """
        promotions = PromotionFactory.create_batch(3)
        for promotion in promotions:
            promotion.create()
        logging.debug(promotions)
        # make sure they got saved
        self.assertEqual(len(Promotion.all()), 3)
        # find the 2nd promotion in the list
        promotion = Promotion.find(promotions[1].id)
        self.assertIsNot(promotion, None)
        self.assertEqual(promotion.id, promotions[1].id)
        self.assertEqual(promotion.name, promotions[1].name)
        self.assertEqual(promotion.description, promotions[1].description)
        self.assertEqual(promotion.end_date, promotions[1].end_date)
        self.assertEqual(promotion.start_date, promotions[1].start_date)

    def test_find_or_404_found(self):
        """ Find or return 404 found """
        promotions = PromotionFactory.create_batch(3)
        for promotion in promotions:
            promotion.create()

        promotion = Promotion.find_or_404(promotions[1].id)
        self.assertIsNot(promotion, None)
        self.assertEqual(promotion.name, promotions[1].name)
        self.assertEqual(promotion.id, promotions[1].id)
        self.assertEqual(promotion.description, promotions[1].description)
        self.assertEqual(promotion.end_date, promotions[1].end_date)
        self.assertEqual(promotion.start_date, promotions[1].start_date)


    def test_find_or_404_not_found(self):
        """ Find or return 404 NOT found """
        self.assertRaises(NotFound, Promotion.find_or_404, 0)


    def test_serialize_a_promotion(self):
        """ Test serialization of a Promotion"""
        promotion = Promotion(name="New_Sale", 
                              description="Amazing", 
                              start_date=datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'), 
                              end_date=datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
        data = promotion.serialize()
        self.assertNotEqual(data, None)
        self.assertIn("id", data)
        self.assertEqual(data["id"], None)
        self.assertIn("name", data)
        self.assertEqual(data["name"], "New_Sale")
        self.assertIn("description", data)
        self.assertEqual(data["description"], "Amazing")
        self.assertIn("start date", data)
        self.assertEqual(data["start date"], datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
        self.assertIn("end date", data)
        self.assertEqual(data["end date"], datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))

    def test_deserialize_a_promotion(self):
        """ Test deserialization of a promotion """
        #data = {"id": 1, "name": "New_deal", "description": "Cool", "start date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'), "end date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')}
        promotion = Promotion(name="New_Sale", 
                              description="Amazing", 
                              start_date=datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'), 
                              end_date=datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
        data = promotion.serialize()
        promotion.deserialize(data)
        self.assertNotEqual(promotion, None)
        self.assertEqual(promotion.id, None)
        self.assertEqual(promotion.name, "New_Sale")
        self.assertEqual(promotion.description, "Amazing")
        self.assertEqual(promotion.start_date, datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
        self.assertEqual(promotion.end_date, datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
    
    
    # def test_serialize_a_cancel(self):
    #     """ Test serialization of a Cancelation"""
    #     promotion = Promotion(name="New_Sale", 
    #                           description="Amazing", 
    #                           start_date=datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'), 
    #                           end_date=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M'))
    #     data = promotion.serialize()
    #     self.assertNotEqual(data, None)
    #     self.assertIn("id", data)
    #     self.assertEqual(data["id"], None)
    #     self.assertIn("name", data)
    #     self.assertEqual(data["name"], "New_Sale")
    #     self.assertIn("description", data)
    #     self.assertEqual(data["description"], "Amazing")
    #     self.assertIn("start date", data)
    #     self.assertEqual(data["start date"], datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
    #     self.assertIn("end date", data)
    #     self.assertEqual(data["end date"], datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M'))


    # def test_deserialize_a_cancel(self):
    #     """ Test deserialization of a Cancelation """
    #     #data = {"id": 1, "name": "New_deal", "description": "Cool", "start date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'), "end date": datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S')}
    #     promotion = Promotion(name="New_Sale", 
    #                           description="Amazing", 
    #                           start_date=datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'), 
    #                           end_date= datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M'))
    #     data = promotion.serialize()
    #     promotion.deserialize(data)
    #     self.assertNotEqual(promotion, None)
    #     self.assertEqual(promotion.id, None)
    #     self.assertEqual(promotion.name, "New_Sale")
    #     self.assertEqual(promotion.description, "Amazing")
    #     self.assertEqual(promotion.start_date, datetime.strptime('2001-01-01 00:00:00', '%Y-%d-%m %H:%M:%S'))
    #     self.assertEqual(promotion.end_date,  datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')) 