from smtplib import SMTP
from email.message import EmailMessage
import datetime

SMTP_HOST = 'mail.gmx.net'
SMTP_PORT = 587

SMTP_USER = "ulrike.gartler@gmx.at"
SMTP_PASS = "IwidLG47mBadS."
yourName = "Ulrike"
        
        #read Userdata from file
            # email to birthdayperson
msgForBirthday = EmailMessage()
msgForBirthday.set_content("test")
msgForBirthday['Subject'] = 'Testgrüße'
msgForBirthday['FROM'] = SMTP_USER
msgForBirthday['To'] = "ulrike.gartler@gmx.at"
  
with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
          smtp.starttls()
          smtp.login(SMTP_USER, SMTP_PASS)
          smtp.send_message(msgForBirthday)
        