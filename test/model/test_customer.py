import unittest

from src.model.customer import Customer
from src.model.discount import Discount, FifteenDiscount, TenDiscount, NoDiscount
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

PRODUCT_15 = 'DIS_15s2'
PRICE = 100
PRODUCT_NAME = "T"
CUSTOMER_NAME = 'KEVIN'

class DiscountTest(unittest.TestCase):

    def test_should_customer_pay_the_order(self):
        product = Product(PRICE, PRODUCT_15, PRODUCT_NAME)
        customer = Customer(CUSTOMER_NAME, PRICE)
        shopping_cart = ShoppingCart(customer, [product])
        order = shopping_cart.checkout()
        self.assertTrue(customer.pay_order(order))
        self.assertEqual(customer.balance, 15)

    def test_should_customer_not_enought_money_to_pay_the_order(self):
        product = Product(PRICE, PRODUCT_15, PRODUCT_NAME)
        customer = Customer(CUSTOMER_NAME)
        shopping_cart = ShoppingCart(customer, [product])
        order = shopping_cart.checkout()
        self.assertFalse(customer.pay_order(order))
        self.assertEqual(customer.balance, 0)