class ReportService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_reports(self):
        report = self.repo.get_reports()
        return report
