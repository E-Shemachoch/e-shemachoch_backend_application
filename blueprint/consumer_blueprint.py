from middleware.authenticated import authenticated
from middleware.authorized import authorized
from middleware.firebase_authenticated import firebase_authenticated
from entity.image import Image
from sanic.response import json
from sanic import Blueprint
from entity.consumer import Consumer
from firebase_admin import auth
import jwt

consumer_blueprint = Blueprint("consumer_blueprint", url_prefix="/consumers")


@consumer_blueprint.get("/")
@authenticated
@authorized
async def get_consumers(request):

    consumer_service = request.app.ctx.consumer_service
    consumers = consumer_service.get_consumers()

    return json([consumer.dict() for consumer in consumers])


@consumer_blueprint.post("/")
@authenticated
@authorized
async def add_consumer(request):
    consumer = Consumer.parse_raw(request.form.get('consumer'))
    image = Image(content=request.files.get('image').body)

    consumer_service = request.app.ctx.consumer_service
    image_id = consumer_service.upload_image(image)
    consumer.image = image_id
    created_consumer = consumer_service.add_consumer(consumer)

    return json(created_consumer.dict())


@consumer_blueprint.put("/")
@authenticated
@authorized
async def update_consumer(request):
    consumer = Consumer(**request.json)

    consumer_service = request.app.ctx.consumer_service
    updated_consumer = consumer_service.update_consumer(consumer)

    return json(updated_consumer.dict())


@consumer_blueprint.delete("/<consumer_id:str>")
@authenticated
@authorized
async def delete_consumer(request, consumer_id):

    consumer_service = request.app.ctx.consumer_service
    success = consumer_service.delete_consumer(consumer_id)

    return json({'success': success})


@consumer_blueprint.get("/images/<image_id:str>")
# @authenticated
# @authorized
async def get_image(request, image_id):
    consumer_service = request.app.ctx.consumer_service
    image = consumer_service.get_image(image_id)
    response = await request.respond(content_type='image/jpeg')
    await response.send(image.content)
    await response.eof()
    return response


@consumer_blueprint.get("/check/<phone_number:str>")
async def check_existence(request, phone_number):

    consumer_service = request.app.ctx.consumer_service
    success = consumer_service.check_existence(phone_number)

    return json({'success': success})


@consumer_blueprint.get("/login")
@firebase_authenticated
async def login_consumer(request):
    phone_number = auth.verify_id_token(request.token)['phone_number']

    consumer_service = request.app.ctx.consumer_service
    consumer = consumer_service.login_consumer(phone_number)

    new_token = jwt.encode({'id': consumer.id, 'role': 'CONSUMER'},
                           request.app.config.JWT_KEY, algorithm="HS256")
    consumer.token = new_token

    return json(consumer.dict())
@consumer_blueprint.put("/images/<image_id:str>")
async def update_image(request, image_id):
    image = Image(id=image_id,content=request.files.get('image').body)
    consumer_service = request.app.ctx.consumer_service
    image = consumer_service.update_image(image)

    return json({'success':True})