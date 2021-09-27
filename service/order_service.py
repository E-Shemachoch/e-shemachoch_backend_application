class OrderService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_orders(self):
        orders = self.repo.get_orders()
        return orders

    def add_order(self, order):
        order = self.repo.add_order(order)
        return order

    def update_order(self, order):
        order = self.repo.update_order(order)
        return order

    def delete_order(self, order):
        success = self.repo.delete_order(order)
        return success

    def get_consumer_orders(self, consumer_id):
        orders = self.repo.get_consumer_orders(consumer_id)
        return orders

    def claim_order(self, order_id):
        success = self.repo.claim_order(order_id)
        return success
