import components.theme as theme
import views.all_pages as all_pages
import views.dashboard as dashboard
from nicegui import app, ui


@ui.page("/")
def index_page() -> None:
    with theme.frame("Homepage"):
        dashboard.content()


all_pages.create()

ui.run(title="Gitlab Monitor")
