import sys
from PySide6.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.services.gitlab_service import GitlabApi

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    gl = GitlabApi()
    mainWindow.addGitlabServer(gl)
    mainWindow.show()
    sys.exit(app.exec())
