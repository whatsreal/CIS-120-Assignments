#Mason Hunter CIS 120
#Assignment 49

#I have no idea what to do in this excersise, I basically copied ex48 and then
#tried to  change it a little to fit into testing a sentence

def test_subject():
    assert_equal(subject.scan("I"), [('subject', 'I')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('subject', 'he'),
                          ('subject', 'they'),
                          ('subject', 'you')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])


def test_sentence():
   if raw_input( )= (subject + verb + noun):
   print "sentence is working"