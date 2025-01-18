import gitlab


class GitlabApi:
    def __init__(self):
        super().__init__()

        self.server = gitlab.Gitlab()
        self.projects = self.server.projects.list(iterator=True)

        for project in self.projects:
            print(project)
