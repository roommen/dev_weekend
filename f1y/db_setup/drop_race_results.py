import mysql.connector
from common.CommonDefs import cnx_str


def drop_race_results():
    connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])

    try:
        cursor = connection.cursor()

        cursor.execute('DROP TABLE race_results;')
        print("Table race_results dropped successfully.")
    except IndexError:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    drop_race_results()


if __name__ == '__main__':
    main()

