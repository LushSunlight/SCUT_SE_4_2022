# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BeforeRun.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BeforeRun(object):
    def setupUi(self, BeforeRun):
        BeforeRun.setObjectName("BeforeRun")
        BeforeRun.resize(719, 357)
        self.centralwidget = QtWidgets.QWidget(BeforeRun)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 50, 441, 111))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 261, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 30, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 70, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        BeforeRun.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BeforeRun)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 26))
        self.menubar.setObjectName("menubar")
        BeforeRun.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BeforeRun)
        self.statusbar.setObjectName("statusbar")
        BeforeRun.setStatusBar(self.statusbar)

        self.retranslateUi(BeforeRun)
        QtCore.QMetaObject.connectSlotsByName(BeforeRun)

    def retranslateUi(self, BeforeRun):
        _translate = QtCore.QCoreApplication.translate
        BeforeRun.setWindowTitle(_translate("BeforeRun", "MainWindow"))
        self.groupBox.setTitle(_translate("BeforeRun", "监控参数设定"))
        self.label_2.setText(_translate("BeforeRun", "迭代的次数："))
        self.label_3.setText(_translate("BeforeRun", "每次迭代显示数据停留的时间（秒）："))
        self.pushButton.setText(_translate("BeforeRun", "开始迭代"))
