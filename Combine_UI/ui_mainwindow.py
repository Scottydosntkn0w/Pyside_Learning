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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDial, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1883, 1055)
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
        self.widget = QWidget(self.groupBox_machineSetting)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 94, 96))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_Almaco = QRadioButton(self.widget)
        self.radioButton_Almaco.setObjectName(u"radioButton_Almaco")

        self.verticalLayout_2.addWidget(self.radioButton_Almaco)

        self.radioButton_Winter = QRadioButton(self.widget)
        self.radioButton_Winter.setObjectName(u"radioButton_Winter")

        self.verticalLayout_2.addWidget(self.radioButton_Winter)

        self.radioButton_Other = QRadioButton(self.widget)
        self.radioButton_Other.setObjectName(u"radioButton_Other")
        self.radioButton_Other.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton_Other)


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
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximumSize(QSize(526, 485))

        self.horizontalLayout.addWidget(self.dial)

        self.dial_2 = QDial(self.centralwidget)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setMaximumSize(QSize(525, 485))

        self.horizontalLayout.addWidget(self.dial_2)

        self.dial_3 = QDial(self.centralwidget)
        self.dial_3.setObjectName(u"dial_3")
        self.dial_3.setMaximumSize(QSize(526, 485))

        self.horizontalLayout.addWidget(self.dial_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.file_label = QLabel(self.splitter_2)
        self.file_label.setObjectName(u"file_label")
        sizePolicy1.setHeightForWidth(self.file_label.sizePolicy().hasHeightForWidth())
        self.file_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(20)
        self.file_label.setFont(font1)
        self.file_label.setFrameShape(QFrame.Panel)
        self.file_label.setFrameShadow(QFrame.Raised)
        self.splitter_2.addWidget(self.file_label)
        self.file_name_label = QLabel(self.splitter_2)
        self.file_name_label.setObjectName(u"file_name_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.file_name_label.sizePolicy().hasHeightForWidth())
        self.file_name_label.setSizePolicy(sizePolicy3)
        self.file_name_label.setFont(font1)
        self.file_name_label.setFrameShape(QFrame.Panel)
        self.file_name_label.setFrameShadow(QFrame.Raised)
        self.file_name_label.setLineWidth(1)
        self.file_name_label.setMidLineWidth(0)
        self.splitter_2.addWidget(self.file_name_label)

        self.verticalLayout.addWidget(self.splitter_2)

        self.entry_table = QTableWidget(self.centralwidget)
        if (self.entry_table.columnCount() < 10):
            self.entry_table.setColumnCount(10)
        if (self.entry_table.rowCount() < 1):
            self.entry_table.setRowCount(1)
        self.entry_table.setObjectName(u"entry_table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(7)
        sizePolicy4.setHeightForWidth(self.entry_table.sizePolicy().hasHeightForWidth())
        self.entry_table.setSizePolicy(sizePolicy4)
        self.entry_table.setAlternatingRowColors(True)
        self.entry_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.entry_table.setSortingEnabled(False)
        self.entry_table.setRowCount(1)
        self.entry_table.setColumnCount(10)

        self.verticalLayout.addWidget(self.entry_table)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1883, 22))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.file_label.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.file_name_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

