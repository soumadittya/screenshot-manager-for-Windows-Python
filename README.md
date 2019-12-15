# screenshot-manager-for-Windows-Python
screenshots in windows can be taken and managed conveniently because of the customization it provides

Description - 

With this application you can customize the following - 

1. Default directory of screenhots taken.
2. Whether to prompt for the file path after every single screenshot taken.

Working and Installation - 

After the installation you have to open the application and set the above mentioned parameters 
and activate the the sofatware. After the activation it will make a shortcut in the Windows startup
and it will start running in the background and then the application can be closed. After this every
single time the user boots his/ her computer the software starts running in the background unless and
until the user deactivates the software.

Explanation for the python files - 

1. capture.py - there is a key listener which keeps on running and as soon as the user hits the 
'prt scr' key it takes a screen shot  and and then creates a folder by the name of today's date 
and saves the screenshot in that folder or opens a gui
window ('savefile_gui.py') which prompts for the file path.

2. write - this file is always accessed by the 'settings.py' file (gui window from where the user
can make all the customization) and it is used to store the settings information in text files.
