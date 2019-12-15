from PyQt5.QtWidgets import QPushButton,QMainWindow,QApplication,QWidget,QMessageBox,\
    QLabel,QLineEdit,QCheckBox
from PyQt5 import QtGui
import sys
from write import Data

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.move(520,200)
        self.resize(800,500)
        self.label()
        self.lineedit()
        self.pushbutton()
        self.checkbox()
        self.show()

    def pushbutton(self):
        self.btn_selectdestination=QPushButton('...',self)
        self.btn_selectdestination.resize(30,30)
        self.btn_selectdestination.move(690,190)
        self.btn_selectdestination.clicked.connect(self.vacant)

    def label(self):
        self.lbl_destination=QLabel('Select the destination folder - ',self)
        self.lbl_destination.setFont(QtGui.QFont('SansSerif',12))
        self.lbl_destination.move(80,150)

        self.lbl_ques=QLabel('Do you want date and time as your file name ?',self)
        self.lbl_ques.setFont(QtGui.QFont('SansSerif',12))
        self.lbl_ques.move(80,250)

        self.lbl_date = QLabel('Date - ', self)
        self.lbl_date.setFont(QtGui.QFont('SansSerif', 12))
        self.lbl_date.move(80, 290)

        self.lbl_time = QLabel('Time - ', self)
        self.lbl_time.setFont(QtGui.QFont('SansSerif', 12))
        self.lbl_time.move(80, 330)

    def lineedit(self):
        self.le_destination=QLineEdit(self)
        self.le_destination.resize(600,35)
        self.le_destination.move(80,190)
        self.le_destination.setFont(QtGui.QFont('SanssSerif',10))
        self.le_destination.setText('Paste the destination folder path here.')

    def checkbox(self):
        self.cb_date_yes=QCheckBox('Yes',self)
        self.cb_date_yes.move(180,290)
        self.cb_date_yes.setFont(QtGui.QFont('SansSerif',10))
        self.cb_date_yes.toggle()

        self.cb_date_no=QCheckBox('No',self)
        self.cb_date_no.move(360,290)
        self.cb_date_no.setFont(QtGui.QFont('SansSerif',10))

        self.cb_time_yes = QCheckBox('Yes', self)
        self.cb_time_yes.move(180, 330)
        self.cb_time_yes.setFont(QtGui.QFont('SansSerif', 10))
        self.cb_time_yes.toggle()

        self.cb_time_no = QCheckBox('No', self)
        self.cb_time_no.move(360, 330)
        self.cb_time_no.setFont(QtGui.QFont('SansSerif', 10))

        self.cb_opendir=QCheckBox('Open the folder',self)
        self.cb_opendir.move(80,380)
        self.cb_opendir.setFont(QtGui.QFont('SansSerif',10))

        self.cb_activation=QCheckBox('Activate the software to take screen shots.',self)
        self.cb_activation.move(80,420)
        self.cb_activation.setFont(QtGui.QFont('SansSerif',10))

        self.cb_date_yes.stateChanged.connect(lambda:self.checkbox_operation('date_yes'))
        self.cb_date_no.stateChanged.connect(lambda:self.checkbox_operation('date_no'))
        self.cb_time_yes.stateChanged.connect(lambda:self.checkbox_operation('time_yes'))
        self.cb_time_no.stateChanged.connect(lambda:self.checkbox_operation('time_no'))

    def checkbox_operation(self,object):
        if object=='date_yes':
            if self.cb_date_yes.isChecked()==True:
                self.cb_date_no.setChecked(False)
            else:
                self.cb_date_no.setChecked(True)

        elif object=='date_no':
            if self.cb_date_no.isChecked()==True:
                self.cb_date_yes.setChecked(False)
            else:
                self.cb_date_yes.setChecked(True)

        elif object=='time_yes':
            if self.cb_time_yes.isChecked()==True:
                self.cb_time_no.setChecked(False)
            else:
                self.cb_time_no.setChecked(True)

        elif object=='time_no':
            if self.cb_time_no.isChecked()==True:
                self.cb_time_yes.setChecked(False)
            else:
                self.cb_time_yes.setChecked(True)

    def vacant(self):
        if self.cb_date_yes.isChecked()==True:
            self.cb_date_no.setChecked(False)

    def export(self):

        try:
            if self.cb_activation.isChecked()==True:

                if self.cb_date_yes.isChecked()==True:    # for date
                    self.cb_date='yes'
                else:
                    self.cb_date='no'

                if self.cb_time_yes.isChecked()==True:    # for time
                    self.cb_time='yes'
                else:
                    self.cb_time='no'

            elif self.cb_activation.isChecked()==False:
                pass

        except Exception:
            QMessageBox.about(self,'Error','Something went wrong. Please fill all the required fields properly.')

        obj1=Data(1,2,3,4)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Window()
    sys.exit(app.exec_())