def max_char(a_string):
    return max(a_string)



#Test With Empty String - RUN TEST
def test_with_empty_string():
    assert max_char('') == ''
 #Test With A Single Char - RUN TEST
def test_with_a_single_char():
    assert max_char('j') == 'j'