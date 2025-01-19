import gitlab


class GitlabApi:
    def __init__(self):
        super().__init__()

        self.server = gitlab.Gitlab()
        self.projects = self.server.projects.list(iterator=True)
        i = 0
        for project in self.projects:
            if i < 1:
                self.project = self.server.projects.get(project.id)
                print(self.project.attributes)
                i += 1
            else:
                break
        print('done')