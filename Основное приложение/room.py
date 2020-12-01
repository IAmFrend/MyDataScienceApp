# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_self_room(object):
    def setupUi(self, self_room):
        self_room.setObjectName("self_room")
        self_room.resize(400, 171)
        self.verticalLayout = QtWidgets.QVBoxLayout(self_room)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblUserName = QtWidgets.QLabel(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUserName.sizePolicy().hasHeightForWidth())
        self.lblUserName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblUserName.setFont(font)
        self.lblUserName.setObjectName("lblUserName")
        self.horizontalLayout.addWidget(self.lblUserName)
        self.lblUser = QtWidgets.QLabel(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUser.sizePolicy().hasHeightForWidth())
        self.lblUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblUser.setFont(font)
        self.lblUser.setFrameShape(QtWidgets.QFrame.Box)
        self.lblUser.setObjectName("lblUser")
        self.horizontalLayout.addWidget(self.lblUser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblUserRoles = QtWidgets.QLabel(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUserRoles.sizePolicy().hasHeightForWidth())
        self.lblUserRoles.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblUserRoles.setFont(font)
        self.lblUserRoles.setObjectName("lblUserRoles")
        self.horizontalLayout_2.addWidget(self.lblUserRoles)
        self.lblUser_2 = QtWidgets.QLabel(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUser_2.sizePolicy().hasHeightForWidth())
        self.lblUser_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblUser_2.setFont(font)
        self.lblUser_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lblUser_2.setWordWrap(True)
        self.lblUser_2.setObjectName("lblUser_2")
        self.horizontalLayout_2.addWidget(self.lblUser_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btEnterExit = QtWidgets.QPushButton(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btEnterExit.sizePolicy().hasHeightForWidth())
        self.btEnterExit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btEnterExit.setFont(font)
        self.btEnterExit.setObjectName("btEnterExit")
        self.horizontalLayout_3.addWidget(self.btEnterExit)
        self.btRegChange = QtWidgets.QPushButton(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btRegChange.sizePolicy().hasHeightForWidth())
        self.btRegChange.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btRegChange.setFont(font)
        self.btRegChange.setObjectName("btRegChange")
        self.horizontalLayout_3.addWidget(self.btRegChange)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.btRoomExit = QtWidgets.QPushButton(self_room)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btRoomExit.sizePolicy().hasHeightForWidth())
        self.btRoomExit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btRoomExit.setFont(font)
        self.btRoomExit.setObjectName("btRoomExit")
        self.verticalLayout.addWidget(self.btRoomExit)

        self.retranslateUi(self_room)
        QtCore.QMetaObject.connectSlotsByName(self_room)

    def retranslateUi(self, self_room):
        _translate = QtCore.QCoreApplication.translate
        self_room.setWindowTitle(_translate("self_room", "Личный кабинет"))
        self.lblUserName.setText(_translate("self_room", "Имя пользователя:"))
        self.lblUser.setText(_translate("self_room", " "))
        self.lblUserRoles.setText(_translate("self_room", "Роли:"))
        self.lblUser_2.setText(_translate("self_room", " "))
        self.btEnterExit.setText(_translate("self_room", "Войти"))
        self.btRegChange.setText(_translate("self_room", "Зарегестрироваться"))
        self.btRoomExit.setText(_translate("self_room", "Покинуть личный кабинет"))
