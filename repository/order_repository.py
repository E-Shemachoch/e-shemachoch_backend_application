from rethinkdb import r
from entity.order import Order


class OrderRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_orders(self):
        result = r.table("orders").run(self.conn)
        return [Order(**document) for document in result]

    def add_order(self, order):
        result = r.table('orders').insert(
            [order.dict(exclude_none=True)]).run(self.conn)
        document = r.table("orders").get(
            result['generated_keys'][0]).run(self.conn)
        order = Order(**document)
        for product in order.products:
            r.table('products').get(product.id).update({'quantity': r.row['quantity']-product.quantity}).run(self.conn)
        return order

    def update_order(self, order):
        result = r.table('orders').get(order.id).replace(
            order.dict()).run(self.conn)
        document = r.table("orders").get(order.id).run(self.conn)

        return Order(**document)

    def delete_order(self, id):
        result = r.table('orders').get(id).delete().run(self.conn)
        success = result['deleted'] != 0

        return success

    def get_consumer_orders(self, consumer_id):
        result = r.table("orders").filter(
            r.row['consumer_id'].eq(consumer_id)).run(self.conn)
        return [Order(**document) for document in result]

    def claim_order(self, id):
        order = Order(**r.table('orders').get(id).run(self.conn))
        order.claimed = True
        result = r.table('orders').get(order.id).replace(
            order.dict()).run(self.conn)
        success = result['replaced'] != 0

        return success
