from nicegui import ui
import datetime
from gitlab import GitlabGetError


class ProjectCard:
    def __init__(self, project):
        super().__init__()
        self.project = project
        self.branches = self.fetch_branches()
        # Generate a card for each project
        self.container = ui.card()
        with self.container:
            ui.label(project.namespace["full_path"])
            ui.label(project.name)
            ui.label(project.default_branch)
        self.update_pipelines()

    # Fetch pipelines based on selected branch
    def fetch_gitlab_pipelines(self, branch=None):
        """Fetch latest pipelines for the selected branch."""
        try:
            filters = {"order_by": "id", "sort": "desc", "per_page": 5}
            if branch:
                filters["ref"] = branch
            return self.project.pipelines.list(**filters)
        except GitlabGetError:
            ui.notify("Failed to fetch pipelines.", type="negative")
            return []

    def update_pipelines(self):
        """Update UI with the latest pipelines for the selected branch."""
        pipelines = self.fetch_gitlab_pipelines(self.branches[0])
        self.container.clear()
        if pipelines:
            for pipeline in pipelines:
                self.create_pipeline_card(pipeline)
        else:
            ui.label("No pipelines found.").classes("text-gray-500")

    # Fetch job details for a pipeline
    def fetch_pipeline_jobs(self, pipeline_id):
        """Retrieve jobs for a given pipeline."""
        try:
            pipeline = self.project.pipelines.get(pipeline_id)
            return pipeline.jobs.list()
        except GitlabGetError:
            ui.notify(f"Failed to fetch jobs for pipeline {pipeline_id}.", type="negative")
            return []

    # Calculate duration from start to finish
    def calculate_duration(self, pipeline):
        """Calculate and format pipeline duration."""
        # if pipeline.finished_at and pipeline.started_at:
        #     start = datetime.datetime.fromisoformat(pipeline.started_at.replace("Z", "+00:00"))
        #     finish = datetime.datetime.fromisoformat(pipeline.finished_at.replace("Z", "+00:00"))
        #     return str(finish - start)
        return "N/A"

    def create_pipeline_card(self, pipeline):
        """Create a UI card for each pipeline."""
        with ui.expansion(
            f"Pipeline #{pipeline.id} - {pipeline.status} ({self.calculate_duration(pipeline)})", icon="folder"
        ):
            ui.label(f"Ref: {pipeline.ref}")
            ui.label(f"Updated: {pipeline.updated_at}")
            # ui.button("View Pipeline", on_click=lambda: ui.open(pipeline.web_url), icon="launch")

            # Job details
            with ui.expansion("Jobs", icon="list"):
                jobs = self.fetch_pipeline_jobs(pipeline.id)
                for job in jobs:
                    with ui.card().classes("p-2 w-full"):
                        ui.label(f"Job: {job.name} - {job.status}").classes("font-bold")
                        # ui.button("View Job", on_click=lambda: ui.open(job.web_url), icon="launch")
                        # ui.button("Show Logs", on_click=lambda j=job.id: show_job_logs(j), icon="article")

    def fetch_branches(self):
        """Retrieve available branches from the GitLab project."""
        try:
            return [branch.name for branch in self.project.branches.list(all=True)]
        except GitlabGetError:
            ui.notify("Failed to fetch branches.", type="negative")
            return []
