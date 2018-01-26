def add_only_integers(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return 'invalid parameters'


#Test Integers - RUN TEST
def test_integers():
    assert add_only_integers(2, 3) == 5
 #Test Not Integers - RUN TEST
def test_not_integers():
    assert add_only_integers(2, 'what') == 'invalid parameters'