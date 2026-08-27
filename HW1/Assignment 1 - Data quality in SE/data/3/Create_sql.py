import sqlite3
import shutil
from Card_reading import reader_card

data = reader_card()

def create_user_officer(file_id): #move office
        file_id = file_id
        x = file_id[2]
        # print(x[0])
        print(x[1:18]) #ID_card
        # 6 gender (7 8)name
        #print('บ้านเลขที่ ' +x[14] +' ' + x[15]+' ' + x[16]+' ' + x[17]+' ' + x[18]+' ' + x[19]+' ' + x[20]+' ' + x[21]) #address
        name_file = x[1:18]
        Name_USER = file_id[7]+' '+file_id[8]
        GENDER = file_id[6]
        # address = x[14] +' ' + x[15]+' ' + x[16]+' ' + x[17]+' ' + x[18]+' ' + x[19]+' ' + x[20]+' ' + x[21]
        address = file_id[15]
        Office = "KMITL" #สมมุติ
        file_name =  name_file+'.db'
        print(file_name)
        conn = sqlite3.connect(file_name)
        cursor = conn.cursor()
        print("create database 0f " + file_name)
        # conn.execute('''CREATE TABLE USER
        #    (ID INT PRIMARY KEY     NOT NULL,
        #     GENDER         TEXT    NOT NULL,
        #     NAME           TEXT    NOT NULL,
        #     ADRESS         TEXT    NOT NULL,
        #     OFFICE         TEXT    NOT NULL);''')
        sqlite_insert_with_param = """INSERT INTO USER
                              (ID, GENDER, NAME, ADRESS, OFFICE)
                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (name_file, Name_USER, GENDER, address, Office)
        print("success created ")
        # conn.execute("INSERT INTO USER VALUES (1, x[1],x[1],x[1],x[1])")
        cursor.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()

        conn.close()
    # except sqlite3.Error as error:
    #     print("Failed to insert Python variable into sqlite table", error)
    # finally:
    #     if conn:
    #         conn.close()
    #         print("The SQLite connection is closed")

create_user_officer(data)
