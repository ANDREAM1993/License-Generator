from datetime import datetime
from os.path import dirname
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton,\
                            QDesktopWidget, QGridLayout, QMessageBox, \
                            QCalendarWidget, QPlainTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QDate

class LicenseGenerator:
    
    def __init__(self):
        self.icon = QIcon("/".join([dirname(__file__),"logo.jpg"]))
        self.window = QWidget()
        self.window.setWindowIcon(self.icon)
        self.window.setWindowTitle("License Generator")
        self.window.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.window.setContentsMargins(10,10,10,10)
        self.window.setFont(QFont("Courier",10,0,False))
        # main layout;
        self.windowLayout = QGridLayout()
        self.windowLayout.setContentsMargins(0,0,0,0)
        self.windowLayout.setSpacing(10)
        self.windowLayout.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.windowLayout.setColumnMinimumWidth(0,100)
        self.windowLayout.setColumnMinimumWidth(1,100)
        self.windowLayout.setColumnMinimumWidth(2,100)
        self.windowLayout.setColumnMinimumWidth(3,100)
        self.windowLayout.setColumnMinimumWidth(4,100)
        self.windowLayout.setColumnMinimumWidth(5,100)
        self.window.setLayout(self.windowLayout)
        # client name field;
        box = QFormLayout()
        box.setContentsMargins(0,0,0,0)
        box.setSpacing(10)
        box.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.fieldName = QLineEdit()
        self.fieldName.setClearButtonEnabled(True)
        box.addRow("Client Name:",self.fieldName)
        self.windowLayout.addLayout(box,0,0,1,3,Qt.AlignHCenter|Qt.AlignVCenter)
        # client email field;
        box = QFormLayout()
        box.setContentsMargins(0,0,0,0)
        box.setSpacing(10)
        box.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.fieldEmail = QLineEdit()
        self.fieldEmail.setClearButtonEnabled(True)
        box.addRow("Client Email:",self.fieldEmail)
        self.windowLayout.addLayout(box,0,3,1,3,Qt.AlignHCenter|Qt.AlignVCenter)
        # client blueprint field;
        box = QFormLayout()
        box.setContentsMargins(0,0,0,0)
        box.setSpacing(10)
        box.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.fieldBlueprint = QLineEdit()
        self.fieldBlueprint.setClearButtonEnabled(True)
        box.addRow("Blueprint:",self.fieldBlueprint)
        self.windowLayout.addLayout(box,1,0,1,6,Qt.AlignHCenter|Qt.AlignVCenter)
        # expiration date field;
        self.expireDate = QCalendarWidget()
        self.expireDate.setFixedWidth(200)
        self.expireDate.setToolTip("Select expiration date for license")
        self.windowLayout.addWidget(self.expireDate,2,0,1,2,Qt.AlignHCenter|Qt.AlignVCenter)
        # private license field;
        self.fieldLicense1 = QPlainTextEdit()
        self.fieldLicense1.setPlaceholderText("Private data")
        self.fieldLicense1.setToolTip("Send this string to client")
        self.fieldLicense1.setFixedWidth(200)
        self.fieldLicense1.setCenterOnScroll(True)
        self.windowLayout.addWidget(self.fieldLicense1,2,2,1,2,Qt.AlignHCenter|Qt.AlignVCenter)
        # public license field;
        self.fieldLicense2 = QPlainTextEdit()
        self.fieldLicense2.setPlaceholderText("Public data")
        self.fieldLicense2.setToolTip("Send this string to client")
        self.fieldLicense2.setFixedWidth(200)
        self.fieldLicense2.setCenterOnScroll(True)
        self.windowLayout.addWidget(self.fieldLicense2,2,4,1,2,Qt.AlignHCenter|Qt.AlignVCenter)
        # send button;
        self.btnSend = QPushButton("SEND")
        self.btnSend.setFixedWidth(100)
        self.btnSend.setToolTip("Click to send encrypted license to client")
        self.windowLayout.addWidget(self.btnSend,3,0,1,2,Qt.AlignHCenter|Qt.AlignVCenter)
        # generate button;
        self.btnEncrypt = QPushButton("ENCRYPT")
        self.btnEncrypt.setFixedWidth(100)
        self.btnEncrypt.setToolTip("Click to encrypt a license")
        self.windowLayout.addWidget(self.btnEncrypt,3,2,1,2,Qt.AlignHCenter|Qt.AlignVCenter)
        # generate button;
        self.btnDecrypt = QPushButton("DECRYPT")
        self.btnDecrypt.setFixedWidth(100)
        self.btnDecrypt.setToolTip("Click to decrypt a license")
        self.windowLayout.addWidget(self.btnDecrypt,3,4,1,2,Qt.AlignHCenter|Qt.AlignVCenter)
        
    def setupUI(self):
        # setup UI;
        currentDate = datetime.now()
        currentDate = QDate(currentDate.year,currentDate.month,currentDate.day)
        self.expireDate.setSelectedDate(currentDate)
        # show window;
        display = QDesktopWidget()
        dw = display.screen(0).width()
        dh = display.screen(0).height()
        x0 = (dw - self.window.width()) // 2
        y0 = (dh - self.window.height()) // 2
        self.window.move(x0,y0)
        self.window.show()
    
    def disableAll(self):
        self.fieldEmail.setDisabled(True)
        self.fieldBlueprint.setDisabled(True)
        self.expireDate.setDisabled(True)
        self.fieldLicense1.setDisabled(True)
        self.fieldLicense2.setDisabled(True)
        self.btnEncrypt.setDisabled(True)
        self.btnDecrypt.setDisabled(True)
        self.btnSend.setDisabled(True)
    
    def enableAll(self):
        self.fieldEmail.setEnabled(True)
        self.fieldBlueprint.setEnabled(True)
        self.expireDate.setEnabled(True)
        self.fieldLicense1.setEnabled(True)
        self.fieldLicense2.setEnabled(True)
        self.btnEncrypt.setEnabled(True)
        self.btnDecrypt.setEnabled(True)
        self.btnSend.setEnabled(True)
        
class View:
    
    def __init__(self,model,controller):
        self.m = model
        self.c = controller
        self.c.setView(self)
        self.licenseGenerator = LicenseGenerator()
        self.settestdata()
        
    def connector(self,model,controller):
        self.m = model
        self.c = controller
    
    def settestdata(self):
        self.licenseGenerator.fieldName.setText("")
        self.licenseGenerator.fieldEmail.setText("@ukr.net")
        self.licenseGenerator.fieldBlueprint.setText("")
    
    def notification(self,params=None):
        msg = QMessageBox()
        if not params:
            msg.setWindowTitle("ERROR")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Unexpected error found!")
        else:
            msg.setWindowTitle(params["title"])
            msg.setIcon(QMessageBox.Information)
            if params["type"] == "error":
                msg.setIcon(QMessageBox.Critical)
            msg.setText(params["text"])
            if "details" in params:
                msg.setDetailedText(params["details"])
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
