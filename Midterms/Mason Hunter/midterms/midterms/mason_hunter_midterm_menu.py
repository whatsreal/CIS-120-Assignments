print "Welcome to the Phonebook"
from mason_hunter_midterm import *
phonebook = phonebook()

while True:
    print """
------------------------


Please select one of the following options:
1.) Add a contact
2.) Search by name
3.) Search by number
4.) Search by work
5.) Search by relationship
6.) Read this phonebook (and pass in another name of a phonebook if you want to read/add that one)
7.) Exit"""
    answer = raw_input("What option do you choose? > ")
    if answer == '1':
	    phonebook.new_contact()
    if answer == '2':
	    phonebook.search_by_name()
    if answer == '3':
	    phonebook.search_by_number()
    if answer == '4':
	    phonebook.search_by_work()
    if answer == '5':
	    phonebook.search_by_relationship()
    if answer == '6':
	    phonebook.read_phonebook()
    if answer == '7':
	    exit()
    