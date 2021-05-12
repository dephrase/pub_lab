import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Peroni", 5, 2)
        drinkList = [self.drink]
        self.pub = Pub("Craigs Pub", 50, drinkList)
        self.customer = Customer("Barry", 20, 40)

    def test_customer_has_name(self):
        self.assertEqual("Barry", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(15, self.customer.wallet)
        self.assertEqual(55, self.pub.till)

    def test_customer_is_not_of_age(self):
        self.customer_not_of_age = Customer("Peter", 50, 16)
        self.customer_not_of_age.buy_drink(self.drink, self.pub)
        self.assertEqual("Do one!", self.customer_not_of_age.buy_drink(self.drink, self.pub))

    def test_customer_is_exact_age(self):
        self.customer_exact_age = Customer("Davross", 20, 18)
        self.customer_exact_age.buy_drink(self.drink, self.pub)
        self.assertEqual(15, self.customer_exact_age.wallet)
        self.assertEqual(55, self.pub.till)

    def test_customer_drunkenness_is_0(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_customer_drunkenness_increases(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(2, self.customer.drunkenness)

    def test_customer_drunkenness_increases_by9(self):
        self.vodka = Drink("Voddy", 8, 9)
        self.customer.buy_drink(self.vodka, self.pub)
        self.assertEqual(9, self.customer.drunkenness)

    def test_customer_cant_buy_third_drink(self):
        self.vodka = Drink("Voddy", 8, 9)
        self.rum = Drink("Kraken", 5, 15)
        self.customer.buy_drink(self.vodka, self.pub)
        self.customer.buy_drink(self.rum, self.pub)
        self.assertEqual("Do one!", self.customer.buy_drink(self.vodka, self.pub))
        self.assertEqual(24, self.customer.drunkenness)

    # def test_customer_is_too_drunk(self):
    #     self.vodka = Drink("Voddy", 8, 9)
    #     self.customer.buy_drink(self.vodka, self.pub)
    #     self.customer.buy_drink(self.vodka, self.pub)
    #     self.assertEqual("Do one!", self.customer.buy_drink(self.vodka, self.pub))