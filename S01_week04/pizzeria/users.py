class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

        self.order_history = UserOrderHistory(username)


class UserOrderHistory:
    def __init__(self, username):
        self.orders = []
        self.username = username
