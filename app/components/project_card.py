from nicegui import ui
from components.pipeline_card import PipelineCard


class ProjectCard:
    def __init__(self, project):
        super().__init__()
        self.project = project

        # Generate a card for each project
        self.container = ui.card()
        with self.container:
            ui.label("Project path: " + project.namespace["full_path"])
            ui.label("Project name: " + project.name)
            ui.label("Default branch: " + project.default_branch)

        self.pipeline_card = PipelineCard(self.container, self.project)
        self.pipeline_card.update_pipelines()
        ui.timer(60.0, self.pipeline_card.update_pipelines)
