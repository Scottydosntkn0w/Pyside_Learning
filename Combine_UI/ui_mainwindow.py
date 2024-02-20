# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget
import Main_Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1874, 1097)
        icon = QIcon()
        icon.addFile(u":/Benson_Hill_Icons/BensonHillIngredients.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_options = QGroupBox(self.centralwidget)
        self.groupBox_options.setObjectName(u"groupBox_options")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_options.sizePolicy().hasHeightForWidth())
        self.groupBox_options.setSizePolicy(sizePolicy)
        self.groupBox_options.setMinimumSize(QSize(236, 0))
        self.groupBox_options.setMaximumSize(QSize(236, 16777215))
        self.groupBox_machineSetting = QGroupBox(self.groupBox_options)
        self.groupBox_machineSetting.setObjectName(u"groupBox_machineSetting")
        self.groupBox_machineSetting.setGeometry(QRect(10, 30, 131, 131))
        self.layoutWidget = QWidget(self.groupBox_machineSetting)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 94, 96))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_Almaco = QRadioButton(self.layoutWidget)
        self.radioButton_Almaco.setObjectName(u"radioButton_Almaco")

        self.verticalLayout_2.addWidget(self.radioButton_Almaco)

        self.radioButton_Winter = QRadioButton(self.layoutWidget)
        self.radioButton_Winter.setObjectName(u"radioButton_Winter")

        self.verticalLayout_2.addWidget(self.radioButton_Winter)

        self.radioButton_Other = QRadioButton(self.layoutWidget)
        self.radioButton_Other.setObjectName(u"radioButton_Other")
        self.radioButton_Other.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton_Other)

        self.groupBox_Error = QGroupBox(self.groupBox_options)
        self.groupBox_Error.setObjectName(u"groupBox_Error")
        self.groupBox_Error.setGeometry(QRect(10, 160, 211, 231))
        self.textBrowser_Error = QTextBrowser(self.groupBox_Error)
        self.textBrowser_Error.setObjectName(u"textBrowser_Error")
        self.textBrowser_Error.setEnabled(True)
        self.textBrowser_Error.setGeometry(QRect(10, 30, 191, 191))
        self.textBrowser_Error.setMouseTracking(True)
        self.textBrowser_Error.setAutoFillBackground(True)
        self.textBrowser_Error.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_2.addWidget(self.groupBox_options)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setFlat(False)
        self.splitter.addWidget(self.pushButton)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setIndent(0)
        self.splitter.addWidget(self.label)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.FirstGraph_QFrame = QFrame(self.centralwidget)
        self.FirstGraph_QFrame.setObjectName(u"FirstGraph_QFrame")
        self.FirstGraph_QFrame.setMinimumSize(QSize(0, 100))
        self.FirstGraph_QFrame.setFrameShape(QFrame.StyledPanel)
        self.FirstGraph_QFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.FirstGraph_QFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.protein_label = QLabel(self.FirstGraph_QFrame)
        self.protein_label.setObjectName(u"protein_label")

        self.horizontalLayout_3.addWidget(self.protein_label)

        self.last_protei_value_label = QLabel(self.FirstGraph_QFrame)
        self.last_protei_value_label.setObjectName(u"last_protei_value_label")

        self.horizontalLayout_3.addWidget(self.last_protei_value_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.widget = AnalogGaugeWidget(self.FirstGraph_QFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 300))

        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.FirstGraph_QFrame)

        self.SecondGraph_QFrame = QFrame(self.centralwidget)
        self.SecondGraph_QFrame.setObjectName(u"SecondGraph_QFrame")
        self.SecondGraph_QFrame.setFrameShape(QFrame.StyledPanel)
        self.SecondGraph_QFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.SecondGraph_QFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_H_Value = QLabel(self.SecondGraph_QFrame)
        self.label_H_Value.setObjectName(u"label_H_Value")

        self.horizontalLayout_4.addWidget(self.label_H_Value)

        self.label_H_Value_Num = QLabel(self.SecondGraph_QFrame)
        self.label_H_Value_Num.setObjectName(u"label_H_Value_Num")

        self.horizontalLayout_4.addWidget(self.label_H_Value_Num)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.widget_2 = AnalogGaugeWidget(self.SecondGraph_QFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 300))

        self.verticalLayout_4.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.SecondGraph_QFrame)

        self.ThirGraph_QFrame = QFrame(self.centralwidget)
        self.ThirGraph_QFrame.setObjectName(u"ThirGraph_QFrame")
        self.ThirGraph_QFrame.setMinimumSize(QSize(0, 100))
        self.ThirGraph_QFrame.setFrameShape(QFrame.StyledPanel)
        self.ThirGraph_QFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.ThirGraph_QFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_S_Value = QLabel(self.ThirGraph_QFrame)
        self.label_S_Value.setObjectName(u"label_S_Value")

        self.horizontalLayout_5.addWidget(self.label_S_Value)

        self.label_S_Value_Num = QLabel(self.ThirGraph_QFrame)
        self.label_S_Value_Num.setObjectName(u"label_S_Value_Num")

        self.horizontalLayout_5.addWidget(self.label_S_Value_Num)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.widget_3 = AnalogGaugeWidget(self.ThirGraph_QFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(300, 300))
        self.widget_3.setMouseTracking(False)

        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.ThirGraph_QFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.file_name_label = QLabel(self.splitter_2)
        self.file_name_label.setObjectName(u"file_name_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.file_name_label.sizePolicy().hasHeightForWidth())
        self.file_name_label.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(20)
        self.file_name_label.setFont(font1)
        self.file_name_label.setFrameShape(QFrame.Panel)
        self.file_name_label.setFrameShadow(QFrame.Raised)
        self.file_name_label.setLineWidth(1)
        self.file_name_label.setMidLineWidth(0)
        self.splitter_2.addWidget(self.file_name_label)
        self.File_timestamp_Label = QLabel(self.splitter_2)
        self.File_timestamp_Label.setObjectName(u"File_timestamp_Label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.File_timestamp_Label.sizePolicy().hasHeightForWidth())
        self.File_timestamp_Label.setSizePolicy(sizePolicy4)
        self.splitter_2.addWidget(self.File_timestamp_Label)

        self.verticalLayout.addWidget(self.splitter_2)

        self.groupBoxStats = QGroupBox(self.centralwidget)
        self.groupBoxStats.setObjectName(u"groupBoxStats")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.groupBoxStats.sizePolicy().hasHeightForWidth())
        self.groupBoxStats.setSizePolicy(sizePolicy5)
        self.groupBoxStats.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.groupBoxStats.setFont(font2)
        self.groupBoxStats.setAcceptDrops(False)
        self.horizontalLayoutWidget_4 = QWidget(self.groupBoxStats)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 10, 1591, 71))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_Bad = QLabel(self.horizontalLayoutWidget_4)
        self.label_Bad.setObjectName(u"label_Bad")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.label_Bad.setFont(font3)
        self.label_Bad.setIndent(1)

        self.horizontalLayout_6.addWidget(self.label_Bad)

        self.label_Bad_Num = QLabel(self.horizontalLayoutWidget_4)
        self.label_Bad_Num.setObjectName(u"label_Bad_Num")
        sizePolicy4.setHeightForWidth(self.label_Bad_Num.sizePolicy().hasHeightForWidth())
        self.label_Bad_Num.setSizePolicy(sizePolicy4)
        self.label_Bad_Num.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_Bad_Num)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_Total = QLabel(self.horizontalLayoutWidget_4)
        self.label_Total.setObjectName(u"label_Total")
        self.label_Total.setFont(font3)
        self.label_Total.setIndent(1)

        self.horizontalLayout_7.addWidget(self.label_Total)

        self.label_Total_Num = QLabel(self.horizontalLayoutWidget_4)
        self.label_Total_Num.setObjectName(u"label_Total_Num")
        sizePolicy4.setHeightForWidth(self.label_Total_Num.sizePolicy().hasHeightForWidth())
        self.label_Total_Num.setSizePolicy(sizePolicy4)
        self.label_Total_Num.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_Total_Num)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_PerGood = QLabel(self.horizontalLayoutWidget_4)
        self.label_PerGood.setObjectName(u"label_PerGood")
        self.label_PerGood.setFont(font3)
        self.label_PerGood.setScaledContents(True)
        self.label_PerGood.setIndent(1)

        self.horizontalLayout_8.addWidget(self.label_PerGood)

        self.label_PerGood_Num = QLabel(self.horizontalLayoutWidget_4)
        self.label_PerGood_Num.setObjectName(u"label_PerGood_Num")
        sizePolicy4.setHeightForWidth(self.label_PerGood_Num.sizePolicy().hasHeightForWidth())
        self.label_PerGood_Num.setSizePolicy(sizePolicy4)
        self.label_PerGood_Num.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_PerGood_Num)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addWidget(self.groupBoxStats)

        self.entry_table = QTableWidget(self.centralwidget)
        if (self.entry_table.columnCount() < 10):
            self.entry_table.setColumnCount(10)
        if (self.entry_table.rowCount() < 1):
            self.entry_table.setRowCount(1)
        self.entry_table.setObjectName(u"entry_table")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(7)
        sizePolicy6.setHeightForWidth(self.entry_table.sizePolicy().hasHeightForWidth())
        self.entry_table.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.entry_table.setFont(font4)
        self.entry_table.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.entry_table.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.entry_table.setLineWidth(2)
        self.entry_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.entry_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.entry_table.setAlternatingRowColors(True)
        self.entry_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.entry_table.setSortingEnabled(False)
        self.entry_table.setRowCount(1)
        self.entry_table.setColumnCount(10)
        self.entry_table.horizontalHeader().setCascadingSectionResizes(True)
        self.entry_table.horizontalHeader().setMinimumSectionSize(100)
        self.entry_table.horizontalHeader().setDefaultSectionSize(200)
        self.entry_table.horizontalHeader().setStretchLastSection(False)
        self.entry_table.verticalHeader().setMinimumSectionSize(20)
        self.entry_table.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout.addWidget(self.entry_table)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(4, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1874, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.groupBox_machineSetting.setTitle(QCoreApplication.translate("MainWindow", u"Choose Machine", None))
        self.radioButton_Almaco.setText(QCoreApplication.translate("MainWindow", u"Almaco", None))
        self.radioButton_Winter.setText(QCoreApplication.translate("MainWindow", u"Winter", None))
        self.radioButton_Other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.groupBox_Error.setTitle(QCoreApplication.translate("MainWindow", u"Error Message", None))
        self.textBrowser_Error.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No Error</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.protein_label.setText(QCoreApplication.translate("MainWindow", u"Protein", None))
        self.last_protei_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_H_Value.setText(QCoreApplication.translate("MainWindow", u"H Value", None))
        self.label_H_Value_Num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_S_Value.setText(QCoreApplication.translate("MainWindow", u"S Value", None))
        self.label_S_Value_Num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.file_name_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.File_timestamp_Label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBoxStats.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_Bad.setText(QCoreApplication.translate("MainWindow", u"Bad:", None))
        self.label_Bad_Num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_Total.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_Total_Num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_PerGood.setText(QCoreApplication.translate("MainWindow", u"% Good:", None))
        self.label_PerGood_Num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

