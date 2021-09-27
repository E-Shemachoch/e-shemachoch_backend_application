from sanic.response import json, text
from sanic import Blueprint
payment_blueprint = Blueprint("payment_blueprint", url_prefix="/payments")


@payment_blueprint.post("/")
async def add_payment(request):
    print(request.json)  # accept the ipn info
    return text('ipn recieved')
