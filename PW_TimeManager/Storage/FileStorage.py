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
        for point in jsn:
            new_item = TrackedItem(point['type_track'],point['date'])
            self._tracked_items.Add(new_item)

    def get_tracked_items(self):
        try:
            return self._tracked_items
        except ValueError:
            return []

    def get_latest_element(self):
        return list(self._tracked_items)[-1]

    @property
    @clrtype.accepts()
    @clrtype.returns(ObservableCollection[TrackedItem])
    def tracked_items(self):
        return self._tracked_items

    def data_add(self,point):
        self._tracked_items.Add(point)
        self.write_json_to_file(self.tracked_items)

    def write_json_to_file(self,jsn):
        with open('d:\\dates.json', 'w+') as json_file:
            temp_array = []
            for point in jsn:
                temp_array.Add(point)
            json_file.write(json.dumps(temp_array))
