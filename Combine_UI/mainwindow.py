import pandas
import os
import numpy as np
from datetime import datetime
from PySide6 import QtGui
from PySide6.QtCore import Qt,QTimer
from PySide6.QtWidgets import  QMainWindow,QMessageBox,QFileDialog,QTableWidgetItem
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Wedge, Rectangle
from ui_mainwindow import Ui_MainWindow
import sys
import random
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure

timer = QTimer()

def rot_text(ang): 
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

def degree_range(n): 
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points

def gauge(labels=['LOW','MEDIUM','HIGH','VERY HIGH','EXTREME'], \
          colors='jet_r', arrow=1, title='', fname=False): 
    
    #"""some sanity checks first """
    
    N = len(labels)
    
    if arrow > N: 
        raise Exception("\n\nThe category ({}) is greated than \
        the length\nof the labels ({})".format(arrow, N))
 
    #""" if colors is a string, we assume it's a matplotlib colormap and we discretize in N discrete colors  """
    
    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arange(N))
        colors = cmap[::-1,:].tolist()
    if isinstance(colors, list): 
        if len(colors) == N:
            colors = colors[::-1]
        else: 
            raise Exception("\n\nnumber of colors {} not equal \
            to number of categories{}\n".format(len(colors), N))

    #"""begins the plotting"""
    
    fig, ax = plt.subplots()

    ang_range, mid_points = degree_range(N)

    labels = labels[::-1]
    
    #"""plots the sectors and the arcs """
    patches = []
    for ang, c in zip(ang_range, colors): 
        # sectors
        patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.5))
    
    [ax.add_patch(p) for p in patches]
    
    #""" set the labels (e.g. 'LOW','MEDIUM',...) """
    
    for mid, lab in zip(mid_points, labels): 

        ax.text(0.35 * np.cos(np.radians(mid)), 0.35 * np.sin(np.radians(mid)), lab, \
            horizontalalignment='center', verticalalignment='center', fontsize=14, \
            fontweight='bold', rotation = rot_text(mid))

    #"""set the bottom banner and the title"""
    r = Rectangle((-0.4,-0.1),0.8,0.1, facecolor='w', lw=2)
    ax.add_patch(r)
    
    ax.text(0, -0.05, title, horizontalalignment='center', \
         verticalalignment='center', fontsize=22, fontweight='bold')

    #""" plots the arrow now """
    
    pos = mid_points[abs(arrow - N)]
    
    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)), \
                 width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')
    
    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

    #"""removes frame and ticks, and makes axis equal and tight """
    
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    plt.tight_layout()
    if fname:
        fig.savefig(fname, dpi=200)
    return ax
    


def Update_Table(self, file_name):
            
        try:
            if self.radioButton_Almaco.isChecked():
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    #need "Timestamp","ID_REC","Property_2_Value" to "Protein","Property_2_H" to "H", "Pro" 
                    csvFile = csvFile[['Timestamp','ID_REC',"Property_2_Value","Property_2_H","Property_2_S"]]
                    csvFile.rename(columns={'Property_2_Value': 'Protein', 'Property_2_H': 'H', "Property_2_S":"S"}, inplace=True)
                    csvFile_rev = csvFile[::-1].reset_index(drop=True)
                    formatted_panda = csvFile_rev
            if self.radioButton_Other.isChecked():         
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    formatted_panda = csvFile

            if self.radioButton_Winter.isChecked():
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    #need "Timestamp","ID_REC","Property_2_Value" to "Protein","Property_2_H" to "H", "Pro" 
                    csvFile = csvFile[['Timestamp','ID_REC',"Property_2_Value","Property_2_H","Property_2_S"]]
                    csvFile.rename(columns={'Property_2_Value': 'Protein', 'Property_2_H': 'H', "Property_2_S":"S"}, inplace=True)
                    csvFile_rev = csvFile[::-1].reset_index(drop=True)
                    formatted_panda = csvFile_rev
            no_row = len(formatted_panda)
            no_columns = len(formatted_panda.columns)
            self.entry_table.setColumnCount(no_columns)
            self.entry_table.setRowCount(no_row)
            for col in formatted_panda.columns:
                        text = col
                        index = formatted_panda.columns.to_list().index(col)
                        col = QTableWidgetItem(text)
                        self.entry_table.setHorizontalHeaderItem(index,col)
            for index, row in formatted_panda.iterrows():
                row_num = index
                for column in row:
                    data = column
                    col_num = row.to_list().index(column)
                    col_name = formatted_panda.columns[col_num]
                    cell_item = QTableWidgetItem(str(column))
                    color = ""
                    if col_name == "H":
                        if data > 60:
                            color = "red"
                        else:
                            color = "green"
                        
                    if col_name == "S":
                        if data > 10:
                            color = "red"
                        else:
                            color = "green"                           
                    
                    if col_name == "Protein":
                        if data < 20 or data > 70:
                            color = "red"
                        else:
                            color = "green"
                    
                    if color != "":
                        cell_item.setBackground(QtGui.QColor(color))

                    self.entry_table.setItem(row_num,col_num,cell_item)
            
            self.entry_table.resizeColumnsToContents()
            first_row = formatted_panda.iloc[0]
            self.last_protei_value_label.setText(str(first_row['Protein']))
            self.label_H_Value_Num.setText(str(first_row['H']))
            self.label_S_Value_Num.setText(str(first_row['S']))
        except Exception as e:
            print(e)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Combine UI")
        self.app = app

        canvas = PlotCanvas(self)


        
        #adding base MATLABPLOTS to QT UI
        static_canvas1 = FigureCanvas(Figure(figsize=(5, 3)))
        self.verticalLayout_3.addWidget(canvas)
        static_canvas2 = FigureCanvas(Figure(figsize=(5, 3)))
        self.verticalLayout_4.addWidget(static_canvas2)
        static_canvas3 = FigureCanvas(Figure(figsize=(5, 3)))
        self.verticalLayout_5.addWidget(static_canvas3)

        #Configre first MatLabplot Canvas
        #self._static_ax = static_canvas1.figure.subplots()
        #t = np.linspace(0, 10, 501)
        #self._static_ax.plot()
        # #Configre second MatLabplot Canvas
        # self._static_ax = static_canvas2.figure.subplots()
        # t = np.linspace(0, 10, 501)
        # self._static_ax.plot(t, np.tan(t), ".")        
        # #Configre third MatLabplot Canvas
        # self._static_ax = static_canvas3.figure.subplots()
        # t = np.linspace(0, 10, 501)
        # self._static_ax.plot(t, np.tan(t), ".")

        #Signal slot connections
        self.pushButton.clicked.connect(self.select_file)

    def checkForUpdate(self):
        print("checked")
        filepath = self.label.text()
        file_timestamp = os.stat(filepath).st_mtime
        saved_timestamp = self.File_timestamp_Label.text()
        file_name = filepath
        if str(file_timestamp) != str(saved_timestamp):
            Update_Table(self, file_name)
            print("updated")
            self.File_timestamp_Label.setText(str(file_timestamp))
        

    def select_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File", "","Text(*.csv);;All files(*.*)")
        if((file_name == "")):
            return
        self.label.setText(file_name)
        document_name = os.path.basename(file_name)
        self.file_name_label.setText(document_name)
        file_timestamp = os.stat(file_name).st_mtime
        self.File_timestamp_Label.setText(str(file_timestamp))
        Update_Table(self, file_name)
        if timer.isActive() is False:
            timer.timeout.connect(self.checkForUpdate)
            timer.start(1000)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, dpi=100):
        super(PlotCanvas, self).__init__(Figure())

        self.setParent(parent)

        # Create the figure and figure canvas
        fig = Figure(dpi=dpi)
        self.figure = fig
        self.canvas = FigureCanvas(self.figure)
        self.axes = fig.add_subplot()

        # Create data for the graph
        data = [random.random() for i in range(25)]

        # Line style
        self.axes.plot(data, linestyle='dashed')

        # Graph title text
        self.axes.set_title('The Graph Title')

        # Axes labels text
        self.axes.set_ylabel('Y Label')
        self.axes.set_xlabel('X Label')

        # X-axis color change
        self.axes.xaxis.label.set_color('blue')

        # Set the x-axis ticks and labels
        self.axes.xaxis.set_tick_params(colors='red')

        # Set y-axis label line color
        self.axes.spines['left'].set_color('orange')
        
        self.draw()




        
