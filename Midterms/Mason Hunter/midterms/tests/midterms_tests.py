from nose.tools import *
from midterms.mason_hunter_midterm import *
test2 = contact()
test2.add_new()

assert_equal(test2.add_new, ['s', 's', 's', 's'])

test1 = phonebook()
test1.new_contact()

assert_equal(test1.phonebook[0].add_new, ['m', 'm', 'm', 'm'])
assert_equal(True, False)

