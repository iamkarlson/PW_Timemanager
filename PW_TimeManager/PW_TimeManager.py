import wpf
import datetime
import pyevent

from System.Windows import Application, Window

from System.Windows.Controls import *
from System.Collections.ObjectModel import *
from System.ComponentModel import *


from ViewModelBase import ViewModelBase
from Command import Command

from Storage.FileStorage import *

from TrackedItemClass import *
from PointClass import *

def OpenDialogFile():
        LoadFile()
        pass
def LoadFile():
        list = []
        f = open('d:\\test strings file.txt')
        lines = f.readlines()
        f.close()
        pass





class MyWindow(Window):
        def __init__(self):
                wpf.LoadComponent(self, 'PW_TimeManager.xaml')
                self.data = ObservableCollection[TrackedItem]()
                self.listView.ItemsSource = self.data
                self.jsn = data_load('d:\\dates.json')
                for point in self.jsn['points']:
                        new_date = TrackedItem()
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
                self.new_date_add(self.jsn,point)

        def StopButton_Click(self, sender, e):
                now_time = str(datetime.datetime.now())
                type = "stop"
                point = Point(type,now_time)
                self.new_date_add(self.jsn,point)

        def new_date_add(self, jsn,point):
                data_add(self.jsn, point.date, point.type)
                write_json_to_file(self.jsn)
                new_date = TrackedItem()
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
