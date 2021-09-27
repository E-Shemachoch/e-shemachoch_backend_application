from rethinkdb import r
from entity.product import Product
from entity.image import Image


class ProductRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_products(self):
        result = r.table("products").run(self.conn)
        return [Product(**document) for document in result]

    def add_product(self, product):
        result = r.table('products').insert(
            [product.dict(exclude_none=True)]).run(self.conn)
        document = r.table("products").get(
            result['generated_keys'][0]).run(self.conn)

        return Product(**document)

    def update_product(self, product):
        result = r.table('products').get(product.id).replace(
            product.dict()).run(self.conn)
        document = r.table("products").get(product.id).run(self.conn)

        return Product(**document)

    def delete_product(self, id):
        product = Product(**r.table('products').get(id).run(self.conn))
        result_product = r.table('products').get(id).delete().run(self.conn)
        result_image = r.table('product_images').get(
            product.image).delete().run(self.conn)
        success = result_product['deleted'] != 0 and result_image['deleted'] != 0

        return success

    def upload_image(self, image):
        result = r.table('product_images').insert(
            image.dict(exclude_none=True)).run(self.conn)
        image_id = result['generated_keys'][0]
        return image_id

    def update_image(self, image):
        r.table('product_images').get(image.id).replace(
            image.dict()).run(self.conn)


    def get_image(self, image_id):
        result = r.table("product_images").get(image_id).run(
            self.conn)
        return Image(**result)
