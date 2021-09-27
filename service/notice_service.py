class NoticeService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_notices(self):
        notices = self.repo.get_notices()
        return notices

    def add_notice(self, notice):
        notice = self.repo.add_notice(notice)
        return notice

    def update_notice(self, notice):
        notice = self.repo.update_notice(notice)
        return notice

    def delete_notice(self, notice):
        success = self.repo.update_notice(notice)
        return success
