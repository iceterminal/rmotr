def append_x(a_string):
    if a_string > 0:
        return a_string + x



#Test With Empty String - RUN TEST
def test_with_empty_string():
    assert append_x('') == ''
 #Test With Valid String - RUN TEST
def test_with_valid_string():
    assert append_x('abc_') == 'abc_x'