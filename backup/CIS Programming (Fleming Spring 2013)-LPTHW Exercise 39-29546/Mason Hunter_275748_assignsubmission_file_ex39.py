#Mason Hunter CIS 120
#Assignment 39
#creating a dict of state abbreviations
states = {
     'Oregon': 'OR',
     'Florida' : "FL",
     "California" : "CA",
     "New York" : "NY",
     "Michigan" : "MI"
}
#dictionary of cities to states
cities = {
     "CA" : "San Fransisco",
     "MI" : "Detroit",
     "FL": "Jacksonville"
}
#adding cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

#printing cities
print '-'*10
print "NY state has: ", cities["NY"]
print "OR state has: ", cities["OR"]

#print states
print '-' * 10
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: " , states["Florida"]

#using two dicts
print "-" * 10
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

#printing all state abbreviations
print '-' * 10
for state, abbrev in states.items():
    print "%s has the city %s" % (state, abbrev)

#printing every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
    
#both at same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
    
#state that isn't there
print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print "The city for the state 'TX' is: %s" % city