from rethinkdb import r
from entity.consumer import Consumer
from entity.image import Image


class ConsumerRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_consumers(self):
        result = r.table("consumers").run(self.conn)
        return [Consumer(**document) for document in result]

    def add_consumer(self, consumer):
        result = r.table('consumers').insert(
            [consumer.dict(exclude_none=True)]).run(self.conn)
        document = r.table("consumers").get(
            result['generated_keys'][0]).run(self.conn)

        return Consumer(**document)

    def update_consumer(self, consumer):
        result = r.table('consumers').get(consumer.id).replace(
            consumer.dict()).run(self.conn)
        document = r.table("consumers").get(consumer.id).run(self.conn)

        return Consumer(**document)

    def delete_consumer(self, id):
        consumer = Consumer(**r.table('consumers').get(id).run(self.conn))
        result_consumer = r.table('consumers').get(id).delete().run(self.conn)
        result_image = r.table('consumer_images').get(
            consumer.image).delete().run(self.conn)
        success = result_consumer['deleted'] != 0 and result_image['deleted'] != 0

        return success

    def upload_image(self, image):
        result = r.table('consumer_images').insert(
            image.dict(exclude_none=True)).run(self.conn)
        image_id = result['generated_keys'][0]
        return image_id

    def update_image(self, image):
        r.table('consumer_images').get(image.id).replace(
            image.dict()).run(self.conn)

    def get_image(self, image_id):
        result = r.table("consumer_images").get(image_id).run(
            self.conn)
        return Image(**result)

    def check_existence(self, phone_number):
        success = r.table('consumers').filter(
            r.row['phone_number'].eq(phone_number)).count().eq(1).run(self.conn)
        return success

    def login_consumer(self, phone_number):
        result = r.table('consumers').filter(
            r.row['phone_number'].eq(phone_number)).nth(0).run(self.conn)
        return Consumer(**result)
