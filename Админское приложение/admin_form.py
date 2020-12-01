# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_form(object):
    def setupUi(self, admin_form):
        admin_form.setObjectName("admin_form")
        admin_form.resize(625, 739)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        admin_form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(admin_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.laRolesAndUsers = QtWidgets.QHBoxLayout()
        self.laRolesAndUsers.setObjectName("laRolesAndUsers")
        self.laRoles = QtWidgets.QVBoxLayout()
        self.laRoles.setObjectName("laRoles")
        self.lblRoles = QtWidgets.QLabel(admin_form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblRoles.setFont(font)
        self.lblRoles.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRoles.setObjectName("lblRoles")
        self.laRoles.addWidget(self.lblRoles)
        self.lvRoles = QtWidgets.QListWidget(admin_form)
        self.lvRoles.setResizeMode(QtWidgets.QListView.Adjust)
        self.lvRoles.setObjectName("lvRoles")
        self.laRoles.addWidget(self.lvRoles)
        self.laRoleButtons = QtWidgets.QHBoxLayout()
        self.laRoleButtons.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.laRoleButtons.setObjectName("laRoleButtons")
        self.btRoleAdd = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btRoleAdd.sizePolicy().hasHeightForWidth())
        self.btRoleAdd.setSizePolicy(sizePolicy)
        self.btRoleAdd.setObjectName("btRoleAdd")
        self.laRoleButtons.addWidget(self.btRoleAdd)
        self.btRoleUpdate = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btRoleUpdate.sizePolicy().hasHeightForWidth())
        self.btRoleUpdate.setSizePolicy(sizePolicy)
        self.btRoleUpdate.setObjectName("btRoleUpdate")
        self.laRoleButtons.addWidget(self.btRoleUpdate)
        self.btRoleDelete = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btRoleDelete.sizePolicy().hasHeightForWidth())
        self.btRoleDelete.setSizePolicy(sizePolicy)
        self.btRoleDelete.setObjectName("btRoleDelete")
        self.laRoleButtons.addWidget(self.btRoleDelete)
        self.laRoles.addLayout(self.laRoleButtons)
        self.laRolesAndUsers.addLayout(self.laRoles)
        self.laUsers = QtWidgets.QVBoxLayout()
        self.laUsers.setObjectName("laUsers")
        self.lblUsers = QtWidgets.QLabel(admin_form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblUsers.setFont(font)
        self.lblUsers.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUsers.setObjectName("lblUsers")
        self.laUsers.addWidget(self.lblUsers)
        self.lvUsers = QtWidgets.QListWidget(admin_form)
        self.lvUsers.setResizeMode(QtWidgets.QListView.Adjust)
        self.lvUsers.setObjectName("lvUsers")
        self.laUsers.addWidget(self.lvUsers)
        self.laUserButtons = QtWidgets.QHBoxLayout()
        self.laUserButtons.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.laUserButtons.setObjectName("laUserButtons")
        self.btUserAdd = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btUserAdd.sizePolicy().hasHeightForWidth())
        self.btUserAdd.setSizePolicy(sizePolicy)
        self.btUserAdd.setObjectName("btUserAdd")
        self.laUserButtons.addWidget(self.btUserAdd)
        self.btUserUpdate = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btUserUpdate.sizePolicy().hasHeightForWidth())
        self.btUserUpdate.setSizePolicy(sizePolicy)
        self.btUserUpdate.setObjectName("btUserUpdate")
        self.laUserButtons.addWidget(self.btUserUpdate)
        self.btUserDelete = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btUserDelete.sizePolicy().hasHeightForWidth())
        self.btUserDelete.setSizePolicy(sizePolicy)
        self.btUserDelete.setObjectName("btUserDelete")
        self.laUserButtons.addWidget(self.btUserDelete)
        self.laUsers.addLayout(self.laUserButtons)
        self.laRolesAndUsers.addLayout(self.laUsers)
        self.verticalLayout.addLayout(self.laRolesAndUsers)
        self.laRoleUser = QtWidgets.QVBoxLayout()
        self.laRoleUser.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.laRoleUser.setObjectName("laRoleUser")
        self.laCurUser = QtWidgets.QHBoxLayout()
        self.laCurUser.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.laCurUser.setObjectName("laCurUser")
        self.lblCurUser = QtWidgets.QLabel(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCurUser.sizePolicy().hasHeightForWidth())
        self.lblCurUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblCurUser.setFont(font)
        self.lblCurUser.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblCurUser.setObjectName("lblCurUser")
        self.laCurUser.addWidget(self.lblCurUser)
        self.cbCurUser = QtWidgets.QComboBox(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCurUser.sizePolicy().hasHeightForWidth())
        self.cbCurUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbCurUser.setFont(font)
        self.cbCurUser.setObjectName("cbCurUser")
        self.laCurUser.addWidget(self.cbCurUser)
        self.laRoleUser.addLayout(self.laCurUser)
        self.gbUserRoles = QtWidgets.QGroupBox(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbUserRoles.sizePolicy().hasHeightForWidth())
        self.gbUserRoles.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbUserRoles.setFont(font)
        self.gbUserRoles.setObjectName("gbUserRoles")
        self.laRoleUser.addWidget(self.gbUserRoles)
        self.verticalLayout.addLayout(self.laRoleUser)
        self.laLineRules = QtWidgets.QVBoxLayout()
        self.laLineRules.setObjectName("laLineRules")
        self.laCurRegion = QtWidgets.QHBoxLayout()
        self.laCurRegion.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.laCurRegion.setObjectName("laCurRegion")
        self.lblCurRegion = QtWidgets.QLabel(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCurRegion.sizePolicy().hasHeightForWidth())
        self.lblCurRegion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblCurRegion.setFont(font)
        self.lblCurRegion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblCurRegion.setObjectName("lblCurRegion")
        self.laCurRegion.addWidget(self.lblCurRegion)
        self.cbCurRegion = QtWidgets.QComboBox(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCurRegion.sizePolicy().hasHeightForWidth())
        self.cbCurRegion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbCurRegion.setFont(font)
        self.cbCurRegion.setObjectName("cbCurRegion")
        self.laCurRegion.addWidget(self.cbCurRegion)
        self.laLineRules.addLayout(self.laCurRegion)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblCurPosition = QtWidgets.QLabel(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCurPosition.sizePolicy().hasHeightForWidth())
        self.lblCurPosition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblCurPosition.setFont(font)
        self.lblCurPosition.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblCurPosition.setObjectName("lblCurPosition")
        self.horizontalLayout_6.addWidget(self.lblCurPosition)
        self.cbCurPosition = QtWidgets.QComboBox(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCurPosition.sizePolicy().hasHeightForWidth())
        self.cbCurPosition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbCurPosition.setFont(font)
        self.cbCurPosition.setObjectName("cbCurPosition")
        self.horizontalLayout_6.addWidget(self.cbCurPosition)
        self.laLineRules.addLayout(self.horizontalLayout_6)
        self.gbLineRoles = QtWidgets.QGroupBox(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbLineRoles.sizePolicy().hasHeightForWidth())
        self.gbLineRoles.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbLineRoles.setFont(font)
        self.gbLineRoles.setObjectName("gbLineRoles")
        self.laLineRules.addWidget(self.gbLineRoles)
        self.verticalLayout.addLayout(self.laLineRules)
        self.btUpdate = QtWidgets.QPushButton(admin_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btUpdate.sizePolicy().hasHeightForWidth())
        self.btUpdate.setSizePolicy(sizePolicy)
        self.btUpdate.setObjectName("btUpdate")
        self.verticalLayout.addWidget(self.btUpdate)

        self.retranslateUi(admin_form)
        QtCore.QMetaObject.connectSlotsByName(admin_form)

    def retranslateUi(self, admin_form):
        _translate = QtCore.QCoreApplication.translate
        admin_form.setWindowTitle(_translate("admin_form", "Окно администратора"))
        self.lblRoles.setText(_translate("admin_form", "Роли"))
        self.btRoleAdd.setText(_translate("admin_form", "Добавить"))
        self.btRoleUpdate.setText(_translate("admin_form", "Изменить"))
        self.btRoleDelete.setText(_translate("admin_form", "Удалить"))
        self.lblUsers.setText(_translate("admin_form", "Пользователи"))
        self.btUserAdd.setText(_translate("admin_form", "Добавить"))
        self.btUserUpdate.setText(_translate("admin_form", "Изменить"))
        self.btUserDelete.setText(_translate("admin_form", "Удалить"))
        self.lblCurUser.setText(_translate("admin_form", "Пользователь:"))
        self.gbUserRoles.setTitle(_translate("admin_form", "Роли пользователя"))
        self.lblCurRegion.setText(_translate("admin_form", "Регион:"))
        self.lblCurPosition.setText(_translate("admin_form", "Статья:"))
        self.gbLineRoles.setTitle(_translate("admin_form", "Роли, которым доступна линия"))
        self.btUpdate.setText(_translate("admin_form", "Обновить статистику"))
