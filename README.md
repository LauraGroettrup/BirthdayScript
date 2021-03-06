# BirthdayScript
## Description
A python script that automatically sends an E-mail to persons in your contacts, if it is their birthday. It addition, it sends an E-mail to you to inform you that a congratulation E-mail has been sent.

This script works under Windows 10.
## Execution Guide
To run this script, following preparations have to be done:

Contacts:
- To send Emails to your contacts, you have to export your contacts from your gmail account (no other sources implemented yet) 
- Replace the sample contacts.csv file with your contacts.csv file (name has to be the same!)
- To use the script, your contacts need to have at least a firstname, an email address, and a birthday

Email-Account:
- Open the file EmailAccData.txt
- Change the email-address to your email-address
- Encode your Email Password with [ROT13](https://gc.de/gc/rot13/) and replace the second line with it
- Replace the last line with your name<br> OR use the example Mail Adresse given in the EmailAccData.txt. To log in, you have to decode the Password (second line) with Rot13

Python:	
- Install Python 3.2 or higher
- In the command line, use following command to import the needed module
```shell
python -m pip install mysql-connector
```

MySQL:
- Download mysql-installer-community-8.0.19.0.msi (https://dev.mysql.com/downloads/installer) and setup the workbench
- Configure a connection to Python (via mysql-connector) - set host, user, password
- Adapt your host, user and password in the files data.py (functions: connectToDB() and connectToBirthdays()) and exportdata.py (function: exportObjectList())

Batchfile:
- Open the birthdayScript.bat
- You have to replace the first string between the "" with your path to your python interpreter. If you don't know the path, write the command
```shell
where python
```
in your terminal.
- Replace the second parameter with the path to the birthdayScript.bat

Cronjob:
- To run the cronjob, go to your Task Scheduler
- Create task 
	- general: Enter the name of the task, mark "execute with highest privileges", select your Windows Version
	- trigger: New -> Start: date> today time >midnight Run: daily
	- actions: New -> Action: start program   Program/Script: Path to birthdayScript.bat
- Run your task manually to check if it works (at midnight it should run automatically)

## About us
This script was developed as part of the Scripting course MSD18 at FH Joanneum.

Authors: Ulrike Gartler, Laura Gröttrup
