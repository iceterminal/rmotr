def is_string(variable):
    if type(variable) == str:
        return True
    else:
        return False



#Test String - RUN TEST
def test_string():
    assert is_string('happy') is True
 #Test Integer - RUN TEST
def test_integer():
    assert is_string(27) is False