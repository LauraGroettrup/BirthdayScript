from smtplib import SMTP
from email.message import EmailMessage
from datetime import date

# file with email access data, first line email addresse, second line email password
USERDATAFILE = 'EmailAccData.txt'
file = open(USERDATAFILE, 'r')
SMTP_USER = file.readline().rstrip()
SMTP_PASS = file.readline().rstrip()
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
persons = []

def calculate_age(born):
    today = date.today()
    return today.year - born.year


# gets a list with all person who should get an email
# sends email to the birthdayperson, and to yourself
def sendMails (persons):
    for person in persons:
        # email to birthdayperson
        msgForBirthday = EmailMessage()
        msgForBirthday.set_content(makeBirthdayMsg(person))
        msgForBirthday['Subject'] = 'Geburtstagsgrüße'
        msgForBirthday['FROM'] = SMTP_USER
        msgForBirthday['To'] = person.email
        try:
            with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USER, SMTP_PASS)
                smtp.send_message(msgForBirthday)
        except Exception as e:
            print('Something went wrong')
            print(e)
            exit(1)
		#email to yourself
        msgAsReminder = EmailMessage()
        msgAsReminder.set_content('Du hast ' + person.firstname + ' zum Geburtstag gratuliert.')
        msgAsReminder['Subject'] = 'Automatische Geburtstagsgrüße wurden versandt.'
        msgAsReminder['FROM'] = SMTP_USER
        msgAsReminder['To'] = SMTP_USER
        try:
            with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USER, SMTP_PASS)
                smtp.send_message(msgAsReminder)
        except Exception as e:
            print('Something went wrong')
            print(e)
            exit(1)
#class Person:
#    def __init__(self, firstname, lastname, birthday, email):
#        self.firstname = firstname
#        self.lastname = lastname
#        self.birthday = birthday
#        self.email = email
        
#test = Person('Laura','G','28-24-1995','laura@groettrup.com')
#persons.append(test)
#sendMails(persons)