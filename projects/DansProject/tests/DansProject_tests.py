from nose.tools import *
from DansProject.dan import *

def setup():
   print "SETUP"
   
def teardown():
    print "tear down"
    
def test_basic():
    print "I ran."

me = Person()
cat = Pet(me)

assert_equal(cat.owner, me)
assert_equal(cat.owner, "Dan")