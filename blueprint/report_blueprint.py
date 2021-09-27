from sanic.response import json
from sanic import Blueprint
from entity.report import Report
from middleware.authenticated import authenticated
from middleware.authorized import authorized

report_blueprint = Blueprint("report_blueprint", url_prefix="/reports")


@report_blueprint.get("/")
@authenticated
@authorized
async def get_reports(request):

    report_service = request.app.ctx.report_service
    report = report_service.get_reports()

    return json(report.dict())

