
from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, QHBoxLayout, QApplication, QMenuBar, QMenu
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Edit:)")
        self.setMinimumSize(400,600)
        self.main = QWidget()
        self.setCentralWidget(self.main)
        self.setStyleSheet('background:2D3047')

        self.initate()
    
    def initate(self):
        self.textFrame = QTextEdit()
        self.layout = QHBoxLayout()
        self.main.setLayout(self.layout)

        self.layout.addWidget(self.textFrame)

        #menu bar 
        self.head = QMenuBar()
        self.setMenuBar(self.head)
        self.file = QMenu()
        self.head.addMenu("File")
        self.head.addMenu("Edit")
        self.head.addMenu("Help")

        # file menu
        self.file.addMenu("Open file")
        self.file.addMenu("New file")


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screen = MainWindow()
    screen.show()

    sys.exit(app.exec_())
		