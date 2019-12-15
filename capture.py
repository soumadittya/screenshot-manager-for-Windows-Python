from pyautogui import screenshot
from pynput.keyboard import Key, Listener
from datetime import date
import os

def read_default_file_path():    # it will read the default file path file

    default_file_path=''
    file=open('C:\screen_capture_USS\settings\default_file_path.txt','r')
    f=file.read()
    file.close()

    for alpha in f:
        if alpha=='\\':
            default_file_path=default_file_path+'/'
        else:
            default_file_path=default_file_path+alpha
    return default_file_path

def read_path_prompt():    # whether file will be saved in default
                           # or it will prompt after every screenshot
    path_prompt=''
    file=open('C:\screen_capture_USS\settings\path_prompt.txt','r')
    path_prompt=file.read()
    file.close()
    return path_prompt

def read_show_folder():    # file contains whether the default
                           # will open after taking each
                           # screenshot or not

    file=open('C:\screen_capture_USS\settings\show_folder.txt','r')
    show_folder=file.read()
    file.close()
    return show_folder

def final_operation():    # first checks whether the folder
                          # exists or not and then creates
                          # folder for every date
    boolean=os.path.exists(read_default_file_path()+'/'+date_calc())
    if boolean==True:
        screenshot(read_default_file_path()+'/'+date_calc()+'/'+capture_number()+'.png')
    elif boolean==False:
        os.mkdir(read_default_file_path()+'/'+date_calc())
        screenshot(read_default_file_path()+'/'+date_calc()+'/'+capture_number()+'.png')

def capture_number():
    file=open('C:/screen_capture_USS/data/capture_number.txt','r')
    f=file.read()
    file.close()

    increase=int(f)
    increase=increase+1

    file=open('C:/screen_capture_USS/data/capture_number.txt','w')
    file.write(str(increase))
    file.close()

    return increase()

def date_calc():
    today_date=date.today()
    return today_date.strftime('%Y-%m-%d')

def take_screenshot(key):
    var='{0}'.format(key)
    if var=='Key.print_screen':
        if read_path_prompt()=='Yes':
            screenshot('C:/screen_capture_USS/current_screenshot.png')


        else:

            final_operation()
            if read_show_folder()=='Yes':
                os.startfile(read_default_file_path()+'/'+date_calc())

with Listener(
        on_press=take_screenshot) as listener:
            listener.join()