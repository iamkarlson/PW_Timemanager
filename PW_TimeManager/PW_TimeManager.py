import wpf
import datetime

import time

import Helpers

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
        
        self.Edit_Click_Command = Command(self.Edit_Click)

        self.data_worker = FileStorage('d:\\dates.json')
        self.data_worker.data_load()
        self._current_task = None
        latest_element = self.data_worker.get_latest_element()
        if(latest_element != None ):
            if(latest_element.type_track != "complete"):
                self._current_task = latest_element

        self.listView.ItemsSource = self.data_worker.get_tracked_items()
        self.grid1.DataContext = self._current_task 
    def __getattr__(self, item):
        #Maps values to attributes.Only called if there *isn't* an attribute with this name
        return self.Root.FindName(item)

    def StartButton_Click(self, sender, e):
        if self._current_task:
            pass
        else:
            self._current_task = TrackedItem()
            self._current_task.date_start = str(datetime.datetime.now())
            self._current_task.type_track = "in progress"
            new_task = self._current_task
            self.new_date_add(new_task)

    def StopButton_Click(self, sender, e):
        if not self._current_task:
            pass
        else:
            self._current_task.date_end = str(datetime.datetime.now())
            self._current_task.type_track = "complete"
            task = self._current_task
            self.new_date_add(task)
            self._current_task = None

    def bind_values(self):
        self.listView.Items.Refresh()
        self.grid1.DataContext = self.data_worker.get_latest_element()

    def new_date_add(self, point):
        self.data_worker.data_update(point)
        self.bind_values()
        element = self.data_worker.get_latest_element()
        #date = datetime.datetime.strptime(element.date_start, "%Y-%m-%d %H:%M:%S.%f")
        self.CurrentTaskStart.Text = element.date_start
        self.CurrentTaskEnd.Text = element.date_end


    def MenuItem_Open_Click(self, sender, e):
        OpenDialogFile()

    def Edit_Click(self, id):
        task = self.data_worker.get_tracked_item_by_id(id)
        self.grid1.DataContext = task

    def Exit_Click(self, sender, e):
        app.Exit
        app.Shutdown()

    def MenuItem_Click(self, sender, e):
        pass

if __name__ == '__main__':
        app = Application()
        window = MyWindow()
        app.Run(window)
