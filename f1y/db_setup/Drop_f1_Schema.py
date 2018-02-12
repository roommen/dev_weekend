import mysql.connector
from common.CommonDefs import cnx_str
import os


def drop_schema():
    connection, cursor = None, None

    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])

        os.system('python drop_race_results.py')

        print("Schema dropped successfully.")
    except mysql.connector.Error as err:
        print("Error occurred", err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()

if __name__ == '__main__':
    drop_schema()
