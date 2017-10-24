from nose.tools import *
from MIDTERM.initialize import *

def test_masterlist():
	stuff = master_list("name", "work", "number", "relationship")
	assert_equal(stuff.name, "name")
	assert_equal(stuff.work, "work")
	assert_equal(stuff.number, "number")
	assert_equal(stuff.relationship, "relationship")
	
def test_add_contacts():
	main = contacts()
	main.add("Justin", "Admissions", "626", "MAN")
	assert_equal(main.entrylist[0].name, "Justin")
	assert_equal(main.entrylist[0].work, "Admissions")
	assert_equal(main.entrylist[0].number, "626")
	assert_equal(main.entrylist[0].relationship, "MAN")
	
def test_update_contacts():
	pass
	#main = contacts()
	#main.update("Justin", "Work", "MARK")
	#assert_equal(main.entrylist[0].name, "Justin")
	#assert_equal(main.entrylist[0].work, "Work")
	#assert_equal(main.entrylist[0].work, "MARK")
	
	
	
