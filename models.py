from json import dumps
from email_validator import validate_email, EmailNotValidError
from emails import Message
from rsa import decrypt, encrypt, PrivateKey, PublicKey, DecryptionError
from binascii import hexlify, unhexlify, Error

class LicenseManager:
    
    keyPrivate = ()
    
    keyPublic = ()
    
    def encrypt(self,bytes):
        return hexlify(encrypt(bytes,self.keyPublic))
    
    def decrypt(self,bytes):
        try:
            return True,decrypt(unhexlify(bytes),self.keyPrivate)
        except DecryptionError:
            return False,"It\'s impossible to decrypt a pubic data!"
        except Error:
            return False,"Odd-length string. Check HEX string (00)!"
            
            
    def newLicense(self,license):
        return self.encrypt(license).decode()
    
    def restoreLicense(self,license):
        license = self.decrypt(license)
        if license[0]:
            return license[0],license[1].decode()
        return license

class Mailbox:
    
    server = {'host':'smtp.gmail.com',
              'port':465,
              'ssl':True,
              'user':"@gmail.com",
              'password':""}
    
    def validateEmail(self,email):
        try:
            return validate_email(email).email
        except EmailNotValidError:
            return False
    
    def newLicenseResponse(self,clientName,clientEmail,clientLicense):
        html = "".join(["<h1>Hi {}!</h1>",
                        "<p>Use the next data to activate your app:</p>",
                        "<p><b>Email: </b><span>{}</span></p>",
                        "<p><b>License: </b><span>{}</span></p>",
                        "<br><i><b>PS:</b>If you have any question, ",
                        "use email {} for feedback!</i>"])
        return html.format(clientName,clientEmail,clientLicense,self.server["user"])
    
    def sendNewLicense(self,clientName,clientEmail,clientLicense):
        message = Message()
        message.subject = "New License Response"
        message.mail_from = self.server["user"]
        message.mail_to = clientEmail
        message.html = self.newLicenseResponse(clientName,clientEmail,clientLicense)
        response = message.send(to=(clientName,clientEmail),smtp=self.server)
        return {"state":response.status_code in [250,],"message":message.as_string()}



class Model:
    
    def __init__(self):
        self.mailbox = Mailbox()
        self.licenseManager = LicenseManager()
