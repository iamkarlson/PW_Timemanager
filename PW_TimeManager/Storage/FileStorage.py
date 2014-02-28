import sys
sys.path.append("Objects")

import clr
import Helpers.clrtype as clrtype

clr.AddReference("System.Core")
import System
clr.ImportExtensions(System.Linq)

from System.Collections.ObjectModel import *

from Objects.TrackedItemClass import *

import datetime
import json
import os

class FileStorage(object):
    def __init__(self,path):
        self.path = path
        self.version = "1.0"

    def _parse_json_item(self,jsn):
        trackedObject = TrackedItem()
        try:
            trackedObject.id = jsn['id']
        except:
            trackedObject.id = ""
        try:
            trackedObject.type_track = jsn['type_track']
        except:
            trackedObject.type_track = ""
        try:
            trackedObject.start_date = jsn['start_date']
        except:
            trackedObject.start_date = ""
        try:
            trackedObject.end_date  = jsn['end_date']
        except:
            trackedObject.end_date = ""
        return trackedObject

    def data_load(self):
        if(os.path.isfile(self.path)!=True):
            jsn=[]
        else:
            with open(self.path, 'r') as json_file:
                try:
                    x = json_file.read()
                    jsn = json.loads(x)
                except ValueError:
                    jsn=[]
        self._tracked_items = ObservableCollection[TrackedItem]()
        try:
            jsn["version"]
            points = jsn["points"]
        except:
            points = []
        for index,point in enumerate(points):
            new_item = self._parse_json_item(point)
            new_item.id=index+1
            self._tracked_items.Add(new_item)

    def get_tracked_items(self):
        try:
            return self._tracked_items
        except ValueError:
            return []

    def get_latest_element(self):
        if(len(self._tracked_items)>0 ):
            return list(self._tracked_items)[-1]
        return None
    @property
    @clrtype.accepts()
    @clrtype.returns(ObservableCollection[TrackedItem])
    def tracked_items(self):
        return self._tracked_items

    def data_update(self,point):
        try:
            ind = self._find_index(list(self._tracked_items), point)
            self._tracked_items[ind].start_date = point.start_date
            self._tracked_items[ind].end_date = point.end_date 
            self._tracked_items[ind].type_track = point.type_track 
        except ValueError:
            last_point =self.get_latest_element()
            if(last_point != None):
                point.id = last_point.id +1
            else:
                point.id=1
            self._tracked_items.Add(point)
        data_to_write = {}
        data_to_write['version'] = self.version
        data_to_write['points'] = list(self.tracked_items)
        self.write_json_to_file(data_to_write)

    def _find_index (self, item_list, target):
        try:
            temp_id = target.id
        except:
            temp_id = -1
        for ind,item in enumerate(item_list):
            if item.id == temp_id:
                return ind
        return -1

    def write_json_to_file(self,jsn):
        with open('d:\\dates.json', 'w+') as json_file:
            json_file.write(json.dumps(jsn))
