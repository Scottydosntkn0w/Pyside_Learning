import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Import Circular progress
from circular_progress import CircularProgress


class MainWindow (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #RESIZE WINDOW
        self.resize(500, 500)
        
        # CREATE CONTAINER AND LAYOUT
        self.container = QFrame()
        self.container.setStyleSheet("background-color: green")
        self.layout = QVBoxLayout()

        # Create Circular Progress
        self.progress = CircularProgress()
        self.progress.value = 50
        self.setMinimumSize(self.progress.width, self.progress.height)
        self.progress.update()

        #Add slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.change_value)

        #add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter, Qt.AlignCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        #Show Window
        self.show()

    def change_value(self, value):
        self.progress.set_value(value)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())