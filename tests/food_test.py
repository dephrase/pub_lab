import unittest

from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.curry = Food("curry", 8,8)

    def test_food_has_name(self):
        self.assertEqual("curry", self.curry.name)

    def test_food_has_price(self):
        self.assertEqual(8, self.curry.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(8, self.curry.rejuvenation_level)