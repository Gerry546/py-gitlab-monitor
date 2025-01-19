from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QWidget
from src.gui.project_card import ProjectCard
from src.gui.flowlayout import FlowLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget = QWidget()

        self.pageLayout = FlowLayout(widget)
        
        widget.setLayout(self.pageLayout)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#212121"))
        self.setPalette(palette)
        self.setWindowTitle("Gitlab Monitor")
        self.setCentralWidget(widget)
    
    def addGitlabServer(self, gl):
        self.gl = gl
        self.addProject()
   
    def addProject(self):
        projectCard = ProjectCard(project=self.gl.getProject())
        self.pageLayout.addWidget(projectCard)