from sanic.response import json
from sanic import Blueprint
from entity.notice import Notice
from middleware.authenticated import authenticated
from middleware.authorized import authorized

notice_blueprint = Blueprint("notice_blueprint", url_prefix="/notices")


@notice_blueprint.get("/")
@authenticated
@authorized
async def get_notices(request):

    notice_service = request.app.ctx.notice_service
    notices = notice_service.get_notices()

    return json([notice.dict() for notice in notices])


@notice_blueprint.post("/")
@authenticated
@authorized
async def add_notice(request):
    notice = Notice(**request.json)

    notice_service = request.app.ctx.notice_service
    created_notice = notice_service.add_notice(notice)

    return json(created_notice.dict())


@notice_blueprint.put("/")
@authenticated
@authorized
async def update_notice(request):
    notice = Notice(**request.json)

    notice_service = request.app.ctx.notice_service
    updated_notice = notice_service.update_notice(notice)

    return json(updated_notice.dict())


@notice_blueprint.delete("/<notice_id:str>")
@authenticated
@authorized
async def delete_notice(request, notice_id):

    notice_service = request.app.ctx.notice_service
    success = notice_service.delete_notice(notice_id)

    return json({'success': success})
