import mysql.connector
import mysql
from mysql.connector import Error

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
	print ("Gesamtzahl Zeilen in table persons: ", cursor.rowcount)

	list_persons = []
	
	for row in resultSet:
		list_persons.append(row)
	'''
		print ("firstName: ", row[0])
		print ("lastName: ", row[1])
		print ("birthday: ", row[2])
		print ("email: ", row[3], "\n")'''
		
	for x in list_persons:
		print (x)
		
	#print (list_persons[1][2])
		
except Error as e:
	print ("Error reading data from Mysql table", e)
finally:
	if (connection.is_connected()):
		connection.close()
		cursor.close()
		print ("Mysql connection closed")