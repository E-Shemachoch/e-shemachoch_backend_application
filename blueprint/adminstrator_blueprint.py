import jwt
from sanic.response import json, text
from sanic import Blueprint
from entity.adminstrator import Adminstrator

adminstrator_blueprint = Blueprint(
    "adminstrator_blueprint", url_prefix="/adminstrators")


@adminstrator_blueprint.post("/login")
async def login_adminstrator(request):
    adminstrator = Adminstrator(**request.json)
    adminstrator_service = request.app.ctx.adminstrator_service
    success: bool
    try:
        checked_adminstrator = adminstrator_service.login_adminstrator(
            adminstrator)        
        new_token = jwt.encode({'role': 'ADMIN'}, request.app.config.JWT_KEY, algorithm="HS256")
        checked_adminstrator.token = new_token
        success = True
    except:
        success = False
        pass

    return json(checked_adminstrator.dict()) if success else text("You are unauthorized.", 401)
