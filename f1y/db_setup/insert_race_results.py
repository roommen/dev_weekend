import mysql.connector
from common.CommonDefs import cnx_str


def insert_race_result(race_results):
    connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])

    # for results in race_results:
    query = "INSERT INTO race_results(grand_prix, race_date, winner, car, laps) VALUES(%s, %s, %s, %s, %s)"
    print("Data inserted into the table race_results successfully.")
    try:
        cursor = connection.cursor()
        cursor.executemany(query, race_results)
        connection.commit()
    except:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    race_results = [
                    ('Australian', '26 Mar 2017', 'Sebastian Vettel', 'Ferrari', '57'),
                    ('Chinese', '09 Apr 2017', 'Lewis Hamilton', 'Mercedes', '56'),
                    ('Bahrain', '16 Apr 2017', 'Sebastian Vettel', 'Ferrari', '57')
                    ('Russian', '30 Apr 2017', 'Valtteri Bottas', 'Mercedes', '52'),
                    ('Spanish', '14 May 2017', 'Lewis Hamilton', 'Mercedes', '66'),
                    ('Monaco', '28 May 2017', 'Sebastian Vettel', 'Ferrari', '78'),
                    ('Canadian', '11 Jun 2017', 'Lewis Hamilton', 'Mercedes', '70'),
                    ('Azerbaijan', '25 Jun 2017', 'Daniel Ricciardo', 'Red Bull Racing', '51'),
                    ('Austrian', '09 Jul 2017', 'Valtteri Bottas', 'Mercedes', '71'),
                    ('British', '16 Jul 2017', 'Lewis Hamilton', 'Mercedes', '51'),
                    ('Hungarian', '30 Jul 2017', 'Sebastian Vettel', 'Ferrari', '70'),
                    ('Belgium', '27 Aug 2017', 'Lewis Hamilton', 'Mercedes', '44'),
                    ('Italian', '03 Sep 2017', 'Lewis Hamilton', 'Mercedes', '53'),
                    ('Singapore', '17 Sep 2017', 'Lewis Hamilton', 'Mercedes', '58'),
                    ('Malaysian', '01 Oct 2017', 'Max Verstappen', 'Red Bull Racing', '56'),
                    ('Japanese', '08 Oct 2017', 'Lewis Hamilton', 'Mercedes', '53'),
                    ('United States', '22 Oct 2017', 'Lewis Hamilton', 'Mercedes', '56'),
                    ('Mexican', '29 Oct 2017', 'Max Verstappen', 'Red Bull Racing', '71'),
                    ('Brazilian', '12 Nov 2017', 'Sebastian Vettel', 'Ferrari', '71'),
                    ('Abu Dhabi', '26 Nov 2017', 'Valtteri Bottas', 'Mercedes', '55')
                    ]
    insert_race_result(race_results)


if __name__ == '__main__':
    main()
