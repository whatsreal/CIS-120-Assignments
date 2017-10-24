from nose.tools import *
from midterms.midterm2 import *

def test_phoneentry():
	mike = phoneentry("mike", "three", "walmart", "Me") 
	assert_equal(mike.name, "mike")
	assert_equal(three.number, "three")
	assert_equal(walmart.work, "walmart")
	assert_equal(Me.relation, "Me")


def test_phonebook():
	things = phonebook("things")
	assert_equal(things.dbname, "things")
	things.add("Bob", "four", "Subway", "cousin")