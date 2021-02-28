import smtplib
import ssl

class MailOperations:
    def __init__(self, password, email):
        self.portSSL = 465
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = email
        self.password = password

    def send_email(self, subject, text, receiver_email):
        message = """\
Subject: {}

{}""".format(subject, text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.portSSL, context=context) as server:
            server.login(self.sender_email, self.password)
            print("Login successful")
            server.sendmail(self.sender_email, receiver_email, message)
            print("Message sent")