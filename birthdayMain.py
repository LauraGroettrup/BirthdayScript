import readExcel
import data
import exportdata
import sendMail

# connection to mysql saved in variable db
db = data.connectToDB()
# check if database birthdays exists: return boolean


# inserted file changed
if (readExcel.checkForChanges):
	allContacts = readExcel.readContacts()
	#readExcel.printContacts(allContacts)
	data.importData(db, allContacts)
# no change - database up to date
todayBirthdayList = exportdata.exportObjectList()
sendMail.sendMails(todayBirthdayList)