import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import ctypes

myappid = 'BensonHill.Combine_UI.V0_01'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
app = QApplication(sys.argv)


#___STYLE__CODE_________________________________________
app.setStyle("Fusion")
darkPalette = app.palette() # [Credit] Palette code source : 
                            # https://gist.github.com/QuantumCD/6245215#file-qt-5-dark-fusion-palette
darkPalette.setColor(QPalette.Window, QColor(53,53,53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(QPalette.Base, QColor(25,25,25))
darkPalette.setColor(QPalette.AlternateBase, QColor(53,53,53))
darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
darkPalette.setColor(QPalette.ToolTipText, Qt.white)
darkPalette.setColor(QPalette.Text, Qt.white)
darkPalette.setColor(QPalette.Button, QColor(53,53,53))
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(darkPalette)
#____________________________________________________________




w = MainWindow(app)
w.show()
app.exec()

sys.exit()