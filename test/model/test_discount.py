import unittest
from src.model.discount import Discount, FifteenDiscount, TenDiscount, NoDiscount
from src.model.product import Product

PRODUCT_15 = 'DIS_15s2'
PRODUCT_10 = 'DIS_10s2'
PRODUCT_NO = 'DI2'
PRICE = 100
PRODUCT_NAME = "T"


class DiscountTest(unittest.TestCase):

    def test_should_discount_be_fiften(self):
        product = Product(PRICE, PRODUCT_15, PRODUCT_NAME)
        self.assertEqual(15, product.calculate_discount())

    def test_should_discount_be_ten(self):
        product = Product(PRICE, PRODUCT_10, PRODUCT_NAME)
        self.assertEqual(10, product.calculate_discount())

    def test_should_discount_be_no(self):
        product = Product(PRICE, PRODUCT_NO, PRODUCT_NAME)
        self.assertEqual(0, product.calculate_discount())
