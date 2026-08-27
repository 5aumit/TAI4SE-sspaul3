import os


def get_os_env_value(key):
    return os.getenv(key)


def get_mysql_uri(user, password, host, database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


MASTER_MYSQL_DATABASE_USER = get_os_env_value('MASTER_MYSQL_DATABASE_USER')
MASTER_MYSQL_DATABASE_PASSWORD = get_os_env_value('MASTER_MYSQL_DATABASE_PASSWORD')
MASTER_MYSQL_DATABASE_HOST = get_os_env_value('MASTER_MYSQL_DATABASE_HOST')
MASTER_MYSQL_DATABASE_DB_CASAONE = get_os_env_value('MASTER_MYSQL_DATABASE_DB_CASAONE')

# SQLALCHEMY_POOL_RECYCLE = 60 * 10
# SQLALCHEMY_POOL_TIMEOUT = 60 * 20
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True

SQLALCHEMY_DATABASE_URI = get_mysql_uri(MASTER_MYSQL_DATABASE_USER, MASTER_MYSQL_DATABASE_PASSWORD,
                                        MASTER_MYSQL_DATABASE_HOST, MASTER_MYSQL_DATABASE_DB_CASAONE)

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True
}
