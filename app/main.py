from nicegui import ui
from services.gitlab_service import GitlabApi
from services.config import Config
from views.dashboard import DashBoard

# Initialize the configuration
config = Config()
# Initialize GitLab API Client
gl = GitlabApi(config)

# Generate a dashboard
DashBoard(gl)

# Run the app
ui.run()
