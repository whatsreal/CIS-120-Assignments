from nose.tools import *
from midterms.midterms import *

assert_equal(loadcontacts("savefile.txt")[0][0], '1234')
