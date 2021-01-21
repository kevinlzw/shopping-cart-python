class LoyaltyPoint():

    RATIO = 100

    def __init__(self, loyalty_point):
        self.loyalty_point = loyalty_point

    def add_loyalty_point(self, point):
        if not isinstance(point, int):
            raise AttributeError('输入数据不为整型')
        self.loyalty_point += point

    def get_loyalty_point(self):
        return self.loyalty_point

    def current_loyalty_worth_of_money(self):
        return self.loyalty_point // self.RATIO

    def convert_to_money(self):
        money = self.loyalty_point // self.RATIO
        self.loyalty_point %= self.RATIO
        return money