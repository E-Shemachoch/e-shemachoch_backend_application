class ProductService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_products(self):
        products = self.repo.get_products()
        return products

    def add_product(self, product):
        product = self.repo.add_product(product)
        return product

    def update_product(self, product):
        product = self.repo.update_product(product)
        return product

    def delete_product(self, product_id):
        success = self.repo.delete_product(product_id)
        return success

    def upload_image(self, image):
        image_id = self.repo.upload_image(image)
        return image_id

    def update_image(self, image):
        self.repo.update_image(image)

    def get_image(self, image_id):
        image = self.repo.get_image(image_id)
        return image
