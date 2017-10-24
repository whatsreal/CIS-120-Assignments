# Make sure that you have tests written for every function and variable that you have in each class.
from os.path import exists
from sys import exit

class master_list(object):

	def __init__(self, name, work, number, relationship):
		self.name = name
		self.work = work
		self.number = number
		self.relationship = relationship


class contacts(object):

	def __init__(self):
		self.entrylist = []
		check = exists("contact.txt")
		if check == False:
			return
		#Why are you creating this variable here? Should have created it before
		#check.  You could have used it there.
		#This way you have to have 2 separate places to change the filename rather than
		#just one.
		contact = "contact.txt"
		read_file = open(contact, 'r')
		for i in read_file:
			split_list = i.split()
			name = split_list[0]
			work = split_list[1]
			number = split_list[2]
			relationship = split_list[3]
			old_entry = master_list(name, work, number, relationship)
			self.entrylist.append(old_entry)

	def add(self, new_name, new_work, new_num, new_rel):
		for i in self.entrylist:
			if i.number == new_num:
				print "This number already exists"
				return
		contact = "contact.txt"
		new_entry = master_list(new_name, new_work, new_num, new_rel)
		self.entrylist.append(new_entry)
		create = open(contact, 'a')
		create.write(new_entry.name)
		create.write("\t")
		create.write(new_entry.work)
		create.write("\t")
		create.write(new_entry.number)
		create.write("\t")
		create.write(new_entry.relationship)
		create.write("\t")
		create.write("\n")
		create.close()

	def search(self, entry):
		found = True
		for i in self.entrylist:
			if (entry == i.name or entry == i.work or entry == i.number or entry == i.relationship):
				print i.name
				print i.work
				print i.number
				print i.relationship
				found = False
		if found:
			print "Database does not contain this contact."

	def update(self, search, attUpdate, newVal):
		#Unused variable?
		count = 0
		for i in self.entrylist:
			if (search == i.name):
                                #Instead of 4 ifs it should be if...elif...elif...elifk
				if (attUpdate == 'Name'):
					self.entrylist[count].name = newVal
					return
				if (attUpdate == 'Work'):
					self.entrylist[count].work = newVal
					return
				if (attUpdate == 'Phone'):
					self.entrylist[count].number = newVal
					return
				if (attUpdate == 'Relationship'):
					self.entrylist[count].relationship = newVal
					return
			#if (search != i.name):
			#	print "Please enter a valid name, workplace, number or relationship."
			#	return
                #It might be good to print something inside each if to let the user know that the update worked.
		count = 1

		print "Entry does not exist"