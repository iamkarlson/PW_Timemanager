from pyevent import *


from System.Collections.ObjectModel import *
from System.ComponentModel import *

class NotifyPropertyChangedBase(INotifyPropertyChanged):
        """
 
http://sdlsdk.codeplex.com/Thread/View.aspx?ThreadId=30322
 
        """
        PropertyChanged = None
        def __init__(self):
                (self.PropertyChanged, self._propertyChangedCaller) = make_event()
 
        def add_PropertyChanged(self, value):
                self.PropertyChanged += value
 
        def remove_PropertyChanged(self, value):
                self.PropertyChanged -= value
         
        def OnPropertyChanged(self, propertyName):
                self._propertyChangedCaller(self, PropertyChangedEventArgs(propertyName))
