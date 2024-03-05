import pandas
import os
from PySide6 import QtGui
from PySide6.QtCore import Qt,QTimer
from PySide6.QtWidgets import  QMainWindow,QFileDialog,QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
from datetime import datetime


timer = QTimer()

def harvest_speed(self,current_day,current_time,No_plots_day,days_first_datetime,reset_day,reset_time,No_Plots_after_reset):

    current_hours = current_time[0]
    current_mins = current_time[1]
    
    days_first_plot_day = days_first_datetime[0]
    days_first_plot_time = days_first_datetime[1]
    days_first_plot_time = days_first_plot_time.split(":")
    days_first_plot_hours = days_first_plot_time[0]
    days_first_plot_mins = days_first_plot_time[1]
    if isinstance(reset_time, str):
        if reset_time != "N/A":
            reset_time = reset_time.split(":")
        else:
            reset_time = [days_first_plot_hours,days_first_plot_mins]
    reset_time_hours = reset_time[0]
    reset_time_mins = reset_time[1]


    current_time_mins = (int(current_hours) * 60) + int(current_mins)
    days_first_plot_time_mins = (int(days_first_plot_hours) * 60) + int(days_first_plot_mins)
    reset_time_total_mins = (int(reset_time_hours) * 60) + int(reset_time_mins)

    Time_after_reset_mins = current_time_mins - reset_time_total_mins

    plots_per_hour_after_reset = No_Plots_after_reset / (Time_after_reset_mins/60)

    self.label_Current_Day_No.setText(current_day)

    Total_Time_mins = current_time_mins - days_first_plot_time_mins
    Total_Time_hrs = Total_Time_mins / 60
    self.label_Total_Time_Day_No.setText(str(Total_Time_hrs))
    self.label_Plot_Day_No.setText(str(No_plots_day))
    Plots_per_hour = No_plots_day / Total_Time_hrs
    self.label_PlotHr_Day_No.setText(str(Plots_per_hour))

    self.label_S_Value_Num.setText(f"{reset_day} {reset_time_hours}:{reset_time_mins}")
    self.label_Speed_Plots_Number.setText(str(No_Plots_after_reset))

    self.widget_3.updateValue(int(plots_per_hour_after_reset))



    """ 
    plots/day Calculation Requirments: 
    Limit readings to the day 
    need total plots for the day
    running time for the day
    duration of first plot for the day needs to be assumed and added

    plots/hr calculation:
    need user input to set "start time" then will look at all plots after that time
    start time will default first plot in the day time.
    total plots after start time
    duration: time_of_last plot - start_time

    UI Elements:
    Daily Statistics:
        Current Day
        Plots
        Total Hrs
        Plots/Hr
    
    Speed Guage:
        Guage (plot/hr): highly dependent on machine and operator
            RED: TBD
            Yellow: TBD
            Green: TBD
        Reset Button
        Start Time
        # of Plots 

    """
    


    pass

def Set_Guage_3_Speed(self):
        # Setup Guage
        self.widget_3.units = "Plots/Hr"
        self.widget_3.minValue = 0
        self.widget_3.maxValue = 200
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
        red_scale_end = .7
        yellow_spread = .1
        self.widget_3.set_scale_polygon_colors([[red_scale_start, Qt.cyan],
                                    [red_scale_start+yellow_spread, Qt.green],
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
        No_Plots_after_reset = 0
        if self.label_S_Value_Num.text() != "NA":
            reset_day_time = self.label_S_Value_Num.text()
            reset_day_time = reset_day_time.split(" ")
            reset_day = reset_day_time[0]
            reset_time = reset_day_time[1]
            reset_time_split = reset_time.split(":")
            reset_hours = reset_time_split[0]
            reset_mins =  reset_time_split[1]

        try:
            
            if self.radioButton_Almaco.isChecked():
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    #need "Timestamp","ID_REC","Property_2_Value" to "Protein","Property_2_H" to "H", "Pro" 
                    csvFile = csvFile[['Timestamp','ID_REC',"Property_1_Value","Property_1_H","Property_1_S","Property_2_Value","Property_2_H","Property_2_S"]]
                    csvFile.rename(columns={'Timestamp':'Time','Property_1_Value': 'Oil', 'Property_1_H': 'Oil_H', "Property_1_S":"Oil_S",'Property_2_Value': 'Protein', 'Property_2_H': 'H', "Property_2_S":"S"}, inplace=True)
                    csvFile_rev = csvFile[::-1].reset_index(drop=True)
                    formatted_panda = csvFile_rev
                    
                    
            if self.radioButton_Other.isChecked():         
                with open(file_name, "r") as fileInput:
                    csvFile = pandas.read_csv(fileInput)
                    formatted_panda = csvFile

            if self.radioButton_Winter.isChecked():
                with open(file_name, "r") as fileInput:
                    #csvFile = pandas.read_csv(fileInput, sep=";", decimal=",",usecols=[0,1,7,9,10,14,16,17],skiprows=1, header=None, on_bad_lines='warn')
                    #csvFile = pandas.read_csv(fileInput, sep=";", decimal=",",skiprows=1, header=None, on_bad_lines='warn')
                    df = pandas.read_fwf(fileInput, header=None)
                    df = df.iloc[1:, :]
                    df = df[0].str.split(';', expand=True)
                    print(df)
                    if self.radioButton_Soy.isChecked(): 
                        cols = [0,1,7,9,10,13,15,16]
                        cols_names = ['Time','ID_REC','Oil','Oil_H','Oil_S','Protein','H','S']
                    if self.radioButton_Yellow_Pea.isChecked():
                        cols = [0,1,7,9,10]
                        cols_names = ['Time','ID_REC','Protein','H','S']
                    csvFile = df[df.columns[cols]]
                    print(csvFile)
                    csvFile.columns = cols_names
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
                            if isinstance(data, str) == True and col_name in ("Protein","H","S","Oil","Oil_H","Oil_S"):
                                try:
                                    data = data.replace(",",".")
                                    data = round(float(data),decimal_places)
                                except Exception as e: 
                                    data = "error"
                                    color = 'pink'
                                    print(f"error in cell parsing column: {col_name},index: {index},data: {data}, Exception: {e}")

                                cell_item = QTableWidgetItem(str(data))
                                cell_item.setTextAlignment(Qt.AlignRight)
                                

                            elif col_name in ("Protein","H","S","Oil","Oil_H","Oil_S"):
                                if isinstance(data, float):
                                    data = round(float(data),decimal_places)
                                cell_item = QTableWidgetItem(str(data))
                                cell_item.setTextAlignment(Qt.AlignRight)
                            elif col_name == "Time":
                                #2023-08-17 22:14:27
                                #10/11/2022 14:01
                                date_time = data.split(" ")
                                date = date_time[0]
                                time = date_time[1]
                                time = time.split(":")
                                hours = time[0]
                                minutes = time[1]
                                if int(hours) >= 12:
                                    if int(hours) > 12:
                                        hours_12 = int(hours) - 12 
                                    else:
                                        hours_12 = hours
                                    meridian = "pm"
                                else:
                                    meridian = "am"
                                    hours_12 = hours
                                data = f"{hours_12}:{minutes} {meridian}"

                                cell_item = QTableWidgetItem(str(data))

                            if col_name == "H" or col_name == "Oil_H":
                                if data > 10:
                                    color = "red"
                                else:
                                    color = "green"
                                
                                if index == 0:
                                    #self.widget_2.updateValue(data)
                                    pass
                                
                            if col_name == "S" or col_name == "Oil_S":
                                if data > 60:
                                    color = "red"
                                else:
                                    color = "green"                           
                            
                                if index == 0:
                                    #self.widget_3.updateValue(data)
                                    pass

                            if col_name == "Protein" or col_name == "Oil":
                                # if data < 5 or data > 80:
                                #     color = "red"
                                # else:
                                #     color = ""
                            
                                if index == 0:
                                    #self.widget.updateValue(data)
                                    pass
                            
                            if col_name == "Time":
                                try:
                                    if index == 0:
                                        current_day = date
                                        current_time = time
                                        No_plots_day = 1
                                        if self.label_S_Value_Num.text() == "NA":
                                            reset_day = date
                                            reset_time = "N/A"
                                            reset_hours = 0
                                            reset_mins = 0
                                        
                                    if index != 0 and date == current_day:
                                        No_plots_day = No_plots_day + 1
                                        date_time_day_first = date_time
                                    
                                    if date == reset_day:
                                        if int(hours) > int(reset_hours):
                                            No_Plots_after_reset = No_Plots_after_reset + 1
                                        if int(hours) == int(reset_hours) and int(minutes) >= int(reset_mins):
                                            No_Plots_after_reset = No_Plots_after_reset + 1
                                except:
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

            harvest_speed(self,current_day,current_time,No_plots_day,date_time_day_first,reset_day,reset_time,No_Plots_after_reset)

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



        
        Set_Guage_3_Speed(self)
    

        #Signal slot connections
        self.pushButton_Reset_Speed.clicked.connect(self.reset_plot_per_hour)
        self.radioButton_Almaco.clicked.connect(self.toggle_to_soy)
        self.radioButton_Winter.clicked.connect(self.enable_yp)
        self.pushButton.clicked.connect(self.select_file)
    
    def reset_plot_per_hour(self):
        now = datetime.now()
        #2023-08-17 22:14:27 winter
        #10/11/2022 14:01 almaco
        if self.radioButton_Almaco.isChecked():
            current_date_time = now.strftime("%m/%d/%Y %H:%M")
        if self.radioButton_Other.isChecked():
            current_date_time = now.strftime("%m/%d/%Y %H:%M")
        if self.radioButton_Winter.isChecked():
            current_date_time = now.strftime("%Y-%m-%d %H:%M")
        self.label_S_Value_Num.setText(current_date_time)
        self.label_Speed_Plots_Number.setText("0")
        self.widget_3.updateValue(0)
        


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

    def toggle_to_soy(self):
        self.radioButton_Yellow_Pea.setDisabled(True)
        self.radioButton_Yellow_Pea.text
        self.radioButton_Soy.setChecked(True)
        self.radioButton_Yellow_Pea.setStyleSheet('color: "gray"')
    def enable_yp(self):
        self.radioButton_Yellow_Pea.setEnabled(True)
        self.radioButton_Yellow_Pea.setStyleSheet('color: "white"')





        
