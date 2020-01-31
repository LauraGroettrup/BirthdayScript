import mysql.connector
import mysql

def initateDB(allContacts):
    db = mysql.connector.connect(
        host="localhost",
        user ="root",
        passwd="IwidLG47mBadS.",
    )

    cursor = db.cursor()
    cursor.execute("create database if not exists birthdays")
    
    cursor.execute("use birthdays")
    cursor.execute("create table if not exists persons (firstName varchar(30) not null, lastName varchar (40), birthday date not null, email varchar (50) not null primary key)")

    sql = "INSERT INTO persons (firstName, lastName, birthday, email) VALUES (%s, %s, %s, %s)"

    for person in allContacts:
        cursor.execute(sql, (person.firstname, person.lastname, person.birthday, person.email))
        db.commit()