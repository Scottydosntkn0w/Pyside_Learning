
import tkinter as tk
from tkinter import filedialog
import pandas
import csv
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path, "r") as fileInput:

    # Skips the heading 
    # Using next() method 
     
    header = pandas.read_csv(fileInput,index_col=0, nrows=0).columns.tolist()
    print(header)
    csvFile = pandas.read_csv(fileInput, sep=";", decimal=",")
    print(csvFile)


        


    # csvFile = pandas.read_csv(fileInput)
    # print(csvFile)
    # #need "Timestamp","ID_REC","Property_2_Value" to "Protein","Property_2_H" to "H", "Pro" 
    # csvFile = csvFile[['Timestamp','ID_REC',"Property_2_Value","Property_2_H","Property_2_S"]]
    # csvFile.rename(columns={'Property_2_Value': 'Protein', 'Property_2_H': 'H', "Property_2_S":"S"}, inplace=True)
    # csvFile_rev = csvFile[::-1].reset_index(drop=True)
    # formatted_panda = csvFile_rev