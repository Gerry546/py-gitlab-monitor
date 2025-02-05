from nicegui import ui
from components.project_card import ProjectCard


class DashBoard:
    def __init__(self, gl):
        super().__init__()

        # UI Elements
        ui.label("🚀 GitLab Monitor").classes("text-2xl font-bold")
        ui.label("User ID: " + str(gl.getUser()))
        for project in gl.getMemberProjects():
            ProjectCard(project)
