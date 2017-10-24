from nose.tools import *
from contactlist.midterm import *

def test_Information():
	Marta = Information("Marta", "123", "TIU", "Me")
	assert_equal(Marta.name, "Marta")
	assert_equal(Marta.number, "123")
	assert_equal(Marta.workplace, "TIU")
	assert_equal(Marta.relationship, "Me")
	
def test_ContactList():
	conlist_var = ContactList("Name", "Number", "Workplace", "Relationship")
	assert_equal(conlist_var.mylist, [])
	conlist_var.add()
	assert_equal(conlist_var.mylist[0].name, "Marta")
	assert_equal(conlist_var.mylist[0].number, "123")
	assert_equal(conlist_var.mylist[0].workplace, "TIU")
	assert_equal(conlist_var.mylist[0].relationship, "Me")