# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 677)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 331, 281))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(60)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button1.setObjectName("button1")
        self.gridLayout_4.addWidget(self.button1, 3, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 0, 331, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 151, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(180, 30, 131, 21))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 70, 131, 21))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(180, 110, 131, 21))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(180, 150, 131, 21))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_5.setGeometry(QtCore.QRect(180, 190, 131, 21))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.button2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button2.setGeometry(QtCore.QRect(10, 240, 150, 23))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.groupBox_2)
        self.button3.setGeometry(QtCore.QRect(170, 240, 150, 23))
        self.button3.setObjectName("button3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 280, 671, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 701, 113))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 50, 109, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.button4 = QtWidgets.QPushButton(self.groupBox_3)
        self.button4.setGeometry(QtCore.QRect(550, 80, 109, 28))
        self.button4.setObjectName("button4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 410, 671, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 650, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(550, 20, 109, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.button5 = QtWidgets.QPushButton(self.groupBox_4)
        self.button5.setGeometry(QtCore.QRect(550, 50, 109, 28))
        self.button5.setObjectName("button5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 500, 671, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_5)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.groupBox_5)
        self.button6.setGeometry(QtCore.QRect(510, 30, 150, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setObjectName("button6")
        self.button7 = QtWidgets.QPushButton(self.groupBox_5)
        self.button7.setGeometry(QtCore.QRect(510, 60, 150, 23))
        self.button7.setObjectName("button7")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_6.setGeometry(QtCore.QRect(140, 30, 131, 21))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_7.setGeometry(QtCore.QRect(140, 60, 131, 21))
        self.textBrowser_7.setObjectName("textBrowser_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.label_2.setText(_translate("MainWindow", "Permutation Symm"))
        self.label_3.setText(_translate("MainWindow", "Data File Name"))
        self.label.setText(_translate("MainWindow", "Max Order"))
        self.button1.setText(_translate("MainWindow", "Generate Basis"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output"))
        self.label_6.setText(_translate("MainWindow", "Polynomial Order"))
        self.label_5.setText(_translate("MainWindow", "Num Configurations"))
        self.label_8.setText(_translate("MainWindow", "Num Coefficients"))
        self.label_7.setText(_translate("MainWindow", "Symmetry"))
        self.label_4.setText(_translate("MainWindow", "Num Atoms"))
        self.button2.setText(_translate("MainWindow", "Continue"))
        self.button3.setText(_translate("MainWindow", "Exit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Weights"))
        self.label_9.setText(_translate("MainWindow", "We can apply weight in the fitting, and the weight of each point is given by wt = E0/(E0+dE),\n"
"where dE is the energy of that point relative to the minimum. E0 is a user-specified parameter\n"
"(in unit Hartree)."))
        self.label_10.setText(_translate("MainWindow", "If you would like to apply the weight, please input the E0 parameter. Otherwise please\n"
"enter \"n\"."))
        self.button4.setText(_translate("MainWindow", "Input"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Parameters"))
        self.label_11.setText(_translate("MainWindow", "Please specify the a0 parameter (in unit Bohr) used in Morse variable yij = exp(-rij/a0). \n"
"The recommended range is 2.0-3.0 Bohr."))
        self.button5.setText(_translate("MainWindow", "Input"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Fitting"))
        self.label_12.setText(_translate("MainWindow", "Overall RMSE"))
        self.label_13.setText(_translate("MainWindow", "Weighted RMSE"))
        self.button6.setText(_translate("MainWindow", "Compute"))
        self.button7.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
