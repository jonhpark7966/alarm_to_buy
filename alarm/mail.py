#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('skylarknews0610@gmail.com', 'password')

msg = MIMEText("테스트")
msg['Subject'] = "test"
msg['To'] = "jonhpark7966@gmail.com"
smtp.sendmail('skylarknews0610@gmail.com', 'jonhpark7966@gmail.com', msg.as_string())

smtp.quit()
