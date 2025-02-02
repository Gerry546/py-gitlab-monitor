from nicegui import ui
import gitlab

# GitLab Configuration
GITLAB_URL = "https://gitlab.com"  # Change for self-hosted GitLab
PRIVATE_TOKEN = "your-gitlab-token"
PROJECT_ID = 123456  # Replace with your project ID

# Initialize GitLab API Client
gl = gitlab.Gitlab(GITLAB_URL)
projects = gl.projects.list(iterator=True)
for project in projects:
    PROJECT_ID = project.id
    break
# gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)
# gl.auth()  # Authenticate

# Fetch available branches for filtering
def fetch_branches():
    """Retrieve available branches from the GitLab project."""
    project = gl.projects.get(PROJECT_ID)
    return [branch.name for branch in project.branches.list(all=True)]

# Fetch pipelines based on selected branch
def fetch_gitlab_pipelines(branch=None):
    """Fetch latest pipelines for the selected branch."""
    project = gl.projects.get(PROJECT_ID)
    filters = {"order_by": "id", "sort": "desc", "per_page": 5}
    if branch:
        filters["ref"] = branch
    return project.pipelines.list(**filters)

# Fetch job details for a pipeline
def fetch_pipeline_jobs(pipeline_id):
    """Retrieve jobs for a given pipeline."""
    project = gl.projects.get(PROJECT_ID)
    pipeline = project.pipelines.get(pipeline_id)
    return pipeline.jobs.list()

# UI Elements
ui.label("🚀 GitLab Monitor").classes("text-2xl font-bold")
ui.label(PROJECT_ID)

# Branch selection dropdown
branch_options = fetch_branches()
selected_branch = ui.select(branch_options, value=branch_options[0] if branch_options else None).classes("w-1/3")

container = ui.column().classes("w-full")

def create_pipeline_card(pipeline):
    """Create a UI card for each pipeline."""
    with ui.expansion(f"Pipeline #{pipeline.id} - {pipeline.status}", icon="folder"):
        ui.label(f"Ref: {pipeline.ref}")
        ui.label(f"Updated: {pipeline.updated_at}")
        ui.button("View Pipeline", on_click=lambda: ui.open(pipeline.web_url), icon="launch")

        # Job details
        with ui.expansion("Jobs", icon="list"):
            jobs = fetch_pipeline_jobs(pipeline.id)
            for job in jobs:
                with ui.card().classes("p-2 w-full"):
                    ui.label(f"Job: {job.name} - {job.status}").classes("font-bold")
                    ui.button("View Job", on_click=lambda: ui.open(job.web_url), icon="launch")

def update_pipelines():
    """Update UI with the latest pipelines for the selected branch."""
    pipelines = fetch_gitlab_pipelines(selected_branch.value)
    container.clear()
    if pipelines:
        for pipeline in pipelines:
            create_pipeline_card(pipeline)
    else:
        ui.label("No pipelines found.").classes("text-gray-500")

# Auto-refresh every 60 seconds
ui.timer(60.0, update_pipelines)

# Update on branch selection change
selected_branch.on("change", update_pipelines)

# Initial load
update_pipelines()

# Run the app
ui.run()
