from src.model.discount import TenDiscount, FifteenDiscount, NoDiscount


class Product:
    TEN_DISCOUNT = "DIS_10"
    FIFTEEN_DISCOUNT = "DIS_15"

    def __init__(self, price, product_code, name):
        self.price = price
        self.product_code = product_code
        self.name = name
        self.set_discount_type(self.product_code)

    def set_discount_type(self, product_code):
        if product_code.startswith(self.TEN_DISCOUNT):
            self.discount = TenDiscount()
        elif product_code.startswith(self.FIFTEEN_DISCOUNT):
            self.discount = FifteenDiscount()
        else:
            self.discount = NoDiscount()

    def calculate_discount(self):
        return self.discount.calculate_discount(self.price)

    def calculate_loyalty_point(self):
        return self.discount.calculate_loyalty_point(self.price)

    def __str__(self):
        return " Name: %s \n Price: %s \n" % (self.name, self.price)
