from dotNET_base.NotifyPropertyChangedBase import *

import clr
import Helpers.clrtype as clrtype

import json

class TrackedItem(NotifyPropertyChangedBase):
    __metaclass__ = clrtype.ClrClass

    def __init__(self,type_track= None, date_start = None, date_end = None):
        super(TrackedItem, self).__init__()
        self.type_track=type_track
        self.date_start=date_start
        self.date_end = date_end

    def _jsonSupport( *args ):
        def default(self,trackedObject):

            jsn = {}
            if trackedObject._id:
                jsn['id'] = trackedObject._id
            else:
                jsn['id']= ""
            if trackedObject._type_track:
                jsn['type_track'] = trackedObject._type_track
            else:
                jsn['type_track']= ""
            if trackedObject._date_start:
                jsn['date_start'] = trackedObject._date_start
            else:
                jsn['date_start']= ""
            if trackedObject._date_end:
                jsn['date_end'] = trackedObject._date_end
            else:
                jsn['date_end']= ""
            return jsn
        """
        def objectHook( obj ):
            if 'type' not in obj:
                return obj
            if obj[ 'type' ] != 'TrackedItem':
                return obj
            return TrackedItem(obj.type_track, obj.date_start, obj.date_end )
        json._default_decoder = json.JSONDecoder( object_hook = objectHook )"""
        json.JSONEncoder.default = default
    _jsonSupport()

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        self._id = value
        self.OnPropertyChanged("id")

    @property
    def type_track(self):
        return self._type_track
 
    @type_track.setter
    def type_track(self, value):
        self._type_track = value
        self.OnPropertyChanged("type_track")

    @property
    def date_start(self):
        return self._date_start
 
    @date_start.setter
    def date_start(self, value):
        self._date_start = value
        self.OnPropertyChanged("date_start")

    @property
    def date_end(self):
        return self._date_end
 
    @date_end.setter
    def date_end(self, val):
        self._date_end = val
        self.OnPropertyChanged("date_end")
