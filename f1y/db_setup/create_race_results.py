import mysql.connector
from common.CommonDefs import cnx_str


def create_race_results():
    connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])

    try:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE race_results(grand_prix VARCHAR(30), race_date VARCHAR(20), winner VARCHAR(50), car VARCHAR(25), laps INTEGER);')
        print("Table race_results created successfully.")
    except IndexError:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    create_race_results()


if __name__ == '__main__':
    main()
