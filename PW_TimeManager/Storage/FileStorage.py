import datetime
import json
import os
from PointClass import *

def jdefault(o):
    return o.__dict__

def data_load(path):
    if(os.path.isfile(path)!=True):
        jsn={}
        jsn['points']=[]
    else:
        with open(path, 'r') as json_file:
            try:
                x = json_file.read()
                jsn = json.loads(x)
            except ValueError:
                jsn={}
                jsn['points']=[]
    return jsn

def data_add(jsn, datetime, type):
    point = Point(type,datetime)
    jsn['points'].append(point)

def write_json_to_file(jsn):
    with open('d:\\dates.json', 'w+') as json_file:
        json_file.write(json.dumps(jsn, default=jdefault))

if __name__ == '__main__':
    now = str(datetime.datetime.now())
    type = "stop"
    jsn = data_load('d:\\dates.json')
    data_add(jsn, now, type)
    write_json_to_file(jsn)
