from json import dumps

class Controller:
    
    def __init__(self,model):
        self.m = model
    
    def setView(self,view):
        self.v = view
    
    def setRelations(self):
        self.v.licenseGenerator.btnEncrypt.clicked.connect(self.v.licenseGenerator.disableAll)
        self.v.licenseGenerator.btnEncrypt.clicked.connect(self.encrypt)
        self.v.licenseGenerator.btnEncrypt.clicked.connect(self.v.licenseGenerator.enableAll)
        self.v.licenseGenerator.btnDecrypt.clicked.connect(self.v.licenseGenerator.disableAll)
        self.v.licenseGenerator.btnDecrypt.clicked.connect(self.decrypt)
        self.v.licenseGenerator.btnDecrypt.clicked.connect(self.v.licenseGenerator.enableAll)
        self.v.licenseGenerator.btnSend.clicked.connect(self.v.licenseGenerator.disableAll)
        self.v.licenseGenerator.btnSend.clicked.connect(self.send)
        self.v.licenseGenerator.btnSend.clicked.connect(self.v.licenseGenerator.enableAll)
    
    def encrypt(self):
        self.v.licenseGenerator.fieldLicense1.clear()
        self.v.licenseGenerator.fieldLicense2.clear()
        license = {
            "email":self.v.licenseGenerator.fieldEmail.text(),
            "blueprint":self.v.licenseGenerator.fieldBlueprint.text(),
            "expire-date":self.v.licenseGenerator.expireDate.selectedDate().toString("dd.MM.yyyy")
        }
        if not self.m.mailbox.validateEmail(license["email"]):
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":"Client email is invalid!",
                "details":self.v.licenseGenerator.fieldEmail.text()})
        if not len(license["blueprint"].strip()):
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":"Blueprint field is empty!",
                "details":self.v.licenseGenerator.fieldBlueprint.text()})
        private = dumps(license)
        public = self.m.licenseManager.newLicense(private.encode())
        self.v.licenseGenerator.fieldLicense1.appendPlainText(private)
        self.v.licenseGenerator.fieldLicense2.appendPlainText(public)
    
    def decrypt(self):
        public = self.v.licenseGenerator.fieldLicense2.toPlainText().strip()
        if not len(public):
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":"Public license field is empty!"})
        self.v.licenseGenerator.fieldLicense1.clear()
        private = self.m.licenseManager.restoreLicense(public.encode())
        if not private[0]:
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":private[1],
                "details":public})
        self.v.licenseGenerator.fieldLicense1.appendPlainText(private[1])
        
    def send(self):
        clientName = self.v.licenseGenerator.fieldName.text()
        clientEmail = self.v.licenseGenerator.fieldEmail.text()
        clientLicense = self.v.licenseGenerator.fieldLicense2.toPlainText()
        if not len(clientLicense.strip()):
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":"Client name field is empty!"})
        if not self.m.mailbox.validateEmail(clientEmail):
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":"Client email is invalid!",
                "details":clientEmail})
        if not len(clientLicense.strip()):
            return self.v.notification({
                "type":"error",
                "title":"License Genarator",
                "text":"License field is empty!"})
        response = self.m.mailbox.sendNewLicense(clientName,clientEmail,clientLicense)
        if response["state"]:
            return self.v.notification({
                "type":"",
                "title":"Congratulation!",
                "text":"New license has been sent successfully!"})
        return self.v.notification({
            "type":"error",
            "title":"Sorry!",
            "text":"New license has not been sent!",
            "details":response["message"]})
    
    def start(self):
        self.setRelations()
        self.v.licenseGenerator.setupUI()