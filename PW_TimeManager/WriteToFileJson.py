import datetime
import json

class Point(object):
    def __init__(self,type,date):
        self.type=type
        self.date=date

def jdefault(o):
    return o.__dict__

def json_load(path):
    with open(path, 'r') as json_file:
        try:
            x = json_file.read()
            jsn = json.loads(x)
        except ValueError:
            jsn={}
            jsn['points']=[]#"""
    return jsn

def json_add(jsn, datetime, type):
    point = Point(type,datetime)
    jsn['points'].append(point)

def write_json_to_file(jsn):
    with open('d:\\dates.json', 'w+') as json_file:
        json_file.write(json.dumps(jsn, default=jdefault))

if __name__ == '__main__':
    now = str(datetime.datetime.now())
    type = "stop"
    jsn = json_load('d:\\dates.json')
    json_add(jsn, now, type)
    write_json_to_file(jsn)
