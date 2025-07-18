# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'per.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 10, 391, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.videoWidget = QWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setGeometry(QRect(20, 70, 491, 331))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(520, 60, 271, 121))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 241, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.guiji_checkBox = QCheckBox(self.layoutWidget)
        self.guiji_checkBox.setObjectName(u"guiji_checkBox")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.guiji_checkBox.setFont(font2)

        self.horizontalLayout.addWidget(self.guiji_checkBox)

        self.text_checkBox = QCheckBox(self.layoutWidget)
        self.text_checkBox.setObjectName(u"text_checkBox")
        self.text_checkBox.setFont(font2)

        self.horizontalLayout.addWidget(self.text_checkBox)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 207, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(520, 180, 271, 211))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.groupBox_2.setFont(font3)
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 60, 191, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(False)
        self.label_8.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.backward_label = QLabel(self.layoutWidget_2)
        self.backward_label.setObjectName(u"backward_label")
        sizePolicy.setHeightForWidth(self.backward_label.sizePolicy().hasHeightForWidth())
        self.backward_label.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.backward_label.setFont(font5)

        self.horizontalLayout_7.addWidget(self.backward_label)

        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 100, 161, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        self.label_2.setFont(font6)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.number_label = QLabel(self.layoutWidget2)
        self.number_label.setObjectName(u"number_label")

        self.horizontalLayout_3.addWidget(self.number_label)

        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 140, 161, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lblFPS_label = QLabel(self.layoutWidget3)
        self.lblFPS_label.setObjectName(u"lblFPS_label")

        self.horizontalLayout_4.addWidget(self.lblFPS_label)

        self.layoutWidget4 = QWidget(self.groupBox_2)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 170, 221, 27))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lblElapsedTime_label = QLabel(self.layoutWidget4)
        self.lblElapsedTime_label.setObjectName(u"lblElapsedTime_label")

        self.horizontalLayout_5.addWidget(self.lblElapsedTime_label)

        self.layoutWidget5 = QWidget(self.groupBox_2)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(21, 30, 191, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.forward_label = QLabel(self.layoutWidget5)
        self.forward_label.setObjectName(u"forward_label")
        sizePolicy.setHeightForWidth(self.forward_label.sizePolicy().hasHeightForWidth())
        self.forward_label.setSizePolicy(sizePolicy)
        self.forward_label.setFont(font5)

        self.horizontalLayout_6.addWidget(self.forward_label)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(520, 390, 271, 161))
        self.groupBox_3.setFont(font3)
        self.vedio_pushButton = QPushButton(self.groupBox_3)
        self.vedio_pushButton.setObjectName(u"vedio_pushButton")
        self.vedio_pushButton.setGeometry(QRect(60, 30, 131, 41))
        self.vedio_pushButton.setFont(font5)
        self.camera_pushButton = QPushButton(self.groupBox_3)
        self.camera_pushButton.setObjectName(u"camera_pushButton")
        self.camera_pushButton.setGeometry(QRect(60, 90, 131, 41))
        self.camera_pushButton.setFont(font5)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 400, 491, 151))
        font7 = QFont()
        font7.setPointSize(12)
        self.groupBox_4.setFont(font7)
        self.inf_tableWidget = QTableWidget(self.groupBox_4)
        self.inf_tableWidget.setObjectName(u"inf_tableWidget")
        self.inf_tableWidget.setGeometry(QRect(10, 20, 471, 121))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u6df1\u5ea6\u5b66\u4e60\u7684\u884c\u4eba\u68c0\u6d4b\u8ffd\u8e2a\u4e0e\u7edf\u8ba1\u7cfb\u7edf", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.guiji_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8ffd\u8e2a\u8f68\u8ff9", None))
        self.text_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6807\u7b7e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6\u9608\u503c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u901a\u884c\u6570:", None))
        self.backward_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u901a\u884c\u603b\u6570\uff1a", None))
        self.number_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u5e27\u7387\uff1a", None))
        self.lblFPS_label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u68c0\u6d4b\u65f6\u957f\uff1a", None))
        self.lblElapsedTime_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5411\u901a\u884c\u6570:", None))
        self.forward_label.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.vedio_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u89c6\u9891", None))
        self.camera_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c\u4e0e\u4f4d\u7f6e\u4fe1\u606f", None))
    # retranslateUi

