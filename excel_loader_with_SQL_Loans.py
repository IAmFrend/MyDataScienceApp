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

def statisticsGet_Loans():
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
                            cursor.execute('INSERT INTO role_rule (role,line) VALUES (%s,%s)',('0',line_id))
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
            