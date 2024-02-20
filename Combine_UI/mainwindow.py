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


def Set_Guage_2_H(self):
        # Setup Guage
        self.widget_2.units = "H"
        self.widget_2.minValue = 0
        self.widget_2.maxValue = 20
        #Divisions
        self.widget_2.scalaCount = 4

        self.widget_2.updateValue(self.widget_2.minValue)
        self.widget_2.updateAngleOffset(0)
        self.widget_2.setScaleStartAngle(135)
        self.widget_2.setTotalScaleAngleSize(270)
        self.widget_2.setEnableBarGraph(True)
        self.widget_2.setEnableValueText(True)
        self.widget_2.setEnableCenterPoint(False)
        self.widget_2.setEnableNeedlePolygon(True)

        self.widget_2.setEnableScaleText(True)
        self.widget_2.setEnableScalePolygon(True)
        self.widget_2.setEnableBigScaleGrid(True)
        self.widget_2.setEnableFineScaleGrid(True)
        self.widget_2.setGaugeColorOuterRadiusFactor(1000)
        self.widget_2.setGaugeColorInnerRadiusFactor(600)
        self.widget_2.setNeedleColor(R=0, G=0, B=0, Transparency=255)
        #self.widget_2.setNeedleColorOnDrag(R=R, G=G, B=B, Transparency=Transparency)
        #self.widget_2.setScaleValueColor(R=R, G=G, B=B, Transparency=Transparency)
        #self.widget_2.setDisplayValueColor(R=R, G=G, B=B, Transparency=Transparency)
        self.widget_2.setGaugeTheme(0)
        #self.widget_2.setOuterCircleColor()
        red_scale_start = .369
        red_scale_end = 1
        yellow_spread = .01
        self.widget_2.set_scale_polygon_colors([[red_scale_start, Qt.red],
                                    [red_scale_start+yellow_spread, Qt.yellow],
                                    [red_scale_start+(yellow_spread*2), Qt.green],
                                    [red_scale_end-(yellow_spread*2), Qt.green],
                                    [red_scale_end-yellow_spread, Qt.yellow],
                                    [red_scale_end, Qt.red]])


        # self.widget_2.setCustomGaugeTheme(
        #     color1 = "red",
        #     color2= "purple",
        #     color3 = "blue"
        # )

        # self.widget_2.setScalePolygonColor(
        #     color1 = "green"
        # )

        # self.widget_2.setNeedleCenterColor(
        #     color1 = "white"
        # )

        # self.widget_2.setOuterCircleColor(
        #     color1 = "black"
        # )

        self.widget_2.setBigScaleColor("#005275")
        self.widget_2.setFineScaleColor("#005275")
        self.widget_2.setMouseTracking(False)

def Set_Guage_3_S(self):
        # Setup Guage
        self.widget_3.units = "S"
        self.widget_3.minValue = 0
        self.widget_3.maxValue = 100
        #Divisions
        self.widget_3.scalaCount = 10

        self.widget_3.updateValue(self.widget_3.minValue)
        self.widget_3.updateAngleOffset(0)
        self.widget_3.setScaleStartAngle(135)
        self.widget_3.setTotalScaleAngleSize(270)
        self.widget_3.setEnableBarGraph(True)
        self.widget_3.setEnableValueText(True)
        self.widget_3.setEnableCenterPoint(False)
        self.widget_3.setEnableNeedlePolygon(True)

        self.widget_3.setEnableScaleText(True)
        self.widget_3.setEnableScalePolygon(True)
        self.widget_3.setEnableBigScaleGrid(True)
        self.widget_3.setEnableFineScaleGrid(True)
        self.widget_3.setGaugeColorOuterRadiusFactor(1000)
        self.widget_3.setGaugeColorInnerRadiusFactor(600)
        self.widget_3.setNeedleColor(R=0, G=0, B=0, Transparency=255)
        #self.widget_3.setNeedleColorOnDrag(R=R, G=G, B=B, Transparency=Transparency)
        #self.widget_3.setScaleValueColor(R=R, G=G, B=B, Transparency=Transparency)
        #self.widget_3.setDisplayValueColor(R=R, G=G, B=B, Transparency=Transparency)
        self.widget_3.setGaugeTheme(0)
        #self.widget_3.setOuterCircleColor()
        red_scale_start = .29
        red_scale_end = 1
        yellow_spread = .01
        self.widget_3.set_scale_polygon_colors([[red_scale_start, Qt.red],
                                    [red_scale_start+yellow_spread, Qt.yellow],
                                    [red_scale_start+(yellow_spread*2), Qt.green],
                                    [red_scale_end-(yellow_spread*2), Qt.green],
                                    [red_scale_end-yellow_spread, Qt.yellow],
                                    [red_scale_end, Qt.red]])
        # self.widget_3.setCustomGaugeTheme(
        #     color1 = "red",
        #     color2= "purple",
        #     color3 = "blue"
        # )

        # self.widget_3.setScalePolygonColor(
        #     color1 = "green"
        # )

        # self.widget_3.setNeedleCenterColor(
        #     color1 = "white"
        # )

        # self.widget_3.setOuterCircleColor(
        #     color1 = "black"
        # )

        self.widget_3.setBigScaleColor("#005275")
        self.widget_3.setFineScaleColor("#005275")
        self.widget_3.setMouseTracking(False)

def Update_Table(self, file_name):
            
        try:
            
            if self.radioButton_Almaco.isChecked():
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    #need "Timestamp","ID_REC","Property_2_Value" to "Protein","Property_2_H" to "H", "Pro" 
                    csvFile = csvFile[['Timestamp','ID_REC',"Property_1_Value","Property_2_Value","Property_2_H","Property_2_S"]]
                    csvFile.rename(columns={'Property_2_Value': 'Protein', 'Property_2_H': 'H', "Property_2_S":"S"}, inplace=True)
                    csvFile_rev = csvFile[::-1].reset_index(drop=True)
                    formatted_panda = csvFile_rev
                    
            if self.radioButton_Other.isChecked():         
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    formatted_panda = csvFile

            if self.radioButton_Winter.isChecked():
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput, sep=";", decimal=",",usecols=[0,1,7,9,10],skiprows=1, header=None)
                    csvFile.columns = ['Timestamp','ID_REC','Protein','H','S']
                    csvFile_rev = csvFile[::-1].reset_index(drop=True)
                    formatted_panda = csvFile_rev
            
            no_row = len(formatted_panda)
            no_columns = len(formatted_panda.columns)
            self.entry_table.setColumnCount(no_columns)
            self.entry_table.setRowCount(no_row)
            rowNumber=0
            rowBad_count = 0
            decimal_places = 1
            try:
                for col in formatted_panda.columns:
                            text = col
                            index = formatted_panda.columns.to_list().index(col)
                            col = QTableWidgetItem(text)
                            self.entry_table.setHorizontalHeaderItem(index,col)
                for index, row in formatted_panda.iterrows():
                    rowBad = False

                    row_num = index
                    for column in row:
                        data = column
                        col_num = row.to_list().index(column)
                        col_name = formatted_panda.columns[col_num]
                        cell_item = QTableWidgetItem(str(column))

                        color = ""
                        try:
                            if isinstance(data, str) == True and col_name in ("Protein","H","S"):
                                data = data.replace(",",".")
                                data = round(float(data),decimal_places)
                                cell_item = QTableWidgetItem(str(data))
                                cell_item.setTextAlignment(Qt.AlignRight)
                            elif col_name in ("Protein","H","S"):
                                data = round(float(data),decimal_places)
                                cell_item = QTableWidgetItem(str(data))
                                cell_item.setTextAlignment(Qt.AlignRight)

                            if col_name == "H":
                                if data > 10:
                                    color = "red"
                                else:
                                    color = "green"
                                
                                if index == 0:
                                    self.widget_2.updateValue(data)
                                    
                                
                            if col_name == "S":
                                if data > 60:
                                    color = "red"
                                else:
                                    color = "green"                           
                            
                                if index == 0:
                                    self.widget_3.updateValue(data)

                            if col_name == "Protein":
                                if data < 5 or data > 80:
                                    color = "red"
                                else:
                                    color = ""
                            
                                if index == 0:
                                    #self.widget.updateValue(data)
                                    pass

                            if color == "red":
                                 rowBad = True

                        except Exception as e:
                            cell_item = QTableWidgetItem("error")
                            color = 'pink'
                            print(f"error in cell parsing column: {col_name},index: {index},data: {data}, Exception: {e}")

                        if color != "":
                            cell_item.setBackground(QtGui.QColor(color))

                        

                        self.entry_table.setItem(row_num,col_num,cell_item)


                    rowNumber = rowNumber + 1
                    if rowBad == True:
                        rowBad_count = rowBad_count + 1

            except Exception as e:
                print("error in cell parsing")
                print(f"column: {col_name}")
                print(f"index: {index}")
                print(f'data: {data}')
                
                print(e)
                self.textBrowser_Error.setPlainText("error in cell parsing,  " + str(e))
                self.textBrowser_Error.setStyleSheet(u"background-color: rgb(255, 0, 0);")
            self.entry_table.resizeColumnsToContents()
            first_row = formatted_panda.iloc[0]
            
            self.label_H_Value_Num.setText(str(first_row['H']))
            self.label_S_Value_Num.setText(str(first_row['S']))
            self.label_Bad_Num.setText(str(rowBad_count))
            self.label_Total_Num.setText(str(rowNumber))
            percent_good = int(((rowNumber - rowBad_count) / rowNumber) * 100)
            self.label_PerGood_Num.setText(str(percent_good) + "%")

            
            
            print(f"Number of rows Bad: {rowBad_count} out of {rowNumber}")
            self.textBrowser_Error.setPlainText("")
            self.textBrowser_Error.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        except Exception as e:
            print(e)
            self.textBrowser_Error.setPlainText(str(e))
            self.textBrowser_Error.setStyleSheet(u"background-color: rgb(255, 0, 0);")



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Combine UI")
        self.setGeometry(0,0,1920,1080)
        #self.setWindowIcon(QtGui.QIcon('BensonHillIngredients.png'))
        self.app = app



        Set_Guage_2_H(self)
        Set_Guage_3_S(self)
        



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







        
