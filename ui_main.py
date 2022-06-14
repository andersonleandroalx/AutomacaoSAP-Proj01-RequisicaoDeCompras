# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReqCompra.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(707, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(69, 129, 202);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 157, 235);\n"
"	\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.li_filepath = QLineEdit(self.frame)
        self.li_filepath.setObjectName(u"li_filepath")
        self.li_filepath.setMinimumSize(QSize(0, 30))
        self.li_filepath.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.li_filepath)

        self.bt_open = QPushButton(self.frame)
        self.bt_open.setObjectName(u"bt_open")
        self.bt_open.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.bt_open)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 157, 235);\n"
"	\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_go = QPushButton(self.frame_3)
        self.bt_go.setObjectName(u"bt_go")
        self.bt_go.setMinimumSize(QSize(160, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bt_go.setFont(font)

        self.horizontalLayout_3.addWidget(self.bt_go, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Automa\u00e7ao SAP - Criar Requisi\u00e7ao de Compra", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Criar Requisi\u00e7\u00e3o de Compra</span></p></body></html>", None))
        self.li_filepath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a planilha com os dados", None))
        self.bt_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.bt_go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
    # retranslateUi

