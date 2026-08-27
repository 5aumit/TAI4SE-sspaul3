from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser


_base_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
_db_config_file = 'db_config.ini'

_cf = configparser.ConfigParser()
_cf.read(os.path.join(_base_dir, _db_config_file))

host = _cf.get("mysqlconf", "host")
port = _cf.get("mysqlconf", "port")
db = _cf.get("mysqlconf", "db_name")
user = _cf.get("mysqlconf", "user")
password = _cf.get("mysqlconf", "password")

# Encapsulating MySQL operation
class DB(object):

    def __init__(self, *args, **kwargs):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            print('- ' + real_sql)
            cursor.execute(real_sql)
        self.conn.commit()
    
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value + ")"

        with self.conn.cursor() as cursor:
            print('- ' + real_sql)
            cursor.execute(real_sql)
        self.conn.commit()
    
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    print('Using INI file: ' + os.path.join(_base_dir, _db_config_file))
    db = DB()
    table_name = "sign_event"
    data = {'id':12,
            'name': '大可乐',
            'attendees_limit': 200,
            'status': 1,
            'address': '古城大理南陵西路12号悦来客栈',
            'start_time': '2012-09-12 14:30:00',
            'create_time': '2018-06-11 09:30:00'
            }
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()