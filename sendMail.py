from smtplib import SMTP
from email.message import EmailMessage
import datetime

# file with email access data, first line email addresse, second line email password
USERDATAFILE = 'EmailAccData.txt'
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
YOURNAME = 'Ich'
persons = []

def calculateAge(born):
    today = date.today()
    return today.year - born.year
    
def makeBirthdayMessage(person):
    birthdayAsDate = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
    if (birthdayAsDate.year == 1111):
        msg = "Hallo " + person.firstname+ ",\nalles alles Gute zum Geburtstag! Lass dich feiern und ess viel Kuchen;)\nLiebe Grüße,\n" + YOURNAME
        return msg
    else:
        age = calculateAge(birthdayAsDate)
        ageStr = str(age) + '.'
        msg = "Hallo " + person.firstname+ ",\nalles alles Gute zum " + ageStr + "Geburtstag! Lass dich feiern und ess viel Kuchen;)\nLiebe Grüße,\n" + YOURNAME
		return msg
	
		
# gets a list with all person who should get an email
# sends email to the birthdayperson, and to yourself
def sendMails (persons):
    for person in persons:
        #read Userdata from file
        try:
            file = open(USERDATAFILE, 'r')
            SMTP_USER = file.readline().rstrip()
            SMTP_PASS = file.readline().rstrip()
            # email to birthdayperson
            msgForBirthday = EmailMessage()
            msgForBirthday.set_content(makeBirthdayMsg(person))
            msgForBirthday['Subject'] = 'Geburtstagsgrüße'
            msgForBirthday['FROM'] = SMTP_USER
            msgForBirthday['To'] = person.email
  
            with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USER, SMTP_PASS)
                smtp.send_message(msgForBirthday)
        
            #email to yourself
            msgAsReminder = EmailMessage()
            msgAsReminder.set_content('Du hast ' + person.firstname + ' zum Geburtstag gratuliert.')
            msgAsReminder['Subject'] = 'Automatische Geburtstagsgrüße wurden versandt.'
            msgAsReminder['FROM'] = SMTP_USER
            msgAsReminder['To'] = SMTP_USER
            
            with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USER, SMTP_PASS)
                smtp.send_message(msgAsReminder)
        except Exception as e:
            print('Something went wrong')
            print(e)
        finally:
            file.close()
            exit(1)