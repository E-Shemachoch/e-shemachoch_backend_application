from entity.adminstrator import Adminstrator
from rethinkdb import r


class AdminstratorRepository:
    def __init__(self, conn):
        self.conn = conn
         
    def login_adminstrator(self, adminstrator):
        result = r.table('adminstrators').filter(
            {'username': adminstrator.username})[0].run(self.conn)
        adminstrator_doc = Adminstrator(**result)
        if(adminstrator_doc.password != adminstrator.password):
                raise Exception()
        return adminstrator_doc
