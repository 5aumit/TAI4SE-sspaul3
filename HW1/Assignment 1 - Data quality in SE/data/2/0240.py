import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFormLayout, QLineEdit

from PyQt5.QtWidgets import QSizePolicy, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt

from validator.StudentValidator import StudentValidator
from dao.StudentDAOSqliteImpl import StudentDAOSqliteImpl
from model.Student import Student



class StudentSaveWindow(QDialog):
    """
    With this class QDialog for adding new model.Student into database is shown.
     
    """
    def __init__(self, tableWidget):
        """
        constructor 
        
        :param tableWidget: QTableWidget 
        """
        super().__init__()
        self.tableWidget = tableWidget
        self.title = "Save New Student"
        self.left , self.top , self.width , self.height = 10, 10, 500, 500
        self.validator = StudentValidator()
        self.dao = StudentDAOSqliteImpl()
        self.initGUI()



    def initGUI(self):
        """
        initializes GUI
        :return: 
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top, self.width , self.height)
        self.setWindowModality(Qt.ApplicationModal)
        self.addComponents()
        self.registerEvents()




    def addComponents(self):
        """
        sets the mainLayout for this class and adds components into it.
        :return: 
        """
        self.mainLayout = QFormLayout()
        self.setLayout(self.mainLayout)
        # title
        self.lblTitle = QLabel("Save New Student")
        self.lblEmpty = QLabel()

        # enrolmentNumber
        self.lblEnrolmentNumber = QLabel("EnrolmentNumber: ")
        self.editEnrolmentNumber = QLineEdit()

        # firstName
        self.lblFirstName = QLabel("FirstName: ")
        self.editFirstName = QLineEdit()


        # lastName
        self.lblLastName = QLabel("LastName: ")
        self.editLastName = QLineEdit()

        # dob
        self.lblDob = QLabel("DateOfBirth: ")
        self.editDob = QLineEdit()

        # faculty
        self.lblFaculty = QLabel("Faculty: ")
        self.editFaculty = QLineEdit()

        # email
        self.lblEmail = QLabel("Email: ")
        self.editEmail = QLineEdit()

        # buttons
        self.btnSave = QPushButton("Save")
        self.btnCancel = QPushButton("Cancel")

        # add all rows to mainLayout
        self.mainLayout.addRow(self.lblEmpty, self.lblTitle)
        self.mainLayout.addRow(self.lblEnrolmentNumber, self.editEnrolmentNumber)
        self.mainLayout.addRow(self.lblFirstName, self.editFirstName)
        self.mainLayout.addRow(self.lblLastName, self.editLastName)
        self.mainLayout.addRow(self.lblDob, self.editDob)
        self.mainLayout.addRow(self.lblFaculty, self.editFaculty)
        self.mainLayout.addRow(self.lblEmail, self.editEmail)
        self.mainLayout.addRow(self.btnSave, self.btnCancel)

    def registerEvents(self):
        """
        registers events
        :return: 
        """
        self.btnSave.clicked.connect(self.onBtnSaveClicked)
        self.btnCancel.clicked.connect(self.onBtnCancelClicked)




    @pyqtSlot()
    def onBtnSaveClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnSave is clicked.
        :return: 
        """
        try:
            errors = []
            enrolmentNumber = self.editEnrolmentNumber.text()
            firstName = self.editFirstName.text()
            lastName = self.editLastName.text()
            dob = self.editDob.text()
            faculty = self.editFaculty.text()
            email = self.editEmail.text()
            if not self.validator.validateEnrolmentNumber(enrolmentNumber):
                errors.append("enrolmentNumber is incorrect.")

            if not self.validator.validateFirstName(firstName):
                errors.append("firstName is incorrect.")

            if not self.validator.validateLastName(lastName):
                errors.append("lastName is incorrect.")

            if not self.validator.validateDob(dob):
                errors.append("DateOfBirth is incorrect.")

            if not self.validator.validateFaculty(faculty):
                errors.append("Faculty is incorrect.")

            if not self.validator.validateEmail(email):
                errors.append("Email is incorrect.")

            if len(errors) > 0 :
                raise Exception("\n".join(errors))


            ret = self.dao.save(Student(enrolmentNumber, firstName, lastName,
                                  dob, faculty, email))

            if ret :
                raise Exception(ret)


            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(enrolmentNumber))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(firstName))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(lastName))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(dob))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(faculty))
            self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(email))

            self.close()

        except Exception as err:

            QMessageBox.critical(self, "<<Error>>", str(err))





    @pyqtSlot()
    def onBtnCancelClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnCancel is clicked.
        :return: 
        """
        self.close()
