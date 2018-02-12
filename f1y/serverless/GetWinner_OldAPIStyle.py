import mysql.connector
from common.CommonDefs import cnx_str


def get_winner(grand_prix):
    con, cur, data = None, None, None
    try:
        con = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                      password=cnx_str['password'], database=cnx_str['db'])

        # Get the winner based on grand prix
        query = "SELECT winner FROM f1.race_results WHERE grand_prix='%s';" % grand_prix
        cur = con.cursor()
        cur.execute(query)
        (winner, ) = cur.fetchall()

        if winner:
            # print({"winner": winner[0]})
            return {"winner": winner[0]})
        else:
            # print({"winner": "false"})
            return {"winner": "false"}
    except mysql.connector.Error as err:
        # print({"winner": err})
        return {"winner": err}
    finally:
        if con:
            con.close()
        if cur:
            cur.close()

# if __name__ == '__main__':
#     grand_prix = 'Chinese'
#     get_winner(grand_prix)

def lambda_handler(event, context):
    grand_prix = event['gp']
    return get_winner(grand_prix)
