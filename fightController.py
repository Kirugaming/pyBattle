import json


def fight():
    monsterNames = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(monsterNames)

    print(y["name"])
