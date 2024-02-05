from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Custom Properties
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = True

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)
        
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)



        
    # Paint Event (Design Your Circular Pgrogress Here)
    def paintEvent(self):
        
        #Set Progress Parameters
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width /2
        value = self.value * 360 / self.max_value
        
        #Painter
        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
         
        #Create Rectangle
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)
        
        # PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # Create ARC / Circular Progresss
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)
        paint.drawText(rect, Qt.AlignCenter)


        #END
        paint.end()
    
        #Set Value
    def set_value(self, value):
        self.value = value
        self.paintEvent() #Render progress bar after chagne value
        print("Here Set value")

