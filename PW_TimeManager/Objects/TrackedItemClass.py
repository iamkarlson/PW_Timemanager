from dotNET_base.NotifyPropertyChangedBase import *

import clr
import Helpers.clrtype as clrtype

import json

class TrackedItem(NotifyPropertyChangedBase):
    __metaclass__ = clrtype.ClrClass
    """
            use setter getter.
            IronPython 2.6 or later.
    """
    def __init__(self,type_track= None, start_date = None, end_date = None):
        super(TrackedItem, self).__init__()
        self.type_track=type_track
        self.start_date=start_date

    def _jsonSupport( *args ):
        def default(self, trackedObject):
            jsn = {}
            if(trackedObject.id != None):
                jsn['id']= trackedObject.id
            if(trackedObject.type_track != None):
                jsn['type_track']= trackedObject.type_track
            if(trackedObject.start_date != None):
                jsn['start_date']= trackedObject.start_date
            if(trackedObject.end_date != None):
                jsn['end_date']= trackedObject.end_date 
            return jsn

        def objectHook( obj ):
            if 'type' not in obj:
                return obj
            if obj[ 'type' ] != 'TrackedItem':
                return obj
            return TrackedItem(obj.type_track, obj.start_date )
        json.JSONEncoder.default = default
        json._default_decoder = json.JSONDecoder( object_hook = objectHook )
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
