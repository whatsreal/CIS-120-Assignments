#Elizabeth Murg
#Assignment Number 39. 2.15.2014.

#create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
}

#creates a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY state has: ", cities ['NY']
print "OR state has: ", cities ['OR']

#print some states 
print '-' * 10
print "Michigan's abbreviation is ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state,abbrev)
	
#print every city in state
print '-' * 10 
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
#safely get an abbreviation by state that might not be there
state = states.get ('Texas', None)

if not state:
	print "Sorry, no Texas."

#get a city with a default value
city = cities.get ('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city


#You probably can't tell a dictionary what item number you want?

#study drill1
cities = {
		  'BU': 'Bucharest',
	      'LD': 'London',
	      'PA': 'Paris',
		  }

countries = {
			'RO': 'Romania',
			'EN': 'England',
			'FR': 'France',
			}
			
print "RO stands for", countries ['RO']
print "England's capital is", cities['LD']
print "The ugliest city in France is", cities ['PA']
			