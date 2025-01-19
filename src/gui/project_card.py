from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QMargins

class ProjectCard(QWidget):
    def __init__(self, project=None, parent=None):
        super().__init__(parent)
        self.project = project

        if parent is not None:
            self.setContentsMargins(QMargins(0, 0, 0, 0))

        self.initUI()

    def initUI(self):
        self.project_path_label = QLabel("<<Project Path>>")

        self.project_name_label = QLabel("<<Project Name>>")
        self.project_name_label.setFont(QFont("Sans Serif", 16))
        self.project_last_update_label = QLabel("<<Last Update>>")
        
        self.pageLayout = QVBoxLayout()
        self.pageLayout.addWidget(self.project_path_label)
        self.pageLayout.addWidget(self.project_name_label)
        self.pageLayout.addWidget(self.project_last_update_label)
        self.setLayout(self.pageLayout)
