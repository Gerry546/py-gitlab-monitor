from PySide6.QtWidgets import QApplication
from src.gui.main_window import GitlabMonitor
from src.services.gitlab_service import GitlabApi


def run_app():
    app = QApplication([])
    gitlab = GitlabApi()
    window = GitlabMonitor()
    window.show()
    app.exec()


if __name__ == "__main__":
    run_app()
