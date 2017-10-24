from initialize import *
from sys import exit 

a_entry = contacts()

while True:
	user_reply = raw_input("""Welcome. What would you like to do? 
	1. Add an entry
	2. Search for an entry
	3. Edit Entry
	4. Quit
	> """)
	
	if(user_reply == '1'):
		print "Please enter the name > "
		name = raw_input()
		print "Please enter the workplace > "
		work = raw_input() 
		print "Please enter the phone number > " 
		phone = raw_input()
		print "Please enter your relationship to this person > "
		relationship = raw_input()
		a_entry.add(name, work, phone, relationship)
		
	elif(user_reply == '2'):
		print "Please enter a name, workplace, phone number or relationship. > "
		entry = raw_input()
		a_entry.search(entry)
		
	elif(user_reply == '3'):
		print "Please enter the name of the entry you would like to edit. > "
		search = raw_input()
		print """What would you like to edit?
	-Name
	-Work
	-Phone
	-Relationship
	> """
		attUpdate = raw_input()
		print "Please enter the new value. > "
		newVal = raw_input()
		a_entry.update(search, attUpdate, newVal)
		
	elif(user_reply == '4'):
		exit(0)
	
	else:
		print "Please enter a valid option."
	
