import mysql.connector
import mysql
from mysql.connector import Error
from datetime import datetime
from readExcel import Person

# exports list with Person objects (whose birthday it is)
def exportObjectList():
	# assigns current date to variable today
	today = datetime.now().strftime('%m-%d')
	
	try:
		# establishes connection to database birthdays
		connection = mysql.connector.connect(
			host="localhost",
			user ="root",
			passwd="",
			database = "birthdays"
		)
		# prepares sql-query-statement
		sql_select_Query = "select * from persons"
		# executes query
		cursor = connection.cursor()
		cursor.execute(sql_select_Query)
		# saves fetched data in var resultSet
		resultSet = cursor.fetchall()

		list_persons = []
		# puts Person objects (whose birthday it is) into list_persons
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
		# closes connection
		if (connection.is_connected()):
			connection.close()
			cursor.close()
			
		

