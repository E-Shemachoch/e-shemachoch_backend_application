from middleware.authorized import authorized
from entity.image import Image
from sanic.response import json
from sanic import Blueprint
from entity.product import Product
from middleware.authenticated import authenticated
product_blueprint = Blueprint("product_blueprint", url_prefix="/products")


@product_blueprint.get("/")
@authenticated
@authorized
async def get_products(request):

    product_service = request.app.ctx.product_service
    products = product_service.get_products()

    return json([product.dict() for product in products])


@product_blueprint.post("/")
@authenticated
@authorized
async def add_product(request):
    product = Product.parse_raw(request.form.get('product'))
    image = Image(content=request.files.get('image').body)

    product_service = request.app.ctx.product_service
    image_id = product_service.upload_image(image)
    product.image = image_id
    created_product = product_service.add_product(product)

    return json(created_product.dict())


@product_blueprint.put("/")
@authenticated
@authorized
async def update_product(request):
    product = Product(**request.json)

    product_service = request.app.ctx.product_service
    updated_product = product_service.update_product(product)

    return json(updated_product.dict())


@product_blueprint.delete("/<product_id:str>")
@authenticated
@authorized
async def delete_product(request, product_id):

    product_service = request.app.ctx.product_service
    success = product_service.delete_product(product_id)

    return json({'success': success})


@product_blueprint.get("/images/<image_id:str>")
async def get_image(request, image_id):
    product_service = request.app.ctx.product_service
    image = product_service.get_image(image_id)
    response = await request.respond(content_type='image/jpeg')
    await response.send(image.content)
    await response.eof()
    return response

@product_blueprint.put("/images/<image_id:str>")
async def update_image(request, image_id):
    image = Image(id=image_id,content=request.files.get('image').body)
    product_service = request.app.ctx.product_service
    image = product_service.update_image(image)

    return json({'success':True})