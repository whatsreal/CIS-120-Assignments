import shelve
import string
from sys import exit

#defining a class requires (Object): at the end.
class phoneentry(object):
    # This doesn't seem to be doing anything?
    def __repr__(self):
            return('%s:%d' % ( self.name, self.type ))

    def __init__(self, name, number, work, relation):
        self.name = name;
        self.number = number;
        self.work = work;
        self.relation = relation;

    #This function is not called anywhere.
    #I was able to comment it out with no problem
    def __cmp__(self, that):
            this = string.lower(str(self))
            that = string.lower(that)

            if string.find(this, that) >= 0:
                    return(0)
            return(cmp(this, that))

    # Again, this function isn't doing anything in your program.
    def showtype(self):
            if self.type == number: return('Number')
            if self.type == name: return('Name')
            if self.type == work: return('Work')
            if self.type == relation: return('Relation')

#see note above class phoneentry
class phonebook(object):
	def __init__(self, dbname = 'phonedata'):
		self.dbname = dbname;
		self.shelve = shelve.open(self.dbname);
		self.phonedata = []

        #Nice! __del__ is always called at the closing of an object!
	def __del__(self):
		self.shelve.close()
		self.shelve = None

	def add(self, name, number, work, relation):
		self.phonedata.append(phoneentry( name, number, work, relation))

        #Why are you printing EVERY phone entry(sublist) instead of the one you
        #Are looking for.
	def search(self, string):
		for sublist in self.phonedata:
			print sublist;


def openPB():
#Because you are re-creating your phonebook every time and
#never saving it to a file or reading in from a file,
#there is never something to search.
	foo = phonebook()
	print 'Please select an option:'
	print '1 - Lookup'
	print '2 - Add'
	print '3 - Delete'
	print '4 - Quit'
	entry=int(raw_input('>> '))
	if entry==1:
		namesearch=raw_input('Please enter a name: ')
		foo.search(namesearch)

	elif entry==2:
		name=raw_input('Name: ')
		number=raw_input('Number: ')
		work=raw_input('Work: ')
		relation=raw_input('Relation: ')
		foo.add(name, number, work, relation)
	elif entry==3:
		delname=raw_input('Please enter a name to delete: ')
		print "Contact '%s' has been deleted" (delname) #You are missing the % between the end of the quoted string and the delname variable.  Crashes here.
	elif entry==4:
		print "Phone book is now closed"
		exit(4)
	else:
		print "Your entry was not recognized."
		openPB()

#instead of this and the while line just do while(True):
i = phonebook
while (i):
	i = phonebook
	openPB()
