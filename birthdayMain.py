import readExcel
import data

# read csv file, take relevant columns and only import rows that have values in the relevant columns
persons = readExcel.readContacts()
readExcel.printContacts(persons)

data.importData(persons)