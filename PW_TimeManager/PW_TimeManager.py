import wpf
import datetime
 
from pyevent import *
from ViewModelBase import ViewModelBase
from Command import Command
from System.Windows import Application, Window

from System.Windows.Controls import *
from System.Collections.ObjectModel import *
from System.ComponentModel import *


from WriteToFileJson import *

def OpenDialogFile():
    LoadFile()
    pass
def LoadFile():
    list = []
    f = open('d:\\test strings file.txt')
    lines = f.readlines()
    f.close()
    pass

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

class DateItem(NotifyPropertyChangedBase):
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



class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'PW_TimeManager.xaml')
        self.data = ObservableCollection[DateItem]()
        self.listView.ItemsSource = self.data
        self.jsn = json_load('d:\\dates.json')
        for point in self.jsn['points']:
            new_date = DateItem()
            new_date.type = point['type']
            new_date.date = point['date']
            self.data.Add(new_date)

    def __getattr__(self, item):
        #Maps values to attributes.Only called if there *isn't* an attribute with this name
        return self.Root.FindName(item)
    def StartButton_Click(self, sender, e):
        now_time = str(datetime.datetime.now())
        type = "start"
        point = Point(type,now_time)
        self.jsn_add(self.jsn,point)

    def StopButton_Click(self, sender, e):
        now_time = str(datetime.datetime.now())
        type = "stop"
        point = Point(type,now_time)
        self.jsn_add(self.jsn,point)

    def jsn_add(self, jsn,point):
        json_add(self.jsn, point.date, point.type)
        write_json_to_file(self.jsn)
        new_date = DateItem()
        new_date.type = point.type
        new_date.date = point.date
        self.data.Add(new_date)

    def MenuItem_Open_Click(self, sender, e):
        OpenDialogFile()


class ViewModel(ViewModelBase):
    def __init__(self):
        ViewModelBase.__init__(self)
        self.FirstName = "Joe"
        self.Surname = "Smith"
        self.ChangeCommand = Command(self.change)
    def change(self):
        self.FirstName = "Dave"
        self.Surname = "Brown"
        self.RaisePropertyChanged("FirstName")
        self.RaisePropertyChanged("Surname")


if __name__ == '__main__':
    app = Application()
    window = MyWindow()
    window.grid1.DataContext = ViewModel()
    app.Run(window)
