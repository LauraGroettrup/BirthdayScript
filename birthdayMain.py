import readExcel
import data
import exportdata
import sendMail

#cronjob at midnight every day
# go to crontab -> add correct times and command "birthdayMain.py" (check if python interpreter has to be added before the script)
# connection to mysql saved in variable db
db = data.connectToDB()

# check if 'inserted file' changed
if (readExcel.checkForChanges()):
    print('fill db')
    allContacts = readExcel.readContacts()
	#readExcel.printContacts(allContacts)
    data.importData(db, allContacts)
# no change - database up to date
todayBirthdayList = exportdata.exportObjectList()
sendMail.sendMails(todayBirthdayList)