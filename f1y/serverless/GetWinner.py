import mysql.connector
from common.CommonDefs import cnx_str


##############################
# Builders
##############################


def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech


def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response


def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card


##############################
# Responses
##############################


def conversation(title, body, session_attributes):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet, session_attributes=session_attributes)


def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)


def continue_dialog():
    message = {}
    message['shouldEndSession'] = False
    message['directives'] = [{'type': 'Dialog.Delegate'}]
    return build_response(message)


##############################
# Custom Intents
##############################

def get_winner(event, context):
    # grand_prix = event['session']['attributes']
    # gra
    # print(event)
    # grand_prix = "Chinese"
    grand_prix = event['request']['intent']['slots']['grand_prix']['value']
    # print(grand_prix)
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
            # return {"winner": winner[0]})
            return statement("getWinner", winner[0])
        else:
            # print({"winner": "false"})
            return statement("getWinner", false)
    except mysql.connector.Error as err:
        # print({"winner": err})
        return statement("getWinner", "error")
    finally:
        if con:
            con.close()
        if cur:
            cur.close()


# def counter_intent(event, context):
#     session_attributes = event['session']['attributes']

#     if "counter" in session_attributes:
#         session_attributes['counter'] += 1

#     else:
#         session_attributes['counter'] = 1

#     return conversation("counter_intent", session_attributes['counter'],
#                         session_attributes)


# def trip_intent(event, context):
#     dialog_state = event['request']['dialogState']

#     if dialog_state in ("STARTED", "IN_PROGRESS"):
#         return continue_dialog()

#     elif dialog_state == "COMPLETED":
#         return statement("trip_intent", "Have a good trip")

#     else:
#         return statement("trip_intent", "No dialog")


##############################
# Required Intents
##############################


def cancel_intent():
    return statement("CancelIntent", "You want to cancel")	#don't use CancelIntent as title it causes code reference error during certification 


def help_intent():
    return statement("CancelIntent", "You want help")		#same here don't use CancelIntent


def stop_intent():
    return statement("StopIntent", "You want to stop")		#here also don't use StopIntent


##############################
# On Launch
##############################


# def on_launch(event, context):
#     return statement("title", "body")


def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents
    if intent == "getWinner":
        return get_winner(event, context)

    # Required Intents
    if intent == "AMAZON.CancelIntent":
        return cancel_intent()

    if intent == "AMAZON.HelpIntent":
        return help_intent()

    if intent == "AMAZON.StopIntent":
        return stop_intent()


def lambda_handler(event, context):
    # if event['request']['type'] == "LaunchRequest":
    #     return on_launch(event, context)
    if event['request']['type'] == "IntentRequest":
        return intent_router(event, context)
