import gitlab


class GitlabApi:
    def __init__(self):
        super().__init__()
        # Initialize GitLab API Client
        self.server = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN, ssl_verify=False)
        self.server.auth()  # Authenticate

    def getUser(self):
        return self.server.user.id

    def getMemberProjects(self):
        return self.server.projects.list(order_by="last_activity_at", membership=True)
