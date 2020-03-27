"""
Test Factory to make fake objects for testing
"""

import factory
from werkzeug.exceptions import NotFound
from factory.fuzzy import FuzzyChoice
from service.models import Promotion
from datetime import datetime


class PromotionFactory(factory.Factory):
    """ Creates fake promotions that you don't have to update """

    class Meta:
        model = Promotion

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("first_name")
    description= FuzzyChoice(choices=["name", "description", "start_date", "end_date"])
    start_date = factory.LazyFunction(datetime.utcnow)
    end_date = factory.LazyFunction(datetime.utcnow)

if __name__ == "__main__":
    for _ in range(10):
        promotion = PromotionFactory()
        print(promotion.serialize())
