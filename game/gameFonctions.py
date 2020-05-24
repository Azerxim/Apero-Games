import json


def MEF(msg, source, destination):
    if type(msg) is dict:
        for k in msg.keys():
            if type(msg[k]) is str:
                msg[k] = msg[k].replace(source, destination)
            else:
                MEF(msg[k], source, destination)
    elif type(msg) is list:
        for x in range(0, len(msg)):
            if type(msg[x]) is str:
                msg[x] = msg[x].replace(source, destination)
            else:
                MEF(msg[x], source, destination)
    elif type(msg) is int:
        pass
    else:
        msg = msg.replace(source, destination)
    return msg


def read(source):
    with open(source, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def dump(source, local):
    with open(source, 'w', encoding='utf-8') as fp:
        json.dump(local, fp, indent=2)
