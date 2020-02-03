# BirthdayScript
## Description
A python script that automatically sends an E-mail to persons in your contacts, if it is their birthday.
## Execution Guide
To run this script, following preparations have to be done:

Contacts:
- To send Emails to your contacts, you have to export your contacts from your gmail account (no other sources implemented yet) 
- Replace the sample contacts.csv file with your contacts.csv file (name have to be the same!)
- To use the script, your contacts need to have at least a firstname, an email address, and a birthday

Email-Account:
- Open the file EmailAccData.txt
- Change the email-address to your email-address
- Encode your Email Password with [ROT13](https://gc.de/gc/rot13/) and replace the second line with it
- replace the last line with your name
OR use the example Mail Adresse given in the EmailAccData.txt. To log in, you have to decode the Password (second line) with Rot13 <br>

Python:	
- Install Python 3.2 or higher
- In the command line, use following command to import the needed module
```shell
python -m pip install mysql-connector
```

MySQL:

Cronjob:

## About us
This script was developed as part of the Scripting course MSD18 at FH joanneum.

Authors: Ulrike Gartler, Laura Gröttrup