from dotNET_base.NotifyPropertyChangedBase import *

class TrackedItem(NotifyPropertyChangedBase):
        """
                use setter getter.
                IronPython 2.6 or later.
        """
        @property
        def type(self):
                return self._type
 
        @type.setter
        def type(self, value):
                self._type = value
                self.OnPropertyChanged("type")
        @property
        def date(self):
                return self._date
 
        @date.setter
        def date(self, value):
                self._date = value
                self.OnPropertyChanged("date")
