import smtplib, ssl
import getpass

class EmailSender:
    '''
    Sends emails from gmail smtp server. Must enable "Less secure app access" in gmail account to work
    '''
    def __init__(self, sender_email):
        self._sender_email = sender_email
        self.port = 465  # For SSL
        print("Type your password and press enter: ")
        self.password = getpass.getpass()
        # Create a secure SSL context
        self.context = ssl.create_default_context()
        
    def send_email(self, message, receiver_email):
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self._sender_email, self.password)
            server.sendmail(self._sender_email, receiver_email, message)

