import readExcel
import data
import exportdata
import sendMail


db = data.connectToDB()

# inserted file changed
if (readExcel.checkForChanges):
	allContacts = readExcel.readContacts()
	#readExcel.printContacts(allContacts)
	data.importData(db, allContacts)
# no change - database up to date
todayBirthdayList = exportdata.exportObjectList()
sendMail.sendMails(todayBirthdayList)