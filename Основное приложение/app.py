from PyQt5 import QtWidgets
from main import *  
from save import *   
from room import *   
from log import * 
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
sys_user_roles = []
s_dbname = 'testdb'
db_user='postgres'
db_user_password='1qaz!QAZ'
db_host='localhost'
db_port='5432'
 
class main_vindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_vindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global sys_user_id
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        self.w5 = db_connection_window(parent = self)
        self.hide()
        if (self.w5.ConnectionCheck()):
            self.raise_()
            self.w5.close()
            self.MainFill()
        self.w5.show()
        self.w5.raise_()

    def MainFill(self):
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
                with conn.cursor() as cursor:
                    # Работа с регионами
                    self.ui.tbRegion.textChanged.connect(self.tbRegionTextChanged)
                    self.tbRegionTextChanged()
                    self.ui.cbRegion.currentIndexChanged.connect(self.LineChanged)
                    # Работа со статьями
                    self.ui.tbPosition.textChanged.connect(self.tbPositionTextChanged)
                    self.tbPositionTextChanged()
                    self.ui.cbPosition.currentIndexChanged.connect(self.LineChanged)
                    # Работа с таблицей
                    self.ui.tbLine.setSortingEnabled(True)
                    cursor.execute('SELECT COUNT (*) FROM record')
                    rccount = cursor.fetchone()
                    self.ui.lblAllRecords.setText('Всего записей: '+str(rccount[0]))
                    # Работа с датами
                    self.ui.cbDate.addItem('Нет фильтра')
                    self.ui.cbDate.addItem('Больше')
                    self.ui.cbDate.addItem('Не меньше')
                    self.ui.cbDate.addItem('Равно')
                    self.ui.cbDate.addItem('Не больше')
                    self.ui.cbDate.addItem('Меньше')
                    self.ui.cbDate.addItem('Не равно')
                    self.ui.cbDate.currentIndexChanged.connect(self.LineChanged)
                    self.ui.dtDate.dateChanged.connect(self.LineChanged)
                    # Работа с числами
                    self.ui.cbValue.addItem('Нет фильтра')
                    self.ui.cbValue.addItem('Больше')
                    self.ui.cbValue.addItem('Не меньше')
                    self.ui.cbValue.addItem('Равно')
                    self.ui.cbValue.addItem('Не больше')
                    self.ui.cbValue.addItem('Меньше')
                    self.ui.cbValue.addItem('Не равно')
                    self.ui.cbValue.currentIndexChanged.connect(self.LineChanged)
                    self.ui.spValue.textChanged.connect(self.LineChanged)
                    self.ui.btFile.clicked.connect(self.SaveWindowShow)
                    # Работа с ролями
                    self.ui.btCab.clicked.connect(self.RoomWindowShow)
                    
                    self.w2 = save_window()
                    self.w2.ui.btCancel.clicked.connect(self.w2.close)
                    self.w2.ui.cbOType.currentIndexChanged.connect(self.w2.TypeChanged)
                    self.w2.ui.btSave.clicked.connect(self.w2.Save)
                    
                    self.w3 = room_window(parent = self)
                    self.w3.RolesSet()
                    self.w3.ButtonChange()
                    self.w3.ui.btRoomExit.clicked.connect(self.w3.close)

    def closeEvent(self, e):
        try:
            self.w2.close()
        except Exception:
            pass
        try:
            self.w3.close()
        except Exception:
            pass
        try:
            self.w5.close()
        except Exception:
            pass
        e.accept()

    def SaveWindowShow(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.w2.show()
                self.w2.raise_()
    
    def RoomWindowShow(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.w3.show()
                self.w3.raise_()

    def LineChanged(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.lblLineRecord.setText('Записей в строке: ')
                self.ui.lblMediane.setText('Среднее: ')
                self.ui.lblOutput.setText('Записей в выдаче: ')
                self.ui.lblOutputMediane.setText('Среднее по выдаче: ')
                self.ui.lblRegLines.setText('Строк по региону: ')
                self.ui.lblPosLines.setText('Строк по статье: ')
                global sys_user_id
                self.ui.tbLine.clear()
                self.ui.tbLine.setRowCount(0)
                cursor.execute('SELECT COUNT (*) FROM record')
                rccount = cursor.fetchone()
                cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(self.ui.cbRegion.currentText(),))
                region_id = cursor.fetchone()
                cursor.execute('SELECT position_id FROM position WHERE position_name = %s',(self.ui.cbPosition.currentText(),))
                position_id = cursor.fetchone()
                cursor.execute('SELECT COUNT (*) FROM line WHERE line_region = %s',(region_id,))
                creglines = cursor.fetchone()
                self.ui.lblRegLines.setText('Строк по региону: '+str(creglines[0]))    
                cursor.execute('SELECT COUNT (*) FROM line WHERE line_position = %s',(position_id,))
                cposlines = cursor.fetchone()
                self.ui.lblPosLines.setText('Строк по статье: '+str(cposlines[0]))    
                line_id = None
                rules = 0
                if (region_id and position_id):
                    cursor.execute('SELECT line_id FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                    line_id = cursor.fetchone()
                    for role in sys_user_roles:
                        cursor.execute('SELECT COUNT(*) FROM role_rule WHERE line = %s and role = %s',(line_id,role))
                        rule = cursor.fetchone()
                        rules += rule[0]
                if line_id and (rules>0):
                    self.ui.tbLine.setColumnCount(2)
                    cursor.execute('SELECT unit FROM position WHERE position_id = %s',(position_id,))
                    position_unit = cursor.fetchone()
                    self.ui.tbLine.setHorizontalHeaderLabels(('Дата',position_unit[0]))
                    cursor.execute('SELECT date,value FROM record WHERE on_line = %s',(line_id,))
                    values = cursor.fetchall()
                    row = 0
                    mediane = 0
                    omediane = 0
                    dif = {'Равно':'==','Не равно':'!=','Больше':'>','Не меньше':'>=','Не больше':'<=','Меньше':'<'}
                    for val in values:
                        mediane+=val[1]
                        tval = str(val[0])
                        tdate = datetime.strptime(tval, "%d.%m.%Y")
                        sub = tdate.date() - self.ui.dtDate.date().toPyDate()
                        if (not self.ui.cbDate.currentText() in dif):
                            if (not self.ui.cbValue.currentText() in dif):
                                self.ui.tbLine.setRowCount(row+1)
                                dt = QTableWidgetItem(str(val[0]))
                                dt.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                vl = QTableWidgetItem(str(val[1]))
                                vl.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                self.ui.tbLine.setItem(row,0,dt)
                                self.ui.tbLine.setItem(row,1,vl)
                                row+=1
                                omediane+=val[1]
                            elif (eval(str(val[1])+dif[self.ui.cbValue.currentText()]+str(self.ui.spValue.value()))):
                                self.ui.tbLine.setRowCount(row+1)
                                dt = QTableWidgetItem(str(val[0]))
                                dt.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                vl = QTableWidgetItem(str(val[1]))
                                vl.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                self.ui.tbLine.setItem(row,0,dt)
                                self.ui.tbLine.setItem(row,1,vl)
                                row+=1 
                                omediane+=val[1]
                        elif (eval(str(sub.days)+dif[self.ui.cbDate.currentText()]+'0')):
                            if (not self.ui.cbValue.currentText() in dif):
                                self.ui.tbLine.setRowCount(row+1)
                                dt = QTableWidgetItem(str(val[0]))
                                dt.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                vl = QTableWidgetItem(str(val[1]))
                                vl.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                self.ui.tbLine.setItem(row,0,dt)
                                self.ui.tbLine.setItem(row,1,vl)
                                row+=1
                                omediane+=val[1]
                            elif (eval(str(val[1])+dif[self.ui.cbValue.currentText()]+str(self.ui.spValue.value()))):
                                self.ui.tbLine.setRowCount(row+1)
                                dt = QTableWidgetItem(str(val[0]))
                                dt.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                vl = QTableWidgetItem(str(val[1]))
                                vl.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                self.ui.tbLine.setItem(row,0,dt)
                                self.ui.tbLine.setItem(row,1,vl)
                                row+=1 
                                omediane+=val[1]
                    cursor.execute('SELECT COUNT(*) FROM record WHERE on_line = %s',(line_id,))
                    lcount = cursor.fetchone()
                    self.ui.lblLineRecord.setText('Записей в строке: '+str(lcount[0]))
                    if lcount[0] != 0:
                        self.ui.lblMediane.setText('Среднее: '+str(mediane/lcount[0]))
                    else:
                        self.ui.lblMediane.setText('Среднее: 0')
                    self.ui.lblOutput.setText('Записей в выдаче: '+str(row))
                    if row !=0:
                        self.ui.lblOutputMediane.setText('Среднее по выдаче: '+str(omediane/row))
                    else:
                        self.ui.lblOutputMediane.setText('Среднее по выдаче: 0')


    def tbRegionTextChanged(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.cbRegion.clear()
                cursor.execute('SELECT region_name FROM region WHERE region_name like %s ORDER BY region_id',('%'+self.ui.tbRegion.text()+'%',))
                regions = cursor.fetchall()
                self.ui.cbRegion.addItem('-Выберите регион-')
                for reg in regions:
                    self.ui.cbRegion.addItem(reg[0])

    def tbPositionTextChanged(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.cbPosition.clear()
                cursor.execute('SELECT position_name FROM position WHERE position_name like %s or unit like %s ORDER BY position_id',('%'+self.ui.tbPosition.text()+'%','%'+self.ui.tbPosition.text()+'%'))
                positions = cursor.fetchall()
                self.ui.cbPosition.addItem('-Выберите статью-')
                for pos in positions:
                    self.ui.cbPosition.addItem(pos[0])

class save_window(QtWidgets.QWidget):
    def __init__(self):
        super(save_window, self).__init__()
        self.ui = Ui_SaveDialog()
        self.ui.setupUi(self)
        # Работа с боксами
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                self.ui.cbOType.addItem('Регион')
                self.ui.cbOType.addItem('Статья')
                cursor.execute('SELECT region_name FROM region ORDER BY region_id')
                self.regions = cursor.fetchall()
                cursor.execute('SELECT position_name FROM position ORDER BY position_id')
                self.positions = cursor.fetchall()
                self.TypeChanged()

    def TypeChanged(self):
        self.ui.cbOutput.clear()
        if (self.ui.cbOType.currentIndex() == 0):
            self.ui.lblOutput.setText('Регион')
            self.ui.cbOutput.addItem('-Выберите регион-')
            for rg in self.regions:
                self.ui.cbOutput.addItem(rg[0])
        else:
            self.ui.lblOutput.setText('Статья')
            self.ui.cbOutput.addItem('-Выберите статью-')
            for ps in self.positions:
                self.ui.cbOutput.addItem(ps[0])
        self.ui.cbOutput.setCurrentIndex(0)
    
    def Save(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                if (self.ui.cbOutput.currentIndex() != 0):
                    save_dlg = QtWidgets.QFileDialog()
                    save_dlg.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
                    save_dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
                    save_dir = save_dlg.getSaveFileName(self,'Выберите папку для сохранения',expanduser("~"))
                    if (save_dir[0] != ''):
                        if (save_dir[0][-5:] == '.xlsx'):
                            file_name = save_dir[0]
                        else:
                            file_name = save_dir[0]+'.xlsx'
                        # Получение данных
                        Frame = pd.DataFrame()
                        if (self.ui.cbOType.currentIndex() == 0):
                            cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(self.ui.cbOutput.currentText(),))
                            region_id = cursor.fetchone()
                            cursor.execute('SELECT line_id FROM line WHERE line_region = %s',(region_id,))
                            lines = cursor.fetchall()
                            positions = []
                            iter = 0
                            for ln in lines:
                                cursor.execute('SELECT line_position FROM line WHERE line_id = %s',(ln,))
                                position_id = cursor.fetchone()
                                cursor.execute('SELECT position_name FROM position WHERE position_id = %s',(position_id,))
                                pos = cursor.fetchone()
                                positions.append(pos[0])
                                cursor.execute('SELECT date,value FROM record WHERE on_line = %s',(ln,))
                                values = cursor.fetchall()
                                for val in values:
                                    date = val[0]
                                    if not (date in Frame.columns):
                                        Frame[date] = 'Не указано'
                                    Frame.loc[iter,date] = val[1]
                                iter+=1
                            Frame.index = positions
                        else:
                            cursor.execute('SELECT position_id FROM position WHERE position_name = %s',(self.ui.cbOutput.currentText(),))
                            position_id = cursor.fetchone()
                            cursor.execute('SELECT line_id FROM line WHERE line_position = %s',(position_id,))
                            lines = cursor.fetchall()
                            regions = []
                            iter = 0
                            for ln in lines:
                                cursor.execute('SELECT line_region FROM line WHERE line_id = %s',(ln,))
                                region_id = cursor.fetchone()
                                cursor.execute('SELECT region_name FROM region WHERE region_id = %s',(region_id,))
                                pos = cursor.fetchone()
                                regions.append(pos[0])
                                cursor.execute('SELECT date,value FROM record WHERE on_line = %s',(ln,))
                                values = cursor.fetchall()
                                for val in values:
                                    date = val[0]
                                    if not (date in Frame.columns):
                                        Frame[date] = 'Не указано'
                                    Frame.loc[iter,date] = val[1]
                                iter+=1
                            Frame.index = regions
                        # Сборка и сохранение
                        if not os.path.exists(file_name):
                            writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
                            writer.save()
                            writer.close()
                        writer = pd.ExcelWriter(file_name, engine='openpyxl')
                        book = openpyxl.load_workbook(file_name)
                        writer.book = book
                        if 'Sheet1' in book.sheetnames:
                            dels = book['Sheet1']
                            book.remove(dels)
                        Frame.to_excel(writer,self.ui.cbOutput.currentText())
                        writer.save()
                        writer.close()
                        self.close()

class room_window(QtWidgets.QWidget):
    def __init__(self,parent):
        super(room_window, self).__init__()
        global sys_user_id
        global sys_user_roles
        self.ui = Ui_self_room()
        self.ui.setupUi(self)
        self.parent = parent
        self.w4 = log_window()
        self.w4.ui.btCancel.clicked.connect(self.w4.close)

    def closeEvent(self, e):
        try:
            self.w4.close()
        except:
            pass
        e.accept()
        

    def RolesSet(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                global sys_user_id
                global sys_user_roles
                cursor.execute('SELECT role FROM role_user WHERE r_user = %s',(sys_user_id,))
                roles = cursor.fetchall()
                sys_user_roles.clear()
                for r in roles:
                    sys_user_roles.append(r[0])
                cursor.execute('SELECT login FROM users WHERE user_id = %s',(sys_user_id,))
                login = cursor.fetchone()
                self.parent.ui.lblUser.setText(login[0])
                
    def ButtonChange(self):
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        with closing(psycopg2.connect(dbname=s_dbname, user=db_user, password=db_user_password, host=db_host, port = db_port)) as conn:
            with conn.cursor() as cursor:
                global sys_user_id
                global sys_user_roles
                self.ui.lblUser.clear()
                cursor.execute('SELECT login FROM users WHERE user_id = %s',(sys_user_id,))
                login = cursor.fetchone()
                self.ui.lblUser.setText(login[0])
                self.ui.lblUser_2.setText('')
                for r in sys_user_roles:
                    cursor.execute('SELECT role_name FROM role WHERE role_id = %s',(r,))
                    role = cursor.fetchone()
                    self.ui.lblUser_2.setText(self.ui.lblUser_2.text()+role[0]+', ')
                self.ui.lblUser_2.setText(self.ui.lblUser_2.text()[:-2])
                try:
                    self.ui.btEnterExit.clicked.disconnect()
                except Exception:
                    pass
                try:
                    self.ui.btRegChange.clicked.disconnect()
                except Exception:
                    pass
                
                if (sys_user_id == 0):
                    self.ui.btEnterExit.setText('Войти')
                    self.ui.btEnterExit.clicked.connect(self.LoginShow)
                    self.ui.btRegChange.setText('Зарегестрироваться')
                    self.ui.btRegChange.clicked.connect(self.RegShow)
                else:
                    self.ui.btEnterExit.setText('Выйти')
                    self.ui.btEnterExit.clicked.connect(self.Logout)
                    self.ui.btRegChange.setText('Сменить логин или пароль')
                    self.ui.btRegChange.clicked.connect(self.ChangeShow)

    def LoginShow(self):
        self.w4.show()
        self.w4.setWindowTitle('Авторизация')
        self.w4.ui.lblConfirm.hide()
        self.w4.ui.tbConfirm.hide()
        self.w4.ui.tbConfirm.clear()
        self.w4.ui.tbLogin.clear()
        self.w4.ui.tbPassword.clear()
        try:
            self.w4.ui.btEnter.clicked.disconnect()
        except Exception:
            pass
        self.w4.ui.btEnter.clicked.connect(self.Login)
    
    def RegShow(self):
        self.w4.show()
        self.w4.setWindowTitle('Регистрация')
        self.w4.ui.lblConfirm.show()
        self.w4.ui.tbConfirm.show()
        self.w4.ui.tbConfirm.clear()
        self.w4.ui.tbLogin.clear()
        self.w4.ui.tbPassword.clear()
        try:
            self.w4.ui.btEnter.clicked.disconnect()
        except Exception:
            pass
        self.w4.ui.btEnter.clicked.connect(self.Reg_User)
    
    def ChangeShow(self):
        self.w4.show()
        self.w4.setWindowTitle('Изменение данных')
        self.w4.ui.lblConfirm.show()
        self.w4.ui.tbConfirm.show()
        self.w4.ui.tbConfirm.clear()
        self.w4.ui.tbLogin.clear()
        self.w4.ui.tbPassword.clear()
        try:
            self.w4.ui.btEnter.clicked.disconnect()
        except Exception:
            pass
        self.w4.ui.btEnter.clicked.connect(self.Change_User_data)
    
    def Login(self):
        global sys_user_id
        global sys_user_roles
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
                slogin = self.w4.ui.tbLogin.text()
                spassword = self.w4.ui.tbPassword.text()
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
                        sys_user_id = suser_id
                        self.RolesSet()
                        self.ButtonChange()
                        self.w4.close()
                    else:
                        msg.setText("Пользователь не найден")
                        msg.exec_()

    def Reg_User(self):
        global sys_user_id
        global sys_user_roles
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
                slogin = self.w4.ui.tbLogin.text()
                spassword = self.w4.ui.tbPassword.text()
                sconfirm = self.w4.ui.tbConfirm.text()
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
                            sys_user_id = nuser_id
                            self.RolesSet()
                            self.ButtonChange()
                            self.w4.close()
    
    def Change_User_data(self):
        global sys_user_id
        global sys_user_roles
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
                slogin = self.w4.ui.tbLogin.text()
                spassword = self.w4.ui.tbPassword.text()
                sconfirm = self.w4.ui.tbConfirm.text()
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
                    cursor.execute('SELECT user_id FROM users WHERE login = %s and not user_id = %s',(slogin,sys_user_id))
                    suser_id = cursor.fetchone()
                    if suser_id:
                        msg.setText("Этот логин уже используется!")
                        msg.exec_()
                    else:
                        try:
                            cursor.execute('UPDATE users SET login = %s,password = %s WHERE user_id = %s',(slogin,spassword,sys_user_id))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                            self.RolesSet()
                            self.ButtonChange()
                            self.w4.close()


    def Logout(self):
        global sys_user_id
        global sys_user_roles
        global s_dbname
        global db_user
        global db_user_password
        global db_host
        global db_port
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Вы уверены, что хотите выйти из аккаунта?")
        msg.setWindowTitle("Личный кабинет")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()   
        if (retval == QtWidgets.QMessageBox.Ok):
            sys_user_id = 0
        self.RolesSet()
        self.ButtonChange()            

class log_window(QtWidgets.QWidget):
    def __init__(self):
        super(log_window, self).__init__()
        self.ui = Ui_Log()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

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
application = main_vindow()
application.show()
try:
    application.w5.raise_()
except:
    pass
 
sys.exit(app.exec())