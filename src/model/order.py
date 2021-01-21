class Order:
    def __init__(self, loyalty_points_earned=0, total_price=0, if_paid=False):
        self.loyalty_points = loyalty_points_earned
        self.total = total_price
        self.if_paid = False

    def set_paid_status_to_true(self):
        self.if_paid = True

    def __str__(self):
        return "Total price: %s \nWill receive %s" % (self.total, self.loyalty_points)
