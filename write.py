import os

class Data:
    def __init__(self,filepath,date,time,switch):
        self.filepath=filepath
        self.date=date    # only 'yes' or 'no' is inside the variable in the form of string
        self.time=time    # only 'yes' or 'no' is inside the variable in the form of string
        self.switch=switch    # 'yes' or 'no' is there inside the variable in the form of string
                              # it is for whether the application will run in ghe background or not

    def openfile(self):

        os.mkdir(r'C:\screen_capture_USS')    # making directory in C
                                              # drive for storing the text file for settings

        self.file=open(r'C:\screen_capture_USS\screen_capture_settings.txt','w')
        self.file.close()

    def write_date(self):    # setting for - whether date will be shown or not
        self.file=open(r'C:\sreen_capture_settings.txt','a')
        self.file.write(self.date)
        self.file.close()

    def write_time(self):    # setting for - whether time will be shown or not
        self.file=open('C:\sreen_capture_settings.txt','a')
        self.file.write(self.time)
        self.file.close()

    def write_switch(self):    # setting for - whether the software will run in background or not
        self.file=open(r'C:\sreen_capture_settings.txt','a')
        self.file.write(self.time)
        self.file.close()

    def write_filepath(self):    # setting for - file path will be written in the file
        self.file=open(r'C:\sreen_capture_settings.txt','a')
        self.file.write(self.time)
        self.file.close()