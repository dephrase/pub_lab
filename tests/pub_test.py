import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        corona = Drink("Corona", 5, 2)
        peroni = Drink("Peroni", 6, 2)
        cobra = Drink("Cobra", 3, 5)
        drinksList = [corona, peroni, cobra]
        self.pub = Pub("The Prancing Pony", 100.00, drinksList)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        corona = Drink("Corona", 5, 2)
        peroni = Drink("Peroni", 6, 4)
        cobra = Drink("Cobra", 3, 5)
        self.assertEqual(3, len(self.pub.drinksList))