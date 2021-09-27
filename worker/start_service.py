from service.adminstrator_service import AdminstratorService
from repository.adminstrator_repository import AdminstratorRepository
from repository.product_repository import ProductRepository
from service.product_service import ProductService
from service.notice_service import NoticeService
from repository.notice_repository import NoticeRepository
from service.consumer_service import ConsumerService
from repository.consumer_repository import ConsumerRepository
from repository.order_repository import OrderRepository
from service.order_service import OrderService
from repository.report_repository import ReportRepository
from service.report_service import ReportService


def start_service(app):
    conn = app.ctx.conn
    app.ctx.notice_service = NoticeService(NoticeRepository(conn))
    app.ctx.product_service = ProductService(ProductRepository(conn))
    app.ctx.consumer_service = ConsumerService(ConsumerRepository(conn))
    app.ctx.order_service = OrderService(OrderRepository(conn))
    app.ctx.report_service = ReportService(ReportRepository(conn))
    app.ctx.adminstrator_service = AdminstratorService(
        AdminstratorRepository(conn))
