from nicegui import ui
from services.gitlab_service import GitlabApi
from views.dashboard import DashBoard


# Initialize GitLab API Client
gl = GitlabApi()

# Generate a dashboard
DashBoard(gl)

# Run the app
ui.run()
