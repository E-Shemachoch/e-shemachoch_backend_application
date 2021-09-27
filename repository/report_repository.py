from rethinkdb import r
from entity.report import Report
import time

class ReportRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_reports(self):
        income = r.table('orders').sum('total_price').run(self.conn)
        sold = r.table('orders').sum('total_quantity').run(self.conn)
        available = r.table('products').sum('quantity').run(self.conn)
        date = round(time.time() * 1000)
        return Report(income= income,sold= sold,available= available,date=date)
