import pandas
import os
from datetime import datetime
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QMainWindow,QMessageBox,QFileDialog,QTableWidgetItem

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Combine UI")
        self.app = app

        

        #Signal slot connections
        self.pushButton.clicked.connect(self.select_file)
        

                    
         



    def select_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                 "",
                                 "Text(*.csv);;All files(*.*)")
        if((file_name == "")):
            return
        
        #_____________________________
        self.label.setText(file_name)
        document_name = os.path.basename(file_name)
        self.file_name_label.setText(document_name)
        file_timestamp = os.stat(file_name).st_mtime
        #_____________________________
               
        #TODO if statement of ALmaoc
        if self.radioButton_Almaco.isChecked():
            with open(file_name, "r") as fileInput:
                csvFile = pandas.read_csv(fileInput)
                #need "Timestamp","ID_REC","Property_2_Value" to "Protein","Property_2_H" to "H", "Pro" 

                csvFile = csvFile[['Timestamp','ID_REC',"Property_2_Value","Property_2_H","Property_2_S"]]
                csvFile.rename(columns={'Property_2_Value': 'Protein', 'Property_2_H': 'H', "Property_2_S":"S"}, inplace=True)
                csvFile_rev = csvFile[::-1].reset_index(drop=True)
                # for index, row in csvFile.iterrows():

                #     #datetime_str = row[0]
                #     #date_object = datetime.strptime(datetime_str, "%-m/%-d/%Y %-H:%M" )
                #     print(timestamp)
                #     timestamp = datetime.timestamp(timestamp)
                #     csvFile.at[index,"Timestamp"] = timestamp


                #csvFile.sort_values(by=['Timestamp'], ascending=False)
                print(csvFile)
                print(csvFile_rev)




                no_row = len(csvFile_rev)
                no_columns = len(csvFile_rev.columns)
                self.entry_table.setColumnCount(no_columns)
                self.entry_table.setRowCount(no_row)
                
                

                for col in csvFile_rev.columns:
                            text = col
                            index = csvFile_rev.columns.to_list().index(col)
                            col = QTableWidgetItem(text)
                            self.entry_table.setHorizontalHeaderItem(index,col)
                
                
                
                for index, row in csvFile_rev.iterrows():
                    row_num = index
                    for column in row:
                        data = column
                        col_num = row.to_list().index(column)
                        col_name = csvFile_rev.columns[col_num]


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
                        
             
         #TODO if statement of Winter
        if self.radioButton_Winter.isChecked():
            with open(file_name, "r") as fileInput:
                csvFile = pandas.read_csv(fileInput)
                no_row = len(csvFile)
                no_columns = len(csvFile.columns)
                self.entry_table.setColumnCount(no_columns)
                self.entry_table.setRowCount(no_row)
                

                for col in csvFile.columns:
                            text = col
                            index = csvFile.columns.to_list().index(col)
                            col = QTableWidgetItem(text)
                            self.entry_table.setHorizontalHeaderItem(index,col)
                
                
                
                for index, row in csvFile.iterrows():
                    row_num = index
                    for column in row:
                        data = column
                        col_num = row.to_list().index(column)
                        col_name = csvFile.columns[col_num]


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
             

        if self.radioButton_Other.isChecked():         
            with open(file_name, "r") as fileInput:
                csvFile = pandas.read_csv(fileInput)
                no_row = len(csvFile)
                no_columns = len(csvFile.columns)
                self.entry_table.setColumnCount(no_columns)
                self.entry_table.setRowCount(no_row)
                

                for col in csvFile.columns:
                            text = col
                            index = csvFile.columns.to_list().index(col)
                            col = QTableWidgetItem(text)
                            self.entry_table.setHorizontalHeaderItem(index,col)
                
                
                
                for index, row in csvFile.iterrows():
                    row_num = index
                    for column in row:
                        data = column
                        col_num = row.to_list().index(column)
                        col_name = csvFile.columns[col_num]


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


                    #cell_item.setBackground(color)
                    #self.entry_table.item(row_num,col_num).setBackground(QtGui.QColor(color))


                    
                    



                 
                 


        
                    


                # items = [
                #     QtGui.QStandardItem(field)
                #     for field in row
                # ]
                # self.entry_table.appendRow(items) 







    # def loadCsv(self, fileName):
    #     with open(fileName, "r") as fileInput:
    #         for row in csv.reader(fileInput):    
    #             items = [
    #                 QtGui.QStandardItem(field)
    #                 for field in row
    #             ]
    #             self.model.appendRow(items)      






    #TODO code the color change of table
    # def setColortoRow(self, rowIndex, color):
    #     for j in range(table.columnCount()):
    #         table.item(rowIndex, j).setBackground(color)
        

