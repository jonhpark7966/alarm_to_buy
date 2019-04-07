#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText

from alarm.sender import Sender

class MailSender(Sender):
    def __init__(self, sender, passwd):
        self.sender_ = sender
        self.passwd_ = passwd

    def send(self, title, contents):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(self.sender_, self.passwd_)
        msg = MIMEText(contents)
        msg['Subject'] = title

        for to in self.addressees_:
            msg['To'] = to
            smtp.sendmail(self.sender_, to, msg.as_string())

        smtp.quit()
