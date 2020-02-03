import csv
import re
import datetime
import os.path
import time

patternNoYear = ' --[^*]*'
patternToReplace = ' -'
TIMESTAMPFILE = 'timeStampFile.txt'
CONTACTFILE = 'contacts.csv'
allContacts = []

class Person:
    def __init__(self, firstname, lastname, birthday, email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.email = email
        
# Compares timestamps of the csv files. If the timestamp on the csv is newer than the saved one (or there is no old time stamp), return true
# Reads the timestamp of the csv file and saves it in the timeStampFile.txt
def checkForChanges():
    contactModifiedDate = time.ctime(os.path.getmtime(CONTACTFILE))
    print(contactModifiedDate)
    try:
        if os.path.isfile(TIMESTAMPFILE):
            oldModifiedFile = open(TIMESTAMPFILE, "r")
            oldModifiedDate = oldModifiedFile.readline()
            oldModifiedFile.close()
            if (contactModifiedDate==oldModifiedDate):
                return False
            else:
                oldModifiedFile = open(TIMESTAMPFILE, "w")
                oldModifiedFile.write(contactModifiedDate)
                oldModifiedFile.close()
                return True          
        #file didn't exist -> first time this script is running
        else:
            print('Did not exist yet')
            oldModifiedFile = open(TIMESTAMPFILE,"w+")
            oldModifiedFile.write(contactModifiedDate)
            oldModifiedFile.close()
            return True
    except Exception as e:
        print(e)
        return True
    finally:
        oldModifiedFile.close()

    

def readContacts():
    firstLine = True
    with open(CONTACTFILE) as csvfile:
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
                if not(row[1]== '' or date=='' or row[30]==''):
                    if re.match(patternNoYear, date):

                        date = re.sub(patternToReplace, '1111', date)

                    person = Person(row[1], row[3], date, row[30])
                    allContacts.append(person)
    csvfile.close()
    return allContacts

# For testing    
def printContacts(allContacts):
    for person in allContacts:
        print(person.firstname + ' ' + person.lastname + ' ' + person.birthday + ' ' + person.email)