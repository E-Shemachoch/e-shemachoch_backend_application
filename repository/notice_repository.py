from rethinkdb import r
from entity.notice import Notice


class NoticeRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_notices(self):
        result = r.table("notices").order_by(r.desc("date")).run(self.conn)
        return [Notice(**document) for document in result]

    def add_notice(self, notice):
        result = r.table('notices').insert(
            [notice.dict(exclude_none=True)]).run(self.conn)
        document = r.table("notices").get(
            result['generated_keys'][0]).run(self.conn)

        return Notice(**document)

    def update_notice(self, notice):
        result = r.table('notices').get(notice.id).replace(
            notice.dict()).run(self.conn)
        document = r.table("notices").get(notice.id).run(self.conn)

        return Notice(**document)

    def delete_notice(self, id):
        result = r.table('notices').get(id).delete().run(self.conn)
        success = result['deleted'] != 0

        return success
