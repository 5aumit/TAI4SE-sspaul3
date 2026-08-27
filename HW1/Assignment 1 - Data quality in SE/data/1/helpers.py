import json
import datetime
import string
import random
import logging

import jwt

from main import db
from main.config import config


def execute_sql_from_file(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()

    # All SQL commands (split on ';')
    sql_commands = sql_file.split(';')

    # Execute every command from the input file
    for command in sql_commands:
        # This will skip and report validation
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            db.session.execute(command.decode('utf-8'))
        except Exception, e:
            logging.exception(e)


def create_mock_data():
    execute_sql_from_file('./sql/test.sql')


def drop_tables():
    execute_sql_from_file('./sql/drop_tables.sql')


def create_headers(access_token=None):
    headers = {
        'Content-Type': 'application/json'
    }

    if access_token:
        headers.update({
            'Authorization': 'Bearer {}'.format(access_token)
        })

    return headers


def json_response(response):
    return json.loads(response.data.decode('utf-8'))


def generate_access_token(user_id, is_expired=False):
    """
    Generate JWT Token for test authentication.

    :param user_id: User ID
    :param is_expired: To generate expired tokens
    :return: JWT Token string
    """

    iat = datetime.datetime.utcnow()

    return jwt.encode({
        'sub': user_id,                             # Subject of this token
        'iat': iat,                                 # Issued at
        'exp': iat + datetime.timedelta(hours=1)    # Expired at
        if not is_expired
        else iat - datetime.timedelta(minutes=5)
    }, config.SECRET_KEY)


def random_string(string_length=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(string_length))
