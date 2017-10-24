from nose.tools import *
from midterms.contactlist import *


def Information_tests ():
	my_var = Information("Elizabeth", "7736008782", "LSM", "Myself")
	assert_equal(my_var.name, "Elizabeth")
	assert_equal(my_var.number, "7736008782")
	assert_equal(my_var.workplace, "LSM")
	assert_equal(my_var.relationship, "Myself")
	
	
def ContactList_tests():
	mycon_var = ContactList("Name", "Number", "Workplace", "Relationship" )
	
	mycon_var.myadd()
	
	
	assert_equal(mycon_var.mylist[0].name, "Elizabeth")
	assert_equal(mycon_var.mylist[0].number, "7736008782")
	assert_equal(mycon_var.mylist[0].workplace, "LSM")
	assert_equal(mycon_var.mylist[0].relationship, "Myself")
	

	
	