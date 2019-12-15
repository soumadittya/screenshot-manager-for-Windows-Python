from PyQt5.QtWidgets import QWidget,QMessageBox,QMainWindow,\
    QLineEdit,QPushButton,QApplication,QLabel,QFileDialog
from PyQt5 import QtGui
import os
import shutil
import sys

class SaveDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700,250)
        self.move(540,190)
        self.setWindowTitle('Save Screenshot')
        self.button()
        self.lineedit()
        self.label()
        self.show()

    def button(self):
        self.btn_save=QPushButton('Save',self)
        self.btn_save.move(80,190)
        self.btn_save.resize(150,40)
        self.btn_save.clicked.connect(self.save)

        self.btn_cancel=QPushButton('Cancel',self)
        self.btn_cancel.move(470,190)
        self.btn_cancel.resize(150,40)
        self.btn_cancel.clicked.connect(self.cancel)

        self.btn_path=QPushButton('...',self)
        self.btn_path.move(630,140)
        self.btn_path.resize(30,30)
        self.btn_path.clicked.connect(self.select_path)

    def lineedit(self):
        self.le_name=QLineEdit('Type your file name.',self)
        self.le_name.move(80,60)
        self.le_name.resize(540,30)

        self.le_path=QLineEdit('Select your file path.',self)
        self.le_path.move(80,140)
        self.le_path.resize(540,30)

    def label(self):
        self.lbl_name=QLabel('Type name of the file - ',self)
        self.lbl_name.move(80,20)
        self.lbl_name.setFont(QtGui.QFont('SansSerif',10))

        self.lbl_path=QLabel('Select the path of the destination folder - ',self)
        self.lbl_path.move(80,100)
        self.lbl_path.setFont(QtGui.QFont('SansSerif',10))

    def save(self):

        self.path=self.le_path.text()
        self.name=self.le_name.text()
        shutil.move('C:/screen_capture_USS/current_screenshot.png',self.path+'/'+self.name+'.png')

    def select_path(self):

        try:
            self.le_path.setText(str(QFileDialog.getExistingDirectory(self,'SelectDrectory')))

        except Exception:
            pass

    def cancel(self):
        try:
            os.remove('C:/screen_capture_USS/current_screenshot.png')

        except Exception:
            pass
        import capture
        self.destroy()

    def operation(self):
        print(self.a)

def main():
    app = QApplication(sys.argv)
    w = SaveDialog()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()