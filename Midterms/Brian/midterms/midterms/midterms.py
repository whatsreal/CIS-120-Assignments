#Brian Jansen
#Midterm Contact List Manager
from random import randint
from sys import exit
import os
import os.path
import operator

def loadcontacts(filename):
	"""This function loads the list of contacts from a file specified when the function is called.
	After the file is loaded, each line is turned into a list with contact info and then those lists are made into a single list."""
	conlist = []
	splitlist = []
	sortlist = []
	f = open(filename)
	for i in f:
#		print "i = \n", i
		splitlist = []
		for p in i.split():
			p = p.replace(";"," ")
			splitlist.append(p)	
#			print "p = \n", splitlist
		conlist.append(splitlist)
	f.close()
	print "Contacts loaded!"
	return conlist

def savecontacts(filename):
	"""This function basically reverses the proccess of loadcontacts() and saves to a file specified when the function is called."""
	global contactlist
	savestring = ""
	for i in contactlist:
		for p in i:
			pstring = p.replace(" ", ";")
			savestring += "%s " % pstring
		savestring += "\n"
#	print "\n\nsavestring =\n", savestring	
	f = open(filename, "w")
	f.write(savestring)
	f.close()
	print "Contacts Saved!"
	
def addcontact():
	"""This function is runs the user though the proccess of adding a contact's name, work place, and phone number and saves it to the external file at the end."""
	global contactlist, contactfile
	idlist = []
	for i in contactlist:
		idlist.append(i[0])
#	print idlist
	randid = str(randint(1000,9999))
	while randid in idlist:
		randid = str(randint(1000,9999))
	print "Add a New Contact\n=-=-=-=-=-=-=-=-=-=-=-=-="
	name = False
	work = False
	phone = False
	while not name:
		name = raw_input("First and Last Name?\n>> ")
	while not work:
		work = raw_input("Workplace?\n>> ")
	while not phone:
		phone = raw_input("Phone Number? (Ex. (xxx) xxx-xxxx) \n>> ")
	newcontact = [randid, name, work, phone]
	contactlist.append(newcontact)
	savecontacts(contactfile)

def delcontact(contactid):
	"""This function will check the list of contacts for the id or name specified and delete what it finds.  Will not delete based on work place for safety reasons."""
	global contactlist
	exist = False
	for i in contactlist:
		if contactid == i[0] or contactid.lower() == i[1].lower():
			print "Removed Contact:\n[%s] %s\n\nChanges will not take effect in the file until you save." % (i[0], i[1])
			contactlist.remove(i)
			exist = True
	if exist == False:
		print "Sorry, that contact does not exist."

def editcontact(conid, field, newvalue):
	pass

def dupcheck():
	"""DupCheck runs through the list and deletes any contacts that have duplicate names or numbers."""
	global contactlist
	print "Duplicate Checker\n=-=-=-=-=-=-=-=-=-="
	exist = False
	namelist = []
	numlist = []
	dupcount = 0
	for i in contactlist:
		namelist.append(i[1].lower())
	for i in namelist:
		namecount = namelist.count(i)
		print "[%r] %r" % (namecount, i)
		if namecount > 1:
			for p in contactlist:
				if namecount > 1 and i == p[1].lower():
					contactlist.remove(p)
					namelist.remove(i)
					exist = True
					dupcount += 1
					namecount -= 1
	for i in contactlist:
		numlist.append(i[3])
	for i in numlist:
		numcount = numlist.count(i)
		print "[%r] %r" % (numcount, i)
		if numcount > 1:
			for p in contactlist:
				if numcount > 1 and i == p[3]:
					contactlist.remove(p)
					numlist.remove(i)
					exist = True
					dupcount += 1
					numcount -= 1
	if exist == False:
		print "Congratulations, there were no duplicates."
	else:
		if dupcount is 1:
			print "Removed %d duplicate..." % dupcount
		else:
			print "Removed %d duplicates..." % dupcount	

def listcontacts():
	"""This function sorts the lists of contacts alphabetically and outputs them to the user."""
	global contactlist
	sortinghat = sorted(contactlist, key=operator.itemgetter(1))
	print "Contact List\n=-=-=-=-=-=-=-=-=-=" 
#	print sortinghat
	for i in sortinghat:
		print "\n[%s] %s\n%s\n%s" % (i[0], i[1], i[2], i[3])

def searchcontacts(query):
	"""This function searches all the contact info at the same time for the argument that has been provided and outputs the results in no particular order."""
	global contactlist
	exist = False
	count = 0
	print "Search Results for: %s\n=-=-=-=-=-=-=-=-=-=" % query 
	for i in contactlist:
		contactcount = i.count(query)
		if contactcount > 0:	
			print "[%s] %s\n%s\n%s" % (i[0], i[1], i[2], i[3])
			exist = True
			count += 1
	if exist == False:
		print "Sorry, there were no results for %s" % query
	else:
		if count is 1:
			print "\n=-=-=-=-=-=-=-=-=-=\nFound %d result for: %s" % (count, query)
		else:
			print "\n=-=-=-=-=-=-=-=-=-=\nFound %d results for %s" % (count, query)
			
def prompt():
	"""This function basically pulls up the 'menu' that allows the user to navigate the program."""
	global contactlist, contactfile
	string = raw_input("\n=-=-=-=-=-=-=-=-=-=\nWhat would you like to do?  (Type 'help' for a list of commands...)\n>> ").lower()
	os.system('cls' if os.name == 'nt' else 'clear')
	deconstruct = string.split()
	if string == "check duplicates" or string == "dupcheck":
		dupcheck()
		pass
	elif string == "save contacts" or string == "save":
		savecontacts(contactfile)
		pass
	elif string == "load contacts" or string == "reload":
		contactlist = loadcontacts(contactfile)
		pass
	else:
#		prepop = deconstruct[0]
		try:
			command = deconstruct.pop(0)
		except IndexError:
			print "Sorry, I don't understand..."
			prompt()
			pass
#		print "Command: !%r! - !%r!" % (command, prepop)
		argument = " ".join(deconstruct)
#		print "Argument: %s" % argument
		if command == "find" or command == "search" and argument:
			searchcontacts(argument)
		elif command == "add":
			addcontact()
		elif command == "delete" or command == "del" and argument:
			delcontact(argument)
		elif command == "help":
			helpmenu()	
		elif command == "list":
			listcontacts()
		elif command == "exit":
			exit()
		else:
			print "Sorry, that command does not exist."
	prompt()
	
def helpmenu():
	"""This function exists simply to provide the user with a list of valid commands for using the program."""
	print """
Help Menu
=-=-=-=-=-=-=-=-=-=
**Please note that all arguments are case sensitive!**

list - 
Shows a list of contacts saved.

add -
Allows you to add a contact to the list.

delete (or del) <argument> -
Allows you to delete a contact that you specify in the argument.
	
help -
Loads this help page.
	
find (or search) <argument> - 
Searches through the contacts for the argument that you provide.
	
check duplicates (or dupcheck) -
Checks the current list of contacts for duplicate names and numbers and removes them.
	
save contacts (or save) -
Saves the current contact list to an external file.
	
load contacts (or reload) -
Reloads and refreshes the contact list from an external file.
	
exit -
Exits the program.
"""

def startup():
	"""This function exists to load the contacts from an existing file at the start up of the program."""
	global contactlist, contactfile
	os.system('cls' if os.name == 'nt' else 'clear')
	print "Jansen Contact Manager\n=-=-=-=-=-=-=-=-=-=\n"
	contactfile = raw_input("Where are the contacts stored? ")
#	contactfile = "savefile.txt"
	fileexist = os.path.isfile(contactfile)
	if fileexist:
		contactlist = loadcontacts(contactfile)
		prompt()
	else:
		raw_input("Sorry, that file does not exist, press enter to continue...")
		startup()
		
#Start the program...
#startup()
	
