from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class GitlabMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitLab Monitor Dashboard")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Welcome to GitLab Monitor Dashboard", self)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
