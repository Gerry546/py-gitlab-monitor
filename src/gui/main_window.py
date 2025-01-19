from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QColor, QFont

class GitlabMonitor():
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.window = loader.load("src/gui/main_window.ui", None)
        self.initUI()
        self.window.show()

    def initUI(self):
        p = self.window.palette()
        p.setColor(self.window.backgroundRole(), QColor("#212121"))
        self.window.setPalette(p)
        self.window.setFont(QFont("Sans Serif", 12))
        self.window.setWindowTitle("Gitlab Monitor")
