
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Editer:)")
        self.setMinimumSize(400,600)
        self.main = QWidget()
        self.setCentralWidget(self.main)
        self.setStyleSheet('background:2D3047')

        self.initate()
    
    def initate(self):
        self.layout = QVBoxLayout()
        self.main.setLayout(self.layout)

        # text frame
        self.textFrame = QTextEdit()
        self.layout.addWidget(self.textFrame)

        # button
        self.buttonLayout = QHBoxLayout()
        self.layout.addLayout(self.buttonLayout)

        self.getFileButton = QPushButton("Open File")
        self.getFileButton.clicked.connect(self.openFile)
        
        self.saveFileButton = QPushButton("Save File")
        self.saveFileButton.clicked.connect(self.saveFile)

        self.buttonLayout.addWidget(self.getFileButton)
        self.buttonLayout.addWidget(self.saveFileButton)

    def openFile(self):
        self.filePath = QFileDialog.getOpenFileName()
        with open(self.filePath[0], "r") as f:
            data = f.read()
        self.textFrame.setText(data)
        print(self.textFrame.toPlainText())
    
    def saveFile(self):
        with open(self.filePath[0], "w") as f:
            data = f.write(self.textFrame.toPlainText())

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screen = MainWindow()
    screen.show()

    sys.exit(app.exec_())

		