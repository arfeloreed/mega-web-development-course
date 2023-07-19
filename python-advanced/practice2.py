class OrderForm:
    """Creates a form order for the customer"""
    def __init__(self, username, price, is_premium):
        """Defines the initial attribute for the OrderForm"""
        self.username = username
        self.price = price
        self.is_premium = is_premium

    def order_status(self, status):
        print(f"\nYour order status is {status}.")


user1 = OrderForm("tommy01", 225, True)
print(user1.username)
print(user1.price)
print(user1.is_premium)
user1.order_status("shipped")