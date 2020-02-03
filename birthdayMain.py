import readExcel
import data
import exportdata
import sendMail


# calls function connectoToDB from module data
# assigns db object (connection) to var db
db = data.connectToDB()

# if csv-contacts-file changed -> csv-file is read and exported as an object list (Person)
if (readExcel.checkForChanges()):
    print('fill db')
	#csv-file is read, exported as list (assigned to var allContacts)
    allContacts = readExcel.readContacts()
	# data from Person object list is imported into database birthdays
    data.importData(db, allContacts)

# no change - database up to date
# exports list with Person objects (whose birthday it is)
todayBirthdayList = exportdata.exportObjectList()

# e-mail is sent to birthday person(s) and yourself 
sendMail.sendMails(todayBirthdayList)