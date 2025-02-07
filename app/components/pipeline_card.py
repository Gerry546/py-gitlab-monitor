from nicegui import ui
from gitlab import GitlabGetError


class PipelineCard:
    def __init__(self, container, project):
        super().__init__()
        self.project = project
        self.container = container
        self.branches = self.fetch_branches()

    def update_pipelines(self):
        """Update UI with the latest pipelines for the selected branch."""
        print("Updating pipelines...")
        pipelines = self.fetch_gitlab_pipelines(self.branches[0])
        if pipelines:
            for pipeline in pipelines:
                self.create_pipeline_card(pipeline)
        else:
            with self.container:
                ui.label("No pipelines found.").classes("text-gray-500")

    def create_pipeline_card(self, pipeline):
        """Create a UI card for each pipeline."""
        with self.container:
            """Create a UI card for each pipeline, displaying jobs horizontally."""
            with ui.card().classes("w-full p-4 my-2 shadow-md"):
                ui.label(f"Pipeline #{pipeline.id} - {pipeline.status} ({self.calculate_duration(pipeline)})").classes(
                    "text-lg font-bold"
                )
                ui.label(f"Branch: {pipeline.ref}")
                ui.label(f"Updated: {pipeline.updated_at}")

                # Job details in a horizontal row
                with ui.row().classes("w-full overflow-auto py-2"):
                    jobs = self.fetch_pipeline_jobs(pipeline.id)
                    for job in jobs:
                        with ui.card().classes("p-2 text-center w-40 border rounded-lg shadow-sm"):
                            ui.label(job.name).classes("font-bold")
                            ui.label(job.status).classes(
                                f"text-sm {'text-green-500' if job.status == 'success' else 'text-red-500'}"
                            )
                            # ui.button(
                            #     "Logs", on_click=lambda j=job.id: self.show_job_logs(j), icon="article", color="blue"
                            # )

    # Fetch pipelines based on selected branch
    def fetch_gitlab_pipelines(self, branch=None):
        """Fetch latest pipelines for the selected branch."""
        try:
            filters = {"order_by": "updated_at", "sort": "desc", "per_page": 5}
            if branch:
                filters["ref"] = branch
            return self.project.pipelines.list(**filters)
        except GitlabGetError:
            ui.notify("Failed to fetch pipelines.", type="negative")
            return []

    def fetch_branches(self):
        """Retrieve available branches from the GitLab project."""
        try:
            return [branch.name for branch in self.project.branches.list(all=True)]
        except GitlabGetError:
            ui.notify("Failed to fetch branches.", type="negative")
            return []

    # Calculate duration from start to finish
    def calculate_duration(self, pipeline):
        """Calculate and format pipeline duration."""
        # if pipeline.finished_at and pipeline.started_at:
        #     start = datetime.datetime.fromisoformat(pipeline.started_at.replace("Z", "+00:00"))
        #     finish = datetime.datetime.fromisoformat(pipeline.finished_at.replace("Z", "+00:00"))
        #     return str(finish - start)
        return "N/A"

    # Fetch job details for a pipeline
    def fetch_pipeline_jobs(self, pipeline_id):
        """Retrieve jobs for a given pipeline."""
        try:
            pipeline = self.project.pipelines.get(pipeline_id)
            return pipeline.jobs.list()
        except GitlabGetError:
            ui.notify(f"Failed to fetch jobs for pipeline {pipeline_id}.", type="negative")
            return []
