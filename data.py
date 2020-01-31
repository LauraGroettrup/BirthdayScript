import mysql.connector
import mysql

def importData(allContacts):
	db = mysql.connector.connect(
		host="localhost",
		user ="root",
		passwd="IwidLG47mBadS.",
	)

	cursor = db.cursor()
	
	cursor.execute("create database if not exists birthdays") #else if exists delete it and create a new one

	cursor.execute("use birthdays")
	cursor.execute("create table if not exists persons (firstName varchar(30) not null, lastName varchar (40), birthday date not null, email varchar (50) not null primary key)")


		
	sql = "INSERT INTO persons (firstName, lastName, birthday, email) VALUES (%s, %s, %s, %s)"

	for x in allContacts:
		cursor.execute(sql, (x.firstname, x.lastname, x.birthday, x.email))
	
	'''for x in persons:
		firstName = x.firstname
		lastname = x.lastname
		birthday = x.birthday
		email = x.email
		'''
	
	
		
	db.commit()