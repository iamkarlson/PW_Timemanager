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
        def __init__(self,type_track,date):
            super(TrackedItem, self).__init__()
            self.type_track=type_track
            self.date=date

        def _jsonSupport( *args ):
            def default(self, xObject):
                return { 'type_track':  xObject.type_track, 'date': xObject.date }

            def objectHook( obj ):
                if 'type' not in obj:
                    return obj
                if obj[ 'type' ] != 'TrackedItem':
                    return obj
                return TrackedItem(obj.type_track, obj.date )
            json.JSONEncoder.default = default
            json._default_decoder = json.JSONDecoder( object_hook = objectHook )
        _jsonSupport()

        @property
        def type_track(self):
                return self._type_track
 
        @type_track.setter
        def type_track(self, value):
                self._type_track = value
                self.OnPropertyChanged("type_track")
        @property
        def date(self):
                return self._date
 
        @date.setter
        def date(self, value):
                self._date = value
                self.OnPropertyChanged("date")
