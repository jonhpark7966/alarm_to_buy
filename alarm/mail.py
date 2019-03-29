#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText

class MailSender:
    def __init__(self):
        self.mailing_list_ = []
        self.sender_ = 'skylarknews0610@gmail.com'
        self.passwd_ = 'passwd'

    def addMailingList(self, mailing_list):
        self.mailing_list_.extend(mailing_list)

    def sendMail(self, title, contents):

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(self.sender_, self.passwd_)

        msg = MIMEText(contents)
        msg['Subject'] = title

        for to in self.mailing_list_:
            msg['To'] = to
            smtp.sendmail(self.sender_, to, msg.as_string())

        smtp.quit()
