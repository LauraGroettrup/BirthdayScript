import csv
import re
import datetime

patternNoYear = ' --[^*]*'
patternToReplace = ' -'
allContacts = []

class Person:
    def __init__(self, firstname, lastname, birthday, email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.email = email

def readContacts():
    firstLine = True
    with open('contacts.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # Skip Header
            if (firstLine):
                firstLine = False
            # Each entry of the contacts becomes a person
            else:
                # row[1]=firstname row[3]=lastname row[14]=birthday row[30]=email
                date = row [14]
                # Must have attributes: first name, email, birthday
                if (row[1]!= ' ' or date!=' ' or row[30]!=' '):
                    if re.match(patternNoYear, date):
                        date = re.sub(patternToReplace, '0000', date)
                    person = Person(row[1], row[3], date, row[30])
                    allContacts.append(person)              
    return allContacts

# For testing    
def printContacts(allContacts):
    for person in allContacts:
        print(person.firstname + ' ' + person.lastname + ' ' + person.birthday + ' ' + person.email)