from dotNET_base.NotifyPropertyChangedBase import *

import clr
import Helpers.clrtype as clrtype

import json

class TrackedItem(NotifyPropertyChangedBase):
    __metaclass__ = clrtype.ClrClass

    def __init__(self,type_track= None, start_date = None, end_date = None):
        super(TrackedItem, self).__init__()
        self.type_track=type_track
        self.start_date=start_date
        self.end_date = end_date

    def _jsonSupport( *args ):
        def default(self,trackedObject):
            jsn = {}
            try:
                jsn['id'] = trackedObject._id
            except:
                jsn['id']= ""
            try:
                jsn['type_track'] = trackedObject._type_track
            except:
                jsn['type_track']= ""
            try:
                jsn['start_date'] = trackedObject._start_date
            except:
                jsn['start_date']= ""
            try:
                jsn['end_date'] = trackedObject._end_date
            except:
                jsn['end_date']= ""            
            return jsn
        """
        def objectHook( obj ):
            if 'type' not in obj:
                return obj
            if obj[ 'type' ] != 'TrackedItem':
                return obj
            return TrackedItem(obj.type_track, obj.start_date, obj.end_date )
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
    def start_date(self):
        return self._start_date
 
    @start_date.setter
    def start_date(self, value):
        self._start_date = value
        self.OnPropertyChanged("start_date")

    @property
    def end_date(self):
        return self._end_date
 
    @start_date.setter
    def end_date(self, value):
        self._end_date = value
        self.OnPropertyChanged("end_date")
