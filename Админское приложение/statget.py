import requests
import datetime
import re
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import os
import psycopg2
import xlrd
from contextlib import closing

def statisticsGet_Debet():
    try:
        now = datetime.datetime.now()
        url = 'http://www.cbr.ru/statistics/bank_sector/sors/#a_63140'
        parse = requests.get(url)
        soup = BeautifulSoup(parse.content,'html.parser')
        titles = soup.find('a',{'id':'a_67587'})
        dls = 'http://www.cbr.ru'+titles.get('href')
        resp = requests.get(dls)
        xl = pd.ExcelFile(resp.content)
        for Sh in xl.sheet_names:
            frame = pd.read_excel(io=resp.content,sheet_name=Sh,header=0,skiprows=1)
            frame.rename(columns={'Unnamed: 0':'Регион'},inplace=True)
            for col_name in frame.columns.values[1:]:
                    if (col_name.day<10):            
                        new_name = '0'+str(col_name.day) + '.'
                    else:
                        new_name = str(col_name.day) + '.'
                    if (col_name.month<10):            
                        new_name = new_name+'0'+str(col_name.month) + '.'
                    else:
                        new_name = new_name+str(col_name.month) + '.'
                    new_name = new_name + str(col_name.year)
                    frame.rename(columns={col_name:new_name},inplace=True)
            iter = 0
            for reg_name in frame['Регион'].values:
                new_name = re.sub(r'РОССИЙСКАЯ ФЕДЕРАЦИЯ','Российская федерация',reg_name)
                new_name = re.sub(r'ФЕДЕРАЛЬНЫЙ ОКРУГ','ФО',new_name)
                new_name = re.sub(r'\s+в том числе ','',new_name)
                new_name = re.sub(r'\s{2,}','',new_name)
                new_name = re.sub(r' без данных .+','(чистая)',new_name)
                if re.match(r'\w+(\s|-)',new_name):
                    fword = re.match(r'\w+(\s|-)',new_name).group(0)
                    new_name = re.sub(re.compile(fword),fword[0]+fword[1:].lower(),new_name)
                    if re.search(re.compile(fword[0]+fword[1:].lower()+'\w+\s'),new_name):
                        sword = re.search(re.compile(fword[0]+fword[1:].lower()+'\w+\s'),new_name).group(0)
                        new_name = re.sub(re.compile(sword),sword[:len(fword[0]+fword[1:].lower())+1]+sword[len(fword[0]+fword[1:].lower())+1:].lower(),new_name)
                new_name = re.sub(r'г\. ','Г.',new_name)
                new_name.strip()
                frame['Регион'].iloc[iter] = new_name
                iter+=1
            Sh=re.sub(r'просроч.','проср',Sh)
            with closing(psycopg2.connect(dbname='testdb', user='postgres', password='1qaz!QAZ', host='localhost')) as conn:
                with conn.cursor() as cursor:
                    try:
                            cursor.execute('SELECT COUNT (*) FROM position WHERE position_name = %s',('Долги(кред)'+Sh,))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO position (position_name,unit) VALUES (%s,%s)',('Долги(кред)'+Sh,'млн руб'))
                    except psycopg2.DatabaseError as err:
                            print("Error:",err)
                    else:
                            conn.commit()
                    cursor.execute('SELECT position_id FROM position WHERE position_name = %s',('Долги(кред)'+Sh,))
                    position_id = cursor.fetchone()
                    iter2 = 0
                    for dbRegion in frame['Регион'].values:
                        try:
                            cursor.execute('SELECT COUNT (*) FROM region WHERE region_name = %s',(dbRegion,))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO region (region_name) VALUES (%s)',(dbRegion,))
                            cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(dbRegion,))
                            region_id = cursor.fetchone()
                            cursor.execute('SELECT COUNT (*) FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO line (line_position,line_region) VALUES (%s,%s)',(position_id,region_id))
                            cursor.execute('SELECT line_id FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                            line_id = cursor.fetchone()
                            cursor.execute('SELECT COUNT (*) FROM role_rule WHERE line = %s',(line_id,))
                            rule = cursor.fetchone()
                            if (rule[0]<1):
                                
                                cursor.execute('INSERT INTO role_rule (role,line) VALUES (%s,%s)',('1',line_id))
                            for dbDate in frame.columns.values:
                                if (dbDate != 'Регион'):
                                    record_value = str(frame[dbDate].iloc[iter2])
                                    cursor.execute('SELECT record_id FROM record WHERE date = %s and on_line = %s',(dbDate,line_id))
                                    value = cursor.fetchone()
                                    if (str(value) == 'None'):
                                        cursor.execute('INSERT INTO record (date,value,on_line) VALUES (%s,%s,%s)',(dbDate,record_value,line_id))
                                    else:
                                        cursor.execute('UPDATE record set date = %s,value = %s,on_line = %s WHERE record_id = %s',(dbDate,record_value,line_id,value))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                        iter2+=1
    except requests.ConnectionError:
        return("Could not connect")

def statisticsGet_Loans():
    try:
        now = datetime.datetime.now()
        url = 'http://www.cbr.ru/statistics/bank_sector/sors/#a_63140'
        parse = requests.get(url)
        soup = BeautifulSoup(parse.content,'html.parser')
        titles = soup.find('a',{'id':'a_67585'})
        dls = 'http://www.cbr.ru'+titles.get('href')
        resp = requests.get(dls)
        xl = pd.ExcelFile(resp.content)
        month = {'Январь':'01.01','Февраль':'01.02','Март':'01.03','Апрель':'01.04','Май':'01.05','Июнь':'01.06','Июль':'01.07','Август':'01.08','Сентябрь':'01.09','Октябрь':'01.10','Ноябрь':'01.11','Декабрь':'01.12'}
        for Sh in xl.sheet_names:
            frame = pd.read_excel(io=resp.content,sheet_name=Sh,header=0,skiprows=1)
            frame.rename(columns={'Unnamed: 0':'Регион'},inplace=True)
            for col_name in frame.columns.values:
                if re.search(r'\S+',col_name).group(0) in month:
                    new_name = re.sub(r'\S+\s',month[re.search(r'\S+',col_name).group(0)]+'.',col_name)
                    frame.rename(columns={col_name:new_name},inplace=True)
            iter = 0
            for reg_name in frame['Регион'].values:
                new_name = re.sub(r'РОССИЙСКАЯ ФЕДЕРАЦИЯ','Российская федерация',reg_name)
                new_name = re.sub(r'ФЕДЕРАЛЬНЫЙ ОКРУГ','ФО',new_name)
                new_name = re.sub(r'\s+в том числе ','',new_name)
                new_name = re.sub(r'\s{2,}','',new_name)
                new_name = re.sub(r' без данных .+','(чистая)',new_name)
                if re.match(r'\w+(\s|-)',new_name):
                    fword = re.match(r'\w+(\s|-)',new_name).group(0)
                    new_name = re.sub(re.compile(fword),fword[0]+fword[1:].lower(),new_name)
                    if re.search(re.compile(fword[0]+fword[1:].lower()+'\w+\s'),new_name):
                        sword = re.search(re.compile(fword[0]+fword[1:].lower()+'\w+\s'),new_name).group(0)
                        new_name = re.sub(re.compile(sword),sword[:len(fword[0]+fword[1:].lower())+1]+sword[len(fword[0]+fword[1:].lower())+1:].lower(),new_name)
                new_name = re.sub(r'г\. ','Г.',new_name)
                new_name.strip()
                frame['Регион'].iloc[iter] = new_name
                iter+=1
            with closing(psycopg2.connect(dbname='testdb', user='postgres', password='1qaz!QAZ', host='localhost')) as conn:
                with conn.cursor() as cursor:
                    try:
                            cursor.execute('SELECT COUNT (*) FROM position WHERE position_name = %s',('Объем кредитов МСП '+Sh,))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO position (position_name,unit) VALUES (%s,%s)',('Объем кредитов МСП '+Sh,'млн руб'))
                    except psycopg2.DatabaseError as err:
                            print("Error:",err)
                    else:
                            conn.commit()
                    cursor.execute('SELECT position_id FROM position WHERE position_name = %s',('Объем кредитов МСП '+Sh,))
                    position_id = cursor.fetchone()
                    iter2 = 0
                    for dbRegion in frame['Регион'].values:
                        try:
                            cursor.execute('SELECT COUNT (*) FROM region WHERE region_name = %s',(dbRegion,))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO region (region_name) VALUES (%s)',(dbRegion,))
                            cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(dbRegion,))
                            region_id = cursor.fetchone()
                            cursor.execute('SELECT COUNT (*) FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO line (line_position,line_region) VALUES (%s,%s)',(position_id,region_id))
                            cursor.execute('SELECT line_id FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                            line_id = cursor.fetchone()
                            cursor.execute('SELECT COUNT (*) FROM role_rule WHERE line = %s',(line_id,))
                            rule = cursor.fetchone()
                            if (rule[0] <1):
                                
                                cursor.execute('INSERT INTO role_rule (role,line) VALUES (%s,%s)',('1',line_id))
                            for dbDate in frame.columns.values:
                                if (dbDate != 'Регион'):
                                    record_value = str(frame[dbDate].iloc[iter2])
                                    cursor.execute('SELECT record_id FROM record WHERE date = %s and on_line = %s',(dbDate,line_id))
                                    value = cursor.fetchone()
                                    if (str(value) == 'None'):
                                        cursor.execute('INSERT INTO record (date,value,on_line) VALUES (%s,%s,%s)',(dbDate,record_value,line_id))
                                    else:
                                        cursor.execute('UPDATE record set date = %s,value = %s,on_line = %s WHERE record_id = %s',(dbDate,record_value,line_id,value))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                        iter2+=1
    except requests.ConnectionError:
        return("Could not connect")

def statisticsGet_nalog():
    try:
        url = 'https://rmsp.nalog.ru/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        pattern = re.compile("var STATISTICS_DATA = \[\{.*?\}\]",re.DOTALL)
        script = soup.find('div',{'id':'uniPageWrapper'}).find('div',{'id':'uniPageMain'}).find('div',{'id':'content'}).find_all('script',{'type':'text/javascript'})
        Region = []
        Total = []
        ul_Total = []
        ul_Micro = []
        ul_Mini = []
        ul_Normal = []
        ip_Total = []
        ip_Micro = []
        ip_Mini = []
        ip_Normal = []
        for item in script:
            out = re.search(pattern,'r'+item.string)
            if out:
                date = re.search(r"\"stat_date\"\:\"\d\d\.\d\d\.\d\d\d\d",out[0])[0]
                regs = re.findall(r"\"cnt_name\"\:\".*?\"",out[0])
                for reg in regs:
                    treg = (reg[len("\"cnt_name\":\""):len(reg)-1])
                    Region.append(treg)
                tts = re.findall(r"\"cnt_total\"\:\d*",out[0])
                for tt in tts:
                    ttt = (tt[len("\"cnt_total\":"):len(tt)])
                    Total.append(ttt)
                utts = re.findall(r"\"cnt_ul_total\"\:\d*",out[0])
                for utt in utts:
                    tutt = (utt[len("\"cnt_ul_total\":"):])
                    ul_Total.append(tutt)
                umicros = re.findall(r"\"cnt_ul_micro\"\:\d*",out[0])
                for umicro in umicros:
                    tumicro = (umicro[len("\"cnt_ul_micro\":"):])
                    ul_Micro.append(tumicro)
                uminis = re.findall(r"\"cnt_ul_mini\"\:\d*",out[0])
                for umini in uminis:
                    tumini = (umini[len("\"cnt_ul_mini\":"):])
                    ul_Mini.append(tumini)
                unormals = re.findall(r"\"cnt_ul_normal\"\:\d*",out[0])
                for unormal in unormals:
                    tunormal = (unormal[len("\"cnt_ul_normal\":"):])
                    ul_Normal.append(tunormal)
                itts = re.findall(r"\"cnt_ip_total\"\:\d*",out[0])
                for itt in itts:
                    titt = (itt[len("\"cnt_ip_total\":"):len(itt)])
                    ip_Total.append(tutt)
                imicros = re.findall(r"\"cnt_ip_micro\"\:\d*",out[0])
                for imicro in imicros:
                    timicro = (imicro[len("\"cnt_ip_micro\":"):])
                    ip_Micro.append(timicro)
                iminis = re.findall(r"\"cnt_ip_mini\"\:\d*",out[0])
                for imini in iminis:
                    timini = (imini[len("\"cnt_ip_mini\":"):])
                    ip_Mini.append(timini)
                inormals = re.findall(r"\"cnt_ip_normal\"\:\d*",out[0])
                for inormal in inormals:
                    tinormal = (inormal[len("\"cnt_ip_normal\":"):])
                    ip_Normal.append(tinormal)
        Frame = pd.DataFrame()
        Frame['Регион'] = pd.Series(Region)
        Frame['Всего ЮР и ИП'] = pd.Series(Total)
        Frame['Всего юридических лиц'] = pd.Series(ul_Total)
        Frame['Микро ЮР'] = pd.Series(ul_Micro)
        Frame['Мини ЮР'] = pd.Series(ul_Mini)
        Frame['Среднее ЮР'] = pd.Series(ul_Normal)
        Frame['Всего индивидуальных предпренимателей'] = pd.Series(ip_Total)
        Frame['Микро ИП'] = pd.Series(ip_Micro)
        Frame['Мини ИП'] = pd.Series(ip_Mini)
        Frame['Среднее ИП'] = pd.Series(ip_Normal)
        tdate = date[len("\"stat_date\"\:"):]
        with closing(psycopg2.connect(dbname='testdb', user='postgres', password='1qaz!QAZ', host='localhost')) as conn:
            with conn.cursor() as cursor:
                for dbRegion in Frame['Регион'].values:
                    try:
                        cursor.execute('SELECT COUNT (*) FROM region WHERE region_name = %s',(dbRegion,))
                        value = str(cursor.fetchone())
                        if (value == '(0,)'):
                            cursor.execute('INSERT INTO region (region_name) VALUES (%s)',(dbRegion,))
                    except psycopg2.DatabaseError as err:
                        print("Error:",err)
                    else:
                        conn.commit()
                for dbPosition in Frame.columns.values:
                    if (dbPosition != 'Регион'):
                        try:
                            cursor.execute('SELECT COUNT (*) FROM position WHERE position_name = %s',(dbPosition,))
                            value = str(cursor.fetchone())
                            if (value == '(0,)'):
                                cursor.execute('INSERT INTO position (position_name,unit) VALUES (%s,%s)',(dbPosition,'шт'))
                        except psycopg2.DatabaseError as err:
                            print("Error:",err)
                        else:
                            conn.commit()
                for dbPosition in Frame.columns.values:
                    iter = 0
                    if (dbPosition != 'Регион'):
                        for dbRegion in Frame['Регион'].values:
                            cursor.execute('SELECT position_id FROM position WHERE position_name = %s',(dbPosition,))
                            position_id = cursor.fetchone()
                            cursor.execute('SELECT region_id FROM region WHERE region_name = %s',(dbRegion,))
                            region_id = cursor.fetchone()
                            try:
                                cursor.execute('SELECT COUNT (*) FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                                value = str(cursor.fetchone())
                                if (value == '(0,)'):
                                    cursor.execute('INSERT INTO line (line_position,line_region) VALUES (%s,%s)',(position_id,region_id))
                            except psycopg2.DatabaseError as err:
                                print("Error:",err)
                            else:
                                conn.commit()
                            cursor.execute('SELECT line_id FROM line WHERE line_position = %s and line_region = %s',(position_id,region_id))
                            line_id = cursor.fetchone()
                            cursor.execute('SELECT COUNT (*) FROM role_rule WHERE line = %s',(line_id,))
                            rule = cursor.fetchone()
                            if (rule[0] < 1):
                                
                                cursor.execute('INSERT INTO role_rule (role,line) VALUES (%s,%s)',('1',line_id))
                            record_value = Frame[dbPosition].iloc[iter]
                            iter+=1
                            try:
                                cursor.execute('SELECT record_id FROM record WHERE date = %s and on_line = %s',(tdate,line_id))
                                value = cursor.fetchone()
                                if (str(value) == 'None'):
                                    cursor.execute('INSERT INTO record (date,value,on_line) VALUES (%s,%s,%s)',(tdate,record_value,line_id))
                                else:
                                    cursor.execute('UPDATE record set date = %s,value = %s,on_line = %s WHERE record_id = %s',(tdate,record_value,line_id,value))
                            except psycopg2.DatabaseError as err:
                                print("Error:",err)
                            else:
                                conn.commit()
    except requests.ConnectionError:
        return("Could not connect")