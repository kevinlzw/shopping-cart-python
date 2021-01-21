from src.model.loyaltypoint import LoyaltyPoint


class Customer:
    def __init__(self, name, balance=0, loyalty_point=0):
        self.name = name
        self.balance = balance
        self.loyalty_point = LoyaltyPoint(loyalty_point)

    def add_balance(self, money):
        if not isinstance(money, float) or not isinstance(money, int):
            raise AttributeError('充值金额不为数字')
        self.balance += money

    def get_balance(self):
        return self.balance

    def pay_order(self, order, if_use_loyalty=False):
        money = self.balance
        if if_use_loyalty:
            money += self.loyalty_point.current_loyalty_worth_of_money()
        if money < order.total:
            return False
        else:
            if if_use_loyalty:
                self.loyalty_point.convert_to_money()
            self.balance = money - order.total
            self.loyalty_point.add_loyalty_point(order.loyalty_points)
            order.set_paid_status_to_true()
            return True

    def __str__(self):
        return self.name
