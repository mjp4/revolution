import json

def get_charger_list():
    """
    Funciton that returns the charger list stored in a json file

    Returns a list of dictionaries with the charger content on them
    """

    charger_file = open('50over.json','r')
    content = charger_file.read()
    charger_list = json.loads(content)

    return charger_list


get_charger_list()