class AdminstratorService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def login_adminstrator(self, adminstrator):
        adminstrator = self.repo.login_adminstrator(adminstrator)
        return adminstrator
