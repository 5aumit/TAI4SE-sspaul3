'''
Created on 2017/01/31

@author: Brian
'''
import sqlite3
from os.path import isfile, getsize

defaultDatabase = "textToolStrings.db"

def create_table():
    conn = sqlite3.connect(defaultDatabase)
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS textStrings(strings TEXT)')
    curs.close()
    conn.close()
    
def data_entry(stringValue):
    conn = sqlite3.connect(defaultDatabase)
    curs = conn.cursor()
    curs.execute("INSERT INTO textStrings (strings) VALUES (?)", (stringValue,))
    conn.commit()
    curs.close()
    conn.close()
