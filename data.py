import mysql.connector
import mysql

# establishes connection to MySQL server, return db object if successful
def connectToDB():
	db = mysql.connector.connect(
		host="localhost",
		user ="root",
		passwd=""
	)
	return db

# tries to connect to database 'birthdays', return true if successful (db birthday already exists) and false if not connected (db birthdays does not exist yet)
def connectToBirthdays():
	try:
		db = mysql.connector.connect(
			host="localhost",
			user ="root",
			passwd ="",
			database="birthdays")
		#print ("true")
		return True
	except:
		#print ("false")
		return False
	
# imports object list (allContacts) with person objects into database birthdays
def importData(db, allContacts):
	cursor = db.cursor()
	# checks if database birthday already exist  -if yes, drops it  
	if (connectToBirthdays()):
		cursor.execute("drop database birthdays") 
		
	# creates database birthdays
	cursor.execute("create database birthdays")
	cursor.execute("use birthdays")	
	
	# creates table persons with four columns
	cursor.execute("create table if not exists persons (firstName varchar(30) not null, lastName varchar (40), birthday date not null, email varchar (50) not null primary key)")	
	
	# prepares sql statement
	sql = "INSERT INTO persons (firstName, lastName, birthday, email) VALUES (%s, %s, %s, %s)"
	
	# inserts person objects into table persons
	for x in allContacts:
		cursor.execute(sql, (x.firstname, x.lastname, x.birthday, x.email))
	
	# commits the transaction
	db.commit()


