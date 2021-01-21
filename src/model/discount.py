from abc import ABCMeta, abstractmethod


class Discount(metaclass=ABCMeta):

    @abstractmethod
    def calculate_discount(self, price):
        pass

    @abstractmethod
    def calculate_loyalty_point(self, price):
        pass


class NoDiscount(Discount):

    def calculate_discount(self, price):
        return 0

    def calculate_loyalty_point(self, price):
        return price / 5


class FifteenDiscount(Discount):

    def calculate_discount(self, price):
        return price * 0.15

    def calculate_loyalty_point(self, price):
        return price / 15


class TenDiscount(Discount):

    def calculate_discount(self, price):
        return price * 0.1

    def calculate_loyalty_point(self, price):
        return price / 10
