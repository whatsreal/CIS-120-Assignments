from sys import argv
from sys import exit
from os.path import exists
#script, filename = argv
filename = "write.txt"
class Information(object):
	def __init__ (self, name, number, workplace, relationship):
		self.name = name
		self.number = number
		self.workplace = workplace
		self.relationship = relationship
class ContactList(object):
	def __init__ (self, name, number, workplace, relationship):
                #Why are you passing in variables name through relationship
                #You aren't doing anything with them.
		self.mylist = []
	def myread(self):
                #Unnecessary Line.  You aren't doing anything with the output.
		exists(filename)
		if exists(filename) == False:
			return
		with open(filename, 'r') as f:
			for line in f:
				word = line.split()
				new_name = word[0]
				new_number = word[1]
				new_workplace = word[2]
				new_relationship = word[3]
				new_contact = Information(new_name, new_number, new_workplace, new_relationship)
				self.mylist.append(new_contact)
	def add(self):
		n = raw_input("How many contacts would you like to add? > ")
		try:
			n = int(n)
			for i in range(0, n):
				new_name = raw_input("Name (First) > ")
				new_number = raw_input("Number ********** > ")
				new_workplace = raw_input("Workplace > ")
				new_relationship = raw_input("Relationship > ")
				new_contact = Information(new_name, new_number, new_workplace, new_relationship)

				for i in self.mylist:
					if new_name == i.name:
						print "That contact already exists in your directory."
						print i.name
						print i.number
						print i.workplace
						print i.relationship
						return
                                #This is an unnecessary for loop.
                                #You could just add an elif check to the above for loop.
                                #Alternately you could make the if line above be:
                                #if(new_name == i.name OR new_number == i.number):
				for i in self.mylist:
					if new_number == i.number:
						print "That number is already saved in your directory."
						print i.name
						print i.number
						print i.workplace
						print i.relationship
						return
				print "Your new contact, %s, has been successfully added to your directory" % new_name
				self.mylist.append(new_contact)
		except ValueError:
			print "That is not valid input"
	def mywrite(self):
		text_file = open(filename, 'w');
		for i in self.mylist:
			text_file.write(i.name)
			text_file.write("\t")
			text_file.write(i.number)
			text_file.write("\t")
			text_file.write(i.workplace)
			text_file.write("\t")
			text_file.write(i.relationship)
			text_file.write("\n")
	def search(self):
		action1 = raw_input("Search by Name, Number, Workplace, or Relationship? > ")
		if action1 == "Name":
			action = raw_input("Name (First) > ")
			for i in self.mylist:
				if action == i.name:
					print "Yes! That contact is saved in your directory."
					print i.name
					print i.number
					print i.workplace
					print i.relationship
					return
			print "That information was not found in your directory."
		elif action1 == "Number":
			action2 = raw_input("Number ********** > ")
			for i in self.mylist:
				if action2 == i.number:
					print "Yes! That number is saved in your directory."
					print i.name
					print i.number
					print i.workplace
					print i.relationship
					return
			print "That information was not found in your directory."
		elif action1 == "Workplace":
			action3 = raw_input("Workplace > ")
			for i in self.mylist:
				if action3 == i.workplace:
					print "Yes! That contact is saved in your directory."
					print i.name
					print i.number
					print i.workplace
					print i.relationship
					return
			print "That information was not found in your directory."
		elif action1 == "Relationship":
			action5 = raw_input("Relationship > ")
			for i in self.mylist:
				if action5 == i.relationship:
					print "Yes! That contact is saved in your directory."
					print i.name
					print i.number
					print i.workplace
					print i.relationship
					return
		else:
			print "That is not an option. Please try again."

def start():
	while(True):
                #You are printing a welcome statement for every action?
		print "Welcome to your directory. What would you like to do?"
		print '''
			1. Add
			2. Search
			3. Exit
		'''

                #OK, why are you creating and re-creating the object s?
                #This is wasting a lot of resources.
                #You won't notice this with a few contacts, but say you had a phonebook
                #Of 100, or 1000 contacts then you will notice it.
                #S should be created once before starting the while loop
                #And then updated with add() myread() and mywrite()
		action4 = raw_input("Choose a number > ")
		try:
			action4 = int(action4)
			if action4 == 1:
				print "Add"
				s = ContactList("Name", "Number", "Workplace", "Relationship")
				s.myread()
				s.add()
				s.mywrite()
			elif action4 == 2:
				print "Search"
				s = ContactList("Name", "Number", "Workplace", "Relationship")
				s.myread()
				s.search()
			elif action4 == 3:
				print "Exit"
				exit()
		except ValueError:
			print "That is not valid input. Please try again."
start()
