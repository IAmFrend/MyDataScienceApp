from PyQt5 import QtWidgets
from log import * 
from admin_form import *
from statget import *
from db import * 
import sys
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import os
import psycopg2
import xlrd
from contextlib import closing
from PyQt5.QtWidgets import QTableWidgetItem      
from datetime import date,datetime
from os.path import expanduser
from winreg import *

sys_user_id = 0
sel_user = 0
sel_role = 0
s_dbname = 'testdb'
db_user='postgres'
db_user_password='1qaz!QAZ'
db_host='localhost'
db_port='5432'

class admin_form(QtWidgets.QWidget):
    def __init__(self):
        super(admin_form, self).__init__()
        self.ui = Ui_admin_form()
        self.ui.setupUi(self)
        self.w5 = db_connection_window(parent = self)
        self.hide()
        if (self.w5.ConnectionCheck()):
            self.w5.close()
            self.MainFill()
        self.w5.show()
        self.w5.raise_()
            
        
    def MainFill(self):
        self.w5.show()
        self.w5.raise_()
        self.login = log_form(parent = self)
        self.login.show()
        self.w1 = user_window()
        self.ui.btRoleDelete.setEnabled(False)
        self.ui.btRoleUpdate.setEnabled(False)
        self.ui.btUserDelete.setEnabled(False)
        self.ui.btUserUpdate.setEnabled(False)
        global sys_user_id
        self.UserListUpdate()
        self.RoleListUpdate()
        self.ui.lvUsers.clicked.connect(self.UserSelected)
        self.ui.lvRoles.clicked.connect(self.RoleSelected)
        self.ui.btRoleAdd.clicked.connect(self.RoleInsert)
        self.ui.btRoleUpdate.clicked.connect(self.RoleUpdate)
        self.ui.btRoleDelete.clicked.connect(self.RoleDelete)
        self.ui.btUserDelete.clicked.connect(self.UserDelete)
        self.ui.btUserAdd.clicked.connect(self.UserInsertShow)
        self.ui.btUserUpdate.clicked.connect(self.UserUpdateShow)
        self.ui.cbCurUser.currentIndexChanged.connect(self.UserRolesFill)
        self.gbUserRolesLayout = QtWidgets.QVBoxLayout()
        self.ui.gbUserRoles.setLayout(self.gbUserRolesLayout)
        self.UserRolesFill()
        self.gbLineRolesLayout = QtWidgets.QVBoxLayout()
        self.ui.gbLineRoles.setLayout(self.gbLineRolesLayout)
        self.ui.cbCurPosition.currentIndexChanged.connect(self.LineRolesFill)
        self.ui.cbCurRegion.currentIndexChanged.connect(self.LineRolesFill)
        self.LineRolesFill()
        self.LineListUpdate()
        self.ui.btUpdate.clicked.connect(self.StatisticsUpdate)

    def LineListUpdate(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.cbCurRegion.clear()
                cursor.execute('SELECT region_name FROM region ORDER BY region_id')
                regions = cursor.fetchall()
                self.ui.cbCurRegion.addItem('-Выберите регион-')
                for reg in regions:
                    self.ui.cbCurRegion.addItem(reg[0])
                self.ui.cbCurPosition.clear()
                cursor.execute('SELECT position_name FROM position ORDER BY position_id')
                positions = cursor.fetchall()
                self.ui.cbCurPosition.addItem('-Выберите статью-')
                for pos in positions:
                    self.ui.cbCurPosition.addItem(pos[0])

    def UserListUpdate(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.lvUsers.clear()
                self.ui.cbCurUser.clear()
                cursor.execute('SELECT login FROM users ORDER BY user_id')
                users_list = cursor.fetchall()
                for user in users_list:
                    self.ui.lvUsers.addItem(user[0])
                    cursor.execute('SELECT user_id FROM users WHERE login = %s',(user[0],))
                    selection = cursor.fetchone()
                    if (selection[0] != 0):
                        self.ui.cbCurUser.addItem(user[0])

    def RoleListUpdate(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.lvRoles.clear()
                cursor.execute('SELECT role_name FROM role ORDER BY role_id')
                roles_list = cursor.fetchall()
                for role in roles_list:
                    self.ui.lvRoles.addItem(role[0])
    
    def UserSelected(self):
        global sel_user
        global sys_user_id
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                if self.ui.lvUsers.selectedItems():
                    cursor.execute('SELECT user_id FROM users WHERE login = %s',(self.ui.lvUsers.selectedItems()[0].text(),))
                    sel_user = cursor.fetchone()
                    cursor.execute('SELECT COUNT (*) FROM role_user WHERE role = 1')
                    admin_count = cursor.fetchone()
                    cursor.execute('SELECT role_rule_id FROM role_user WHERE role = 1 and r_user = %s',(sel_user,))
                    user_admin = cursor.fetchone()
                    if (sel_user[0] != 0):
                        self.ui.btUserUpdate.setEnabled(True)
                        if ((admin_count[0]>1) or not (user_admin)) and (sel_user[0] != sys_user_id):
                            self.ui.btUserDelete.setEnabled(True)
                        else:
                            self.ui.btUserDelete.setEnabled(False)
                    else:
                        self.ui.btUserDelete.setEnabled(False)
                        self.ui.btUserUpdate.setEnabled(False)
                else:
                    self.ui.btUserDelete.setEnabled(False)
                    self.ui.btUserUpdate.setEnabled(False)

    
    def RoleSelected(self):
        global sel_role
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                if self.ui.lvRoles.selectedItems():
                    cursor.execute('SELECT role_id FROM role WHERE role_name = %s',(self.ui.lvRoles.selectedItems()[0].text(),))
                    sel_role = cursor.fetchone()
                    if (sel_role[0] != 0) and (sel_role[0] != 1):
                        self.ui.btRoleDelete.setEnabled(True)
                        self.ui.btRoleUpdate.setEnabled(True)
                    else:
                        self.ui.btRoleDelete.setEnabled(False)
                        self.ui.btRoleUpdate.setEnabled(False)
                else:
                    self.ui.btRoleDelete.setEnabled(False)
                    self.ui.btRoleUpdate.setEnabled(False)
    
    def RoleInsert(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                role_name, ok = QtWidgets.QInputDialog.getText(self, 'Добавление роли', 'Введите название роли:')
                if (ok and role_name):                    
                    cursor.execute('SELECT COUNT(*) FROM role WHERE role_name = %s',(role_name,))
                    r_count = cursor.fetchone()
                    if (r_count[0]>0):
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setWindowTitle("Добавление роли")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msg.setText("Этот название уже используется!")
                        msg.exec_()
                    else:
                        cursor.execute('SELECT role_id FROM role ORDER BY role_id DESC LIMIT 1')
                        nrole_id = cursor.fetchone()
                        try:
                            cursor.execute('INSERT INTO role (role_id,role_name) VALUES (%s,%s)',(nrole_id[0]+1,role_name))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                            self.RoleListUpdate()
                            self.UserRolesFill()
                            self.LineRolesFill()
    
    def RoleUpdate(self):
        global sel_role
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                role_name, ok = QtWidgets.QInputDialog.getText(self, 'Изменение роли', 'Введите новое название роли ' + self.ui.lvRoles.selectedItems()[0].text()+' :')
                if (ok and role_name):                    
                    cursor.execute('SELECT COUNT(*) FROM role WHERE role_name = %s and not role_id = %s',(role_name,sel_role))
                    r_count = cursor.fetchone()
                    if (r_count[0]>0):
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setWindowTitle("Изменение роли")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msg.setText("Этот название уже используется!")
                        msg.exec_()
                    else:
                        try:
                            cursor.execute('UPDATE role SET role_name = %s WHERE role_id = %s',(role_name,sel_role))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                            self.RoleListUpdate()
                            self.UserRolesFill()
                            self.LineRolesFill()

    def RoleDelete(self):
        global sel_role
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Удаление роли")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                msg.setText("Вы действительно хотите удалить эту роль?")
                retval = msg.exec_()
                if (retval == QtWidgets.QMessageBox.Ok):
                    try:
                        cursor.execute('DELETE FROM role WHERE role_id = %s',(sel_role,))
                    except psycopg2.DatabaseError as err:
                        print("Error:",err)
                    else:
                        conn.commit()
                        self.RoleListUpdate()
                        self.UserRolesFill()
                        self.LineRolesFill()

    def UserDelete(self):
        global sel_user
        global sys_user_id
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Удаление пользователя")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                msg.setText("Вы действительно хотите удалить этого пользователя?")
                retval = msg.exec_()
                if (retval == QtWidgets.QMessageBox.Ok):
                    try:
                        cursor.execute('DELETE FROM users WHERE user_id = %s',(sel_user,))
                    except psycopg2.DatabaseError as err:
                        print("Error:",err)
                    else:
                        conn.commit()
                        self.UserListUpdate()
    
    def UserInsertShow(self):
        self.w1.show()
        try:
            self.w1.ui.btEnter.clicked.disconnect()
        except Exception:
            pass
        self.w1.ui.btEnter.clicked.connect(self.UserInsert)

    def UserUpdateShow(self):
        self.w1.show()
        try:
            self.w1.ui.btEnter.clicked.disconnect()
        except Exception:
            pass
        self.w1.ui.btEnter.clicked.connect(self.UserUpdate)
    
    def UserInsert(self):
        global sys_user_id
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Регистрация")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                slogin = self.w1.ui.tbLogin.text()
                spassword = self.w1.ui.tbPassword.text()
                sconfirm = self.w1.ui.tbConfirm.text()
                if not slogin:
                    msg.setText("Введите логин")
                    msg.exec_()
                elif not spassword:
                    msg.setText("Введите пароль")
                    msg.exec_()
                elif not sconfirm:
                    msg.setText("Подтвердите пароль")
                    msg.exec_()
                elif sconfirm != spassword:
                    msg.setText("Пароли не совпадают")
                    msg.exec_()
                else:
                    cursor.execute('SELECT user_id FROM users WHERE login = %s',(slogin,))
                    suser_id = cursor.fetchone()
                    if suser_id:
                        msg.setText("Этот логин уже используется!")
                        msg.exec_()
                    else:
                        try:
                            cursor.execute('INSERT INTO users(login,password) VALUES (%s,%s)',(slogin,spassword))
                            cursor.execute('SELECT user_id FROM users WHERE login = %s and password = %s',(slogin,spassword))
                            nuser_id = cursor.fetchone()
                            cursor.execute('INSERT INTO role_user(role,r_user) VALUES (%s,%s)',('0',nuser_id))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                            self.UserListUpdate()
                            self.w1.close()
    
    def UserUpdate(self):
        global sel_user
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Изменение данных")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                slogin = self.w1.ui.tbLogin.text()
                spassword = self.w1.ui.tbPassword.text()
                sconfirm = self.w1.ui.tbConfirm.text()
                if not slogin:
                    msg.setText("Введите логин")
                    msg.exec_()
                elif not spassword:
                    msg.setText("Введите пароль")
                    msg.exec_()
                elif not sconfirm:
                    msg.setText("Подтвердите пароль")
                    msg.exec_()
                elif sconfirm != spassword:
                    msg.setText("Пароли не совпадают")
                    msg.exec_()
                else:
                    cursor.execute('SELECT user_id FROM users WHERE login = %s and not user_id = %s',(slogin,sel_user))
                    suser_id = cursor.fetchone()
                    if suser_id:
                        msg.setText("Этот логин уже используется!")
                        msg.exec_()
                    else:
                        try:
                            cursor.execute('UPDATE users SET login = %s,password = %s WHERE user_id = %s',(slogin,spassword,sel_user))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                            self.UserListUpdate()
                            self.w1.close()
    
    def UserRolesFill(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT user_id FROM users WHERE login = %s',(self.ui.cbCurUser.currentText(),))
                suser_id = cursor.fetchone()
                cursor.execute('SELECT role_id,role_name FROM role')
                roles = cursor.fetchall()
                cursor.execute('SELECT role FROM role_user WHERE r_user = %s',(suser_id,))
                suser_roles = cursor.fetchall()
                user_roles = []
                for r in suser_roles:
                    user_roles.append(r[0])
                for i in reversed(range(self.gbUserRolesLayout.count())): 
                    self.gbUserRolesLayout.itemAt(i).widget().setParent(None)
                for role in roles:
                    rb = QtWidgets.QCheckBox(role[1])
                    rb.role_id = role[0]
                    if (role[0] == 0):
                        rb.setEnabled(False)
                    if (role[0] in user_roles):
                        rb.setChecked(True)
                    rb.stateChanged.connect(self.ChangeUserRole)
                    self.gbUserRolesLayout.addWidget(rb)
    
    def ChangeUserRole(self, state):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                sender = self.sender()
                ch_role = sender.role_id
                cursor.execute('SELECT user_id FROM users WHERE login = %s',(self.ui.cbCurUser.currentText(),))
                suser_id = cursor.fetchone()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Изменение пользовательских ролей")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                try:
                    if state == QtCore.Qt.Checked:
                        cursor.execute('insert into role_user (role,r_user) values (%s,%s)',(ch_role,suser_id))
                    else:
                        cursor.execute('SELECT COUNT (*) FROM role_user WHERE role = 1')
                        admin_count = cursor.fetchone()
                        if ((admin_count[0]>1) or (ch_role != 1)):
                            if ((ch_role != 1) or (sys_user_id != suser_id)):
                                cursor.execute('delete from role_user where role = %s and r_user = %s',(ch_role,suser_id)) 
                            else:
                                msg.setText("Нельзя снять должность админа с текущего пользователя!")
                                msg.exec_()   
                        else:
                            msg.setText("Нельзя снять должность админа с последнего админа!")
                            msg.exec_()
                except psycopg2.DatabaseError as err:
                    print("Error:",err)
                else:
                    conn.commit()
                self.UserRolesFill()

    def LineRolesFill(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(self.ui.cbCurRegion.currentText(),))
                region_id = cursor.fetchone()
                cursor.execute('SELECT position_id FROM position WHERE position_name = %s',(self.ui.cbCurPosition.currentText(),))
                position_id = cursor.fetchone()
                cursor.execute('SELECT line_id FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                line_id = cursor.fetchone()
                cursor.execute('SELECT role_id,role_name FROM role')
                roles = cursor.fetchall()
                for i in reversed(range(self.gbLineRolesLayout.count())): 
                    self.gbLineRolesLayout.itemAt(i).widget().setParent(None)
                if line_id:
                    cursor.execute('SELECT role FROM role_rule WHERE line = %s',(line_id,))
                    sline_roles = cursor.fetchall()
                    line_roles = []
                    for r in sline_roles:
                        line_roles.append(r[0])
                    for role in roles:
                        rb = QtWidgets.QCheckBox(role[1])
                        rb.role_id = role[0]
                        if (role[0] == 1):
                            rb.setEnabled(False)
                        if (role[0] in line_roles):
                            rb.setChecked(True)
                        rb.stateChanged.connect(self.ChangeLineRole)
                        self.gbLineRolesLayout.addWidget(rb)
                else:
                    ln = QtWidgets.QLabel('Линия отсутствует')
                    self.gbLineRolesLayout.addWidget(ln)

    def ChangeLineRole(self, state):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                sender = self.sender()
                ch_role = sender.role_id
                cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(self.ui.cbCurRegion.currentText(),))
                region_id = cursor.fetchone()
                cursor.execute('SELECT position_id FROM position WHERE position_name = %s',(self.ui.cbCurPosition.currentText(),))
                position_id = cursor.fetchone()
                cursor.execute('SELECT line_id FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                line_id = cursor.fetchone()
                try:
                    if state == QtCore.Qt.Checked:
                        cursor.execute('insert into role_rule (role,line) values (%s,%s)',(ch_role,line_id))
                    else:
                        cursor.execute('delete from role_rule where role = %s and line = %s',(ch_role,line_id)) 
                except psycopg2.DatabaseError as err:
                    print("Error:",err)
                else:
                    conn.commit()
                self.LineRolesFill()

    def StatisticsUpdate(self):
        dtcon = statisticsGet_Debet()
        lncon = statisticsGet_Loans()
        nlcon = statisticsGet_nalog()
        if dtcon or lncon or nlcon:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Загрузка статистики")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setText("Невозможно подключиться к интернету")
            msg.exec_()
        self.LineListUpdate()
 
class log_form(QtWidgets.QWidget):
    def __init__(self, parent):
        super(log_form, self).__init__()
        self.ui = Ui_Log()
        self.ui.setupUi(self)
        self.parent = parent
        self.setWindowTitle('Авторизация')
        self.ui.lblConfirm.hide()
        self.ui.tbConfirm.hide()
        self.ui.btCancel.hide()
        self.ui.tbConfirm.clear()
        self.ui.tbLogin.clear()
        self.ui.tbPassword.clear()
        self.ui.btEnter.clicked.connect(self.Login)

    def Login(self):
        global sys_user_id
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Вход в учётную запись")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                slogin = self.ui.tbLogin.text()
                spassword = self.ui.tbPassword.text()
                if not slogin:
                    msg.setText("Введите логин")
                    msg.exec_()
                elif not spassword:
                    msg.setText("Введите пароль")
                    msg.exec_()
                else:
                    cursor.execute('SELECT user_id FROM users WHERE login = %s and password = %s',(slogin,spassword))
                    suser_id = cursor.fetchone()
                    if suser_id:
                        cursor.execute('SELECT COUNT(*) FROM role_user WHERE r_user = %s and role = 1',(suser_id,))
                        adm_con = cursor.fetchone()
                        if (adm_con[0]>0):
                            sys_user_id = suser_id
                            self.parent.show()
                            self.parent.raise_()
                            self.close()
                        else:
                            msg.setText("Пользователь не является администратором")
                            msg.exec_()
                    else:
                        msg.setText("Пользователь не найден")
                        msg.exec_()


class user_window(QtWidgets.QWidget):
    def __init__(self):
        super(user_window, self).__init__()
        self.ui = Ui_Log()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui.btCancel.clicked.connect(self.close)

class db_connection_window(QtWidgets.QWidget):
    def __init__(self,parent):
        super(db_connection_window, self).__init__()
        self.ui = Ui_db_select()
        self.ui.setupUi(self)
        self.parent = parent
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        self.cls = True
        reg = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\\", 0, KEY_READ  | KEY_WOW64_64KEY)
        try:
            subKey = OpenKey(reg, r"MyDataScienceApp\\", 0, KEY_READ  | KEY_WRITE)
        except:
            subKey = CreateKey(reg, r"MyDataScienceApp\\")
            subKey = OpenKey(reg, r"MyDataScienceApp\\", 0, KEY_READ  | KEY_WRITE)
        try:
            s_dbname,regtype = QueryValueEx(subKey,'s_dbname')
        except:
            SetValueEx(subKey,'s_dbname',0,REG_SZ,None)
            s_dbname,regtype = QueryValueEx(subKey,'s_dbname')
        if (s_dbname != None):
            self.ui.tbDBName.setText(s_dbname)
        try:
            db_user,regtype = QueryValueEx(subKey,'db_user')
        except:
            SetValueEx(subKey,'db_user',0,REG_SZ,None)
            db_user,regtype = QueryValueEx(subKey,'db_user')
        if (db_user != None):
            self.ui.tbDBUser.setText(db_user)
        try:
            db_user_password,regtype = QueryValueEx(subKey,'db_user_password')
        except:
            SetValueEx(subKey,'db_user_password',0,REG_SZ,None)
            db_user_password,regtype = QueryValueEx(subKey,'db_user_password')
        if (db_user_password != None):
            self.ui.tbDBUserPassword.setText(db_user_password)
        try:
            db_host,regtype = QueryValueEx(subKey,'db_host')
        except:
            SetValueEx(subKey,'db_host',0,REG_SZ,None)
            db_host,regtype = QueryValueEx(subKey,'db_host')
        if (db_host != None):
            self.ui.tbDBHost.setText(db_host)
        try:
            db_port,regtype = QueryValueEx(subKey,'db_port')
        except:
            SetValueEx(subKey,'db_port',0,REG_SZ,None)
            db_port,regtype = QueryValueEx(subKey,'db_port')
        if (db_port != None):
            self.ui.tbDBPort.setText(db_port)
        self.ui.btCheck.clicked.connect(self.ConnectionCheck)
        self.ui.btEnter.setEnabled(False)
        self.ui.btEnter.clicked.connect(self.EnterClick)
            

    def closeEvent(self, e):
        if self.cls:
            self.parent.close()
        e.accept()
    
    def ConnectionCheck(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Проверка подключения")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        try:
            conn = closing(psycopg2.connect(dbname=self.ui.tbDBName.text(), user=self.ui.tbDBUser.text(), password=self.ui.tbDBUserPassword.text(), host=self.ui.tbDBHost.text(), port = self.ui.tbDBPort.text()))
        except:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Подключение не установлено")
            msg.exec_()
            self.ui.btEnter.setEnabled(False)
            return False
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Подключение установлено")
            msg.exec_()
            s_dbname=self.ui.tbDBName.text()
            db_user=self.ui.tbDBUser.text()
            db_user_password=self.ui.tbDBUserPassword.text()
            db_host=self.ui.tbDBHost.text()
            db_port = self.ui.tbDBPort.text()
            self.ui.btEnter.setEnabled(True)
            return True
    
    def EnterClick(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        reg = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\\", 0, KEY_READ  | KEY_WOW64_64KEY)
        subKey = OpenKey(reg, r"MyDataScienceApp\\", 0, KEY_READ  | KEY_WRITE)
        SetValueEx(subKey,'s_dbname',0,REG_SZ,s_dbname)
        SetValueEx(subKey,'db_user',0,REG_SZ,db_user)
        SetValueEx(subKey,'db_user_password',0,REG_SZ,db_user_password)
        SetValueEx(subKey,'db_host',0,REG_SZ,db_host)
        SetValueEx(subKey,'db_port',0,REG_SZ,db_port)
        self.cls = False
        self.parent.MainFill()
        self.close()


app = QtWidgets.QApplication([])
application = admin_form()
application.show()
try:
    application.w5.raise_()
except:
    pass
application.close()
sys.exit(app.exec())