from sanic.response import json
from sanic import Blueprint
from entity.order import Order
from middleware.authenticated import authenticated
from middleware.authorized import authorized

order_blueprint = Blueprint("order_blueprint", url_prefix="/orders")


@order_blueprint.get("/")
@authenticated
@authorized
async def get_orders(request):

    order_service = request.app.ctx.order_service
    orders = order_service.get_orders()

    return json([order.dict() for order in orders])


@order_blueprint.post("/")
@authenticated
@authorized
async def add_order(request):
    order = Order(**request.json)

    order_service = request.app.ctx.order_service
    created_order = order_service.add_order(order)

    return json(created_order.dict())


@order_blueprint.put("/")
@authenticated
@authorized
async def update_order(request):
    order = Order(**request.json)

    order_service = request.app.ctx.order_service
    updated_order = order_service.update_order(order)

    return json(updated_order.dict())


@order_blueprint.delete("/<order_id:str>")
@authenticated
@authorized
async def delete_order(request, order_id):

    order_service = request.app.ctx.order_service
    success = order_service.delete_order(order_id)

    return json({'success': success})


@order_blueprint.get("/consumers/<consumer_id:str>")
@authenticated
@authorized
async def get_orders(request, consumer_id):

    order_service = request.app.ctx.order_service
    orders = order_service.get_consumer_orders(consumer_id)

    return json([order.dict() for order in orders])


@order_blueprint.put("/claim/<order_id:str>")
async def claim_order(request, order_id):

    order_service = request.app.ctx.order_service
    success = order_service.claim_order(order_id)

    return json({'success': success})
