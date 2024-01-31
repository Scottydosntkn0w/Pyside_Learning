
#Importing the componenets we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The sys module is responsible for processing command line arguments
import sys



app = QApplication(sys.argv)

window = QMainWindow()



window = QMainWindow()
window.show()

#Start the event Loop
app.exec()