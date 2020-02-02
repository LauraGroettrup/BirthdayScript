import mysql.connector
import mysql
from mysql.connector import Error
from datetime import datetime
from readExcel import Person

def exportObjectList():

	today = datetime.now().strftime('%m-%d')
	
	'''class Person:
		def __init__(self, firstname, lastname, birthday, email):
			self.firstname = firstname
			self.lastname = lastname
			self.birthday = birthday
			self.email = email
	'''
	try:

		connection = mysql.connector.connect(
			host="localhost",
			user ="root",
			passwd="IwidLG47mBadS.",
			database = "birthdays"
		)

		sql_select_Query = "select * from persons"
		cursor = connection.cursor()
		cursor.execute(sql_select_Query)
		resultSet = cursor.fetchall()

		list_persons = []
	
		for row in resultSet:
			if (row[2].strftime('%m-%d') == today):
				person = Person(row[0], row[1], row[2], row[3])
				list_persons.append(person)
		
		for person in list_persons:
			print (person.firstname, person.lastname, person.birthday, person.email)
	
		return list_persons
		
	except Error as e:
		print ("Error reading data from Mysql table", e)
	finally:
		if (connection.is_connected()):
			connection.close()
			cursor.close()
			
		

