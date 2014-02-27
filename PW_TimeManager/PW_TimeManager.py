import wpf
import datetime

import Helpers.pyevent

from System.Windows import Application, Window

from System.Windows.Controls import *
from System.Collections.ObjectModel import *
from System.ComponentModel import *


#from ViewModelBase import ViewModelBase
from Helpers.Command import Command

from Storage.FileStorage import *


from Objects.TrackedItemClass import *

def OpenDialogFile():
        LoadFile()
        pass
def LoadFile():
        list = []
        f = open('d:\\test strings file.txt')
        #lines = f.readlines()
        #f.close()
        pass

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'PW_TimeManager.xaml')
        
        self.data_worker = FileStorage('d:\\dates.json')
        self.data_worker.data_load()

        self.listView.ItemsSource = self.data_worker.get_tracked_items()
        self.grid1.DataContext = self.data_worker.get_latest_element()

    def __getattr__(self, item):
        #Maps values to attributes.Only called if there *isn't* an attribute with this name
        return self.Root.FindName(item)
    def StartButton_Click(self, sender, e):
        now_time = str(datetime.datetime.now())
        type_track = "start"
        point = TrackedItem(type_track,now_time)
        self.new_date_add(point)

    def StopButton_Click(self, sender, e):
        now_time = str(datetime.datetime.now())
        type_track = "stop"
        point = TrackedItem(type_track,now_time)
        self.new_date_add(point)

    def new_date_add(self, point):
        self.data_worker.data_add(point)
        self.grid1.DataContext = self.data_worker.get_latest_element()

    def MenuItem_Open_Click(self, sender, e):
        OpenDialogFile()

if __name__ == '__main__':
        app = Application()
        window = MyWindow()
        #window.grid1.DataContext = ViewModel()
        app.Run(window)
