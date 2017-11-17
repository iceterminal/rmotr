def check_if_none(a, b, c, d, e):
    if None in (a, b, c, d, e):
        return True
    else:
        return False




#Test With Many None Value - RUN TEST
def test_with_many_none_value():
    assert check_if_none(None, 2, 'a', 8, None) == True
    assert check_if_none(None, None, None, None, None) == True
# Test Without Many None Value - RUN TEST
def test_without_many_none_value():
    assert check_if_none(0, 2, 'a', 8, 'Z') == False
 #Test With One None Value - RUN TEST
def test_with_one_none_value():
    assert check_if_none(None, 2, 'a', 8, 'Z') == True