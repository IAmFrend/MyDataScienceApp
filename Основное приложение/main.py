# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(520, 694)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblRegion = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRegion.sizePolicy().hasHeightForWidth())
        self.lblRegion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblRegion.setFont(font)
        self.lblRegion.setFrameShape(QtWidgets.QFrame.Box)
        self.lblRegion.setTextFormat(QtCore.Qt.PlainText)
        self.lblRegion.setObjectName("lblRegion")
        self.horizontalLayout.addWidget(self.lblRegion)
        self.cbRegion = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbRegion.sizePolicy().hasHeightForWidth())
        self.cbRegion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.cbRegion.setFont(font)
        self.cbRegion.setObjectName("cbRegion")
        self.horizontalLayout.addWidget(self.cbRegion)
        self.tbRegion = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbRegion.sizePolicy().hasHeightForWidth())
        self.tbRegion.setSizePolicy(sizePolicy)
        self.tbRegion.setMaxLength(32768)
        self.tbRegion.setObjectName("tbRegion")
        self.horizontalLayout.addWidget(self.tbRegion)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblPosition = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPosition.sizePolicy().hasHeightForWidth())
        self.lblPosition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblPosition.setFont(font)
        self.lblPosition.setFrameShape(QtWidgets.QFrame.Box)
        self.lblPosition.setTextFormat(QtCore.Qt.PlainText)
        self.lblPosition.setObjectName("lblPosition")
        self.horizontalLayout_2.addWidget(self.lblPosition)
        self.cbPosition = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.cbPosition.setFont(font)
        self.cbPosition.setObjectName("cbPosition")
        self.horizontalLayout_2.addWidget(self.cbPosition)
        self.tbPosition = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbPosition.sizePolicy().hasHeightForWidth())
        self.tbPosition.setSizePolicy(sizePolicy)
        self.tbPosition.setObjectName("tbPosition")
        self.horizontalLayout_2.addWidget(self.tbPosition)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblDate = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDate.sizePolicy().hasHeightForWidth())
        self.lblDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblDate.setFont(font)
        self.lblDate.setFrameShape(QtWidgets.QFrame.Box)
        self.lblDate.setObjectName("lblDate")
        self.horizontalLayout_5.addWidget(self.lblDate)
        self.cbDate = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDate.sizePolicy().hasHeightForWidth())
        self.cbDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.cbDate.setFont(font)
        self.cbDate.setObjectName("cbDate")
        self.horizontalLayout_5.addWidget(self.cbDate)
        self.dtDate = QtWidgets.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.dtDate.setFont(font)
        self.dtDate.setObjectName("dtDate")
        self.horizontalLayout_5.addWidget(self.dtDate)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblValue = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValue.sizePolicy().hasHeightForWidth())
        self.lblValue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblValue.setFont(font)
        self.lblValue.setFrameShape(QtWidgets.QFrame.Box)
        self.lblValue.setObjectName("lblValue")
        self.horizontalLayout_6.addWidget(self.lblValue)
        self.cbValue = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbValue.sizePolicy().hasHeightForWidth())
        self.cbValue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.cbValue.setFont(font)
        self.cbValue.setObjectName("cbValue")
        self.horizontalLayout_6.addWidget(self.cbValue)
        self.spValue = QtWidgets.QSpinBox(self.centralwidget)
        self.spValue.setMaximum(999999999)
        self.spValue.setObjectName("spValue")
        self.horizontalLayout_6.addWidget(self.spValue)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.tbLine = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tbLine.sizePolicy().hasHeightForWidth())
        self.tbLine.setSizePolicy(sizePolicy)
        self.tbLine.setObjectName("tbLine")
        self.tbLine.setColumnCount(0)
        self.tbLine.setRowCount(0)
        self.verticalLayout.addWidget(self.tbLine)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblAllRecords = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.lblAllRecords.setFont(font)
        self.lblAllRecords.setObjectName("lblAllRecords")
        self.verticalLayout_2.addWidget(self.lblAllRecords)
        self.lblRegLines = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.lblRegLines.setFont(font)
        self.lblRegLines.setObjectName("lblRegLines")
        self.verticalLayout_2.addWidget(self.lblRegLines)
        self.lblPosLines = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.lblPosLines.setFont(font)
        self.lblPosLines.setObjectName("lblPosLines")
        self.verticalLayout_2.addWidget(self.lblPosLines)
        self.lblLineRecord = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.lblLineRecord.setFont(font)
        self.lblLineRecord.setObjectName("lblLineRecord")
        self.verticalLayout_2.addWidget(self.lblLineRecord)
        self.lblOutput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblOutput.setFont(font)
        self.lblOutput.setObjectName("lblOutput")
        self.verticalLayout_2.addWidget(self.lblOutput)
        self.lblMediane = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblMediane.setFont(font)
        self.lblMediane.setObjectName("lblMediane")
        self.verticalLayout_2.addWidget(self.lblMediane)
        self.lblOutputMediane = QtWidgets.QLabel(self.centralwidget)
        self.lblOutputMediane.setObjectName("lblOutputMediane")
        self.verticalLayout_2.addWidget(self.lblOutputMediane)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.btFile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btFile.sizePolicy().hasHeightForWidth())
        self.btFile.setSizePolicy(sizePolicy)
        self.btFile.setObjectName("btFile")
        self.verticalLayout.addWidget(self.btFile)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btCab = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btCab.sizePolicy().hasHeightForWidth())
        self.btCab.setSizePolicy(sizePolicy)
        self.btCab.setObjectName("btCab")
        self.horizontalLayout_3.addWidget(self.btCab)
        self.lblUser = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUser.sizePolicy().hasHeightForWidth())
        self.lblUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblUser.setFont(font)
        self.lblUser.setObjectName("lblUser")
        self.horizontalLayout_3.addWidget(self.lblUser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Статистика"))
        self.lblRegion.setText(_translate("MainWindow", "Регион"))
        self.lblPosition.setText(_translate("MainWindow", "Статья"))
        self.lblDate.setText(_translate("MainWindow", "Дата"))
        self.lblValue.setText(_translate("MainWindow", "Значение"))
        self.lblAllRecords.setText(_translate("MainWindow", "Всего записей:"))
        self.lblRegLines.setText(_translate("MainWindow", "Строк по региону"))
        self.lblPosLines.setText(_translate("MainWindow", "Строк по статье:"))
        self.lblLineRecord.setText(_translate("MainWindow", "Записей в строке"))
        self.lblOutput.setText(_translate("MainWindow", "Записей в выдаче"))
        self.lblMediane.setText(_translate("MainWindow", "Среднее значение по строке"))
        self.lblOutputMediane.setText(_translate("MainWindow", "Среднее по выдаче"))
        self.btFile.setText(_translate("MainWindow", "Вывести в файл"))
        self.btCab.setText(_translate("MainWindow", "Личный кабинет"))
        self.lblUser.setText(_translate("MainWindow", "Не Гость"))
