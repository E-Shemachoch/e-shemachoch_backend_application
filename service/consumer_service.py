class ConsumerService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_consumers(self):
        consumers = self.repo.get_consumers()
        return consumers

    def add_consumer(self, consumer):
        consumer = self.repo.add_consumer(consumer)
        return consumer

    def update_consumer(self, consumer):
        consumer = self.repo.update_consumer(consumer)
        return consumer

    def delete_consumer(self, consumer):
        success = self.repo.update_consumer(consumer)
        return success

    def upload_image(self, image):
        image_id = self.repo.upload_image(image)
        return image_id

    def update_image(self, image):
        self.repo.update_image(image)
 
    def get_image(self, image_id):
        image = self.repo.get_image(image_id)
        return image

    def check_existence(self, phone_number):
        success = self.repo.check_existence(phone_number)
        return success

    def login_consumer(self, phone_number):
        consumer = self.repo.login_consumer(phone_number)
        return consumer
