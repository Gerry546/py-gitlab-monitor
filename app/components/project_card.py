from nicegui import ui


class ProjectCard:
    def __init__(self, project):
        super().__init__()
        # Generate a card for each project
        with ui.card():
            ui.label(project.namespace["full_path"])
            ui.label(project.name)
            ui.label(project.default_branch)
