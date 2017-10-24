from sys import argv
from sys import exit
from os.path import exists 
 


filename = "contactlist.txt"
#script, filename = argv

class Information (object):
	def __init__ (self, name, number, workplace, relationship):
		self.name = name
		self.number = number
		self.workplace = workplace 
		self.relationship = relationship
		
class ContactList(object):
	def __init__ (self, name, number, workplace, relationship):
		#Why are you passing the arguments after self? You certainly aren't using them.
		self.mylist = []
		
	def myread (self):
		#Unnecessary Line:
		exists(filename)
		if exists(filename) == False:
			return
		else: 
			print "%r exists." % filename
		with open(filename, "r") as f:
			for line in f:
				word = line.split()
				new_name = word[0]
				new_number = word[1]
				new_workplace = word[2]
				new_relationship = word[3]
				
				new_contact = Information(new_name, new_number, new_workplace, new_relationship)
				
				self.mylist.append(new_contact)
				
	def myadd (self):
		n = raw_input("How many contacts would you like to add? > ")
		
		try:
			n = int(n)
			for i in range(0,n):
				new_name = raw_input("Insert a new name. > ")
				new_number = raw_input("Insert a new number. > ")
				new_workplace = raw_input("Insert a new workplace. > ")
				new_relationship = raw_input ("Insert the contact's relationship to yourself. > ")
			
				new_contact = Information(new_name, new_number, new_workplace, new_relationship)
				
				#OK, checking name as well as number.  Cool.  You could do this as one loop and save yourself some time.
				#Just delete the second for line and make the second if an elif line.
				#I'd also suggest doing the line above this comment AFTER you check for duplicate
				#No sense making the Information() object if you don't need to.
				for i in self.mylist:
					if new_name == i.name:
						print "That name is already in the directory."
						print i.name
						print i.number
						print i.workplace
						print i.relationship
						return
				for i in self.mylist:
					if new_number == i.number:
						print "That number is already in the directory."
						print i.name
						print i.number
						print i.workplace
						print i.relationship
						return
					
				self.mylist.append(new_contact)
				print "Your new contact information for %s has been added." % new_name
				
		except ValueError:
			print "That is not an option. Try again please."
			
	def mywrite (self):
		my_file = open(filename, "w")
		for i in self.mylist:
			my_file.write(i.name)
			my_file.write("\t")
			my_file.write(i.number)
			my_file.write("\t")
			my_file.write(i.workplace)
			my_file.write("\t")
			my_file.write(i.relationship)
			my_file.write("\n")
			
	def mysearch (self):
		action2 = raw_input("Would you like to search by name or by number? > ")
		
		if action2 == "name":
			action3 = raw_input("Insert a name. > ")
			for i in self.mylist:
				if action3 == i.name:
					print "Yes! That contact is in the directory!"
					print i.name 
					print i.number
					print i.workplace
					print i.relationship
					return
					
				
				print "That information is not available."
					
		if action2 == "number":
			action4 = raw_input("Insert a number. > ")
			for i in self.mylist:
				if action4 == i.number:
					print "Yes! That contact is in the directory."
					print i.name
					print i.number
					print i.workplace
					print i.relationship
					return
		#No search by work?  That one is trickier, but would need to be done.
		#Can't ding you on it, though it wasn't in the actual midterm question...oops.
				
				print "That information is not available."
				
def Start():
	while (True):
		print "Welcome to the directory. What would you like to do."
		print '''
			1. Add
			2. Search
			3. Exit
		'''
		
		action6 = raw_input("Choose a number. > ")
		
		try:
			action6 = int(action6)
			#You are creating and re-creating the s variable each time you go through this loop.  
			#That is really really unnecessary.  
			#The correct way to do it would be to initiate s once BEFORE you enter the while loop
			#and then call its functions repeatedly.
			#While you won't notice a performance hit because modern computers are so fast,
			#on a bigger program you'd notice it quite a bit.  
			#This means you are reading and writing also an unnecessarily large number of times.
			#That is another performance hit.

			if action6 == 1:
				print "Add a Contact:"
				s = ContactList("Name", "Number", "Workplace", "Relationship")
				s.myread()
				s.myadd()
				s.mywrite()
				
			if action6 == 2:
				print "Search: > "
				s = ContactList("Name", "Number", "Workplace", "Relationship")
				s.myread()
				s.mysearch()
				
			if action6 == 3:
				print "Exiting."
				exit()
				
		except ValueError:
			print "That is not an option. Try again."

Start()				
