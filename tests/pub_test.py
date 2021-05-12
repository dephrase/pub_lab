import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.corona = Drink("Corona", 5, 2)
        self.peroni = Drink("Peroni", 6, 2)
        self.cobra = Drink("Cobra", 3, 5)
        drinksList = [self.corona, self.peroni, self.cobra]
        self.pub = Pub("The Prancing Pony", 100.00, drinksList)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual([self.corona, self.peroni, self.cobra], self.pub.drinks)

        