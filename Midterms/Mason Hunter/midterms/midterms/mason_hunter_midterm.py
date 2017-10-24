"""Create a contact program.  Keep a collection of all your contacts.  Each contact needs to have a phone 
number, name, and workplace (eg Starbucks, UPS, Walmart...) as well as your relationship to the person (friend, dad, mom, sister, husband).
You should be able to add a phone record to your collection.  Duplicates, based on number, should not be allowed.
The entire collection needs to be written out to a file.
You need to be able to read in from the file and import all the records into your collection.
 
Make sure that you have tests written for every function and variable that you have in each class."""
class contact(object):
    def __init__(self):
	    pass
    
    def add_new(self):
	    global new_number
	    new_name = raw_input("What is the name of the new contact? > ")
	    new_number = raw_input("What is the 10 digit phone number- without any punctuation like '-', '.', '/', etc,- of the new contact? > ")
	    new_work = raw_input("And where does this person work? > ")
	    new_relationship = raw_input("In one work -without spaces- how would you describe your relationship to this person? > ")
	    self.add_new = [new_name, new_number, new_work, new_relationship]
		
class phonebook(object):
    def __init__(self):
	    self.phonebook = []
	
    def new_contact(self):
	    contact1 = contact()
	    global new_number
	    contact1.add_new()
	    for sublist in self.phonebook:
		    if sublist.add_new[1] == new_number:
			    print "That number is already assigned to a contact, please input a different number"
			    contact1 = contact()
			    contact1.add_new()
			    break
		    else:
			    pass
	    self.phonebook.append(contact1)
   	    with open(str('my_phonebook.txt'), 'w') as file:
		    for sublist in self.phonebook:
			    for i in sublist.add_new: 
			        file.write(i), file.write(" ")
			    file.write("\n")
	    file.close()
	     
		
    def search_by_name(self):
	    search_term = raw_input("Please enter the name of the person you wish to search for > ")
	    for sublist in self.phonebook:
		    if sublist.add_new[0] == search_term:
			    print "Found 'em!", sublist.add_new
			    break
		    else:
			    print "Sorry, we could not find that here"
		
    def search_by_number(self):
	    search_term = raw_input("Please input the phone number of the person you are searching for > ")
	    for sublist in self.phonebook:
		    if sublist.add_new[1] == search_term:
			    print "Found 'em!", sublist.add_new
			    break
		    else:
			    print "Sorry, we could not find that here"
		
    def search_by_work(self):
	    search_term = raw_input("Please input the workplace of the person you are searching for > ")
	    for sublist in self.phonebook:
		    if sublist.add_new[2] == search_term:
			    print "Found 'em!", sublist.add_new
			    break
		    else:
			    print "Sorry, we could not find that here"
	
    def search_by_relationship(self):
	    search_term = raw_input("Please input your relationship to the person -or people- you are searching for > ")
	    for sublist in self.phonebook:
		    if sublist.add_new[3] == search_term:
			    print "Found 'em!", sublist.add_new
			    break
		    else:
			    print "Sorry, we could not find that here"
	
    def read_other(self):
	    readable_file = raw_input("What is the name of the file -with its dot notation- you wish to read? > ")
	    with open(readable_file, 'r') as file:
		    print file.read
		    file.close
		
    def add_other(self):
	    added_file = raw_input("What is the name of the phonebook -with its dot notation- which you wish to add to this one? > ")
	    with open(added_file, 'r')as file:
		    self.phonebook.append(file)
		    
	   
	    
    def read_phonebook(self, other_file = "my_phonebook.txt"):
	    file = open('my_phonebook.txt')
	    for i in file:
		    l = i.split(" ")
		    contact1 = contact()
		    contact1.add_new = l
		    self.phonebook.append(contact1)
	    with open(str('my_phonebook.txt'), 'a') as file:
		    file.write("%s" % self.phonebook)
