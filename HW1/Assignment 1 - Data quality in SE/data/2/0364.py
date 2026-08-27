#coding: utf-8
#/usr/bin/python
__author__='julia sayapina'

### Use db_reset.py to drop the db and recreate it, then use 'migrate' --> 'createsuperuser' --> 'makemigrations' --> 'migrate' as usual.
### This will create the DB structure as it has to be from django
### Then use test_db_fullfill.py to fullfill the db with test data. if you don't need to create tables manually don't use db_create()

from warnings import filterwarnings
import MySQLdb as db
import os
import shutil
import os
import sys 
from subprocess import Popen, PIPE, STDOUT
import uuid
from decimal import *
from datetime import date
from random import randint


# Создание или открытие файла базы данных и создание схемы
filterwarnings('ignore', category = db.Warning)
db_name = 'ved3'

def db_create():    # creates tables manually (doesn't create AO and AB tables)
  cur.execute("""
        create table if not exists Offshores_asset (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            asset_name          VARCHAR(100),
            asset_link          VARCHAR(200),
            slug                CHAR(200),
            uuid                CHAR(36)
    );
    """)
  cur.execute("""
        create table if not exists Offshores_offshore (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            off_name            VARCHAR(50),
            off_jurisdiction    VARCHAR(50),
            file                VARCHAR(100),
            image               VARCHAR(100),
            off_parent          VARCHAR(50),
            off_link            VARCHAR(300),
            slug                VARCHAR(200),
            uuid                CHAR(36)
    );
    """)
  cur.execute("""
        create table if not exists Offshores_beneficiary (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            ben_name            VARCHAR(50),
            ben_lastname        VARCHAR(100),
            ben_midname         VARCHAR(30),
            ben_holding         VARCHAR(70),
            ben_link            VARCHAR(300),
            slug                VARCHAR(200),
            uuid                CHAR(36)
    );
    """)
  cur.execute("""
        create table if not exists Offshores_beneficiariesoffshores (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            share               DECIMAL,
            rel_date            DATE,
            source              VARCHAR(150),
            link                VARCHAR(200),
            beneficiary_id      INT,
            offshore_id         INT,
            uuid                CHAR(36)
    );
    """)
  conn.commit()
  print('tables created')


def db_insert(numrows):
  # inserts test data into tables
  for x in xrange(0,numrows): #creates test data for tables
    num = str(x)
    a_name = 'Asset' + num
    a_link = 'http://somelink/'+a_name
    a_uuid = uuid.uuid4().hex
    a_slug = a_name + '-' + str(a_uuid)
    o_name = 'Offshore' + num
    o_jur = 'Cyprus'
    o_file = 'offshores/favicon.xcf'
    o_image = 'offshores/favicon.png'
    o_prnt = 'parent' + num
    o_link = 'http://' + o_name + '-' + num + '.com'
    o_uuid = uuid.uuid4().hex
    o_slug = o_name + str(o_uuid)
    b_name = 'Michael' + num
    b_lname = 'Prohorov' + num
    b_mname = 'Dmitrievich' + num
    b_holding = 'Onexim' + num
    b_link = 'http://onexim.ru/' + b_name + b_lname + '-' + num + '.com'
    b_uuid = uuid.uuid4().hex
    b_slug = b_lname + str(b_uuid)

    try: #inserts test data to tables via SQL; still produces wierd errors for Beneficiariesoffshores idk why
      cur.execute("""INSERT INTO Offshores_asset (asset_name, asset_link, slug, uuid) VALUES (%s,%s,%s,%s)""",(a_name, a_link, a_slug, a_uuid))
      cur.execute("""INSERT INTO Offshores_offshore (off_name, off_jurisdiction, file, image, off_parent, off_link, slug, uuid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(o_name, o_jur, o_file, o_image, o_prnt, o_link, o_slug, o_uuid))
      cur.execute("""INSERT INTO Offshores_beneficiary (ben_name, ben_lastname, ben_midname, ben_holding, ben_link, slug, uuid) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(b_name, b_lname, b_mname, b_holding, b_link, b_slug, b_uuid))
      conn.commit()
    except Exception as e:
      print ("Exception 1:", type(e), e)

def db_insert_linktables(numrows):
  # inserts test data into linking tables; has to be called after db_insert(), as first basic tables need to be generated to produce links between
  # them using random numbers
  for x in xrange(0,numrows): #creates test data for tables
    num = str(x)
    bo_share = Decimal(x)
    bo_date = date(2016, randint(1, 12), randint(1, 28))
    bo_source = 'source' + num
    bo_link = 'http://bo.ru/' + bo_source + '-' + num
    bo_ben = randint(1, numrows)
    bo_off = randint(1, numrows)
    bo_uuid = uuid.uuid4().hex
    oa_uuid = uuid.uuid4().hex
    oa_share = Decimal(x)
    oa_date = date(2016, randint(1, 12), randint(1, 28))
    oa_source = 'source' + num
    oa_link = 'http://oa.ru/' + oa_source + '-' + num
    oa_asset = randint(1, numrows)
    oa_off = randint(1, numrows)
    ab_uuid = uuid.uuid4().hex
    ab_share = Decimal(x)
    ab_date = date(2016, randint(1, 12), randint(1, 28))
    ab_source = 'source' + num
    ab_link = 'http://ab.ru/' + oa_source + '-' + num
    ab_asset = randint(1, numrows)
    ab_ben = randint(1, numrows)

    try: #inserts test data to tables via SQL; still produces wierd errors for Beneficiariesoffshores idk why
      cur.execute("""INSERT INTO Offshores_beneficiariesoffshores (share, rel_date, source, link, beneficiary_id, offshore_id, uuid) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(bo_share, bo_date, bo_source, bo_link, bo_ben, bo_off, bo_uuid))
      cur.execute("""INSERT INTO Offshores_offshoresassets (uuid, share, rel_date, source, link, asset_id, offshore_id) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(oa_uuid, oa_share, oa_date, oa_source, oa_link, oa_asset, oa_off))
      cur.execute("""INSERT INTO Offshores_assetsbeneficiaries (uuid, share, rel_date, source, link, asset_id, beneficiary_id) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(ab_uuid, ab_share, ab_date, ab_source, ab_link, ab_asset, ab_ben))
      conn.commit()
    except Exception as e:
      print ("Exception 1:", type(e), e)

numrows = 20
try:
  conn = db.connect("localhost","root","0013Tau","ved2" )
  cur = conn.cursor()
  # db_create()       #<-- to create tables manually uncomment this
  db_insert(numrows)
  db_insert_linktables(numrows) # IMPORTANT! has to be called ONLY after db_insert()!

except Exception as e:
  print ("Exception 0:", type(e), e)

except: db.rollback() 


conn.commit()
conn.close()
print ('DB fullfilled')


# def main():
#   if len(sys.argv) != 2:
#     print('usage: python3 db_fullfill.py [numrows]')
#     sys.exit(1)

#   if len(sys.argv) == 2: 
#     numrows = sys.argv[1]

#   else:
#     numrows = 15
#   print (numrows)

#   return numrows
#   sys.exit(1)

# if __name__ == '__main__':
#     main()

