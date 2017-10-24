#Brian Jansen
#Ex 18

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg):
	print "arg: %r" % arg
	
def print_none():
	print "Aint got nuthin!"
	
print_two("Zed","Shaw")
print_two_again("Brian","Jansen")
print_one("OH WOW!")
print_none()

#Nothing to do within the script as far as study drills go....
