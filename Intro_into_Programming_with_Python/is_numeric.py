def is_numeric(a_number):
    if type(a_number) == str or type(a_number) == bool:
        return False
    else:
        return True



# Test With Boolean - RUN TEST
def test_with_boolean():
    assert is_numeric(True) == False
# Test With Float - RUN TEST
def test_with_float():
    assert is_numeric(0.8) == True
# Test With Integer - RUN TEST
def test_with_integer():
    assert is_numeric(22) == True
# Test With String - RUN TEST
def test_with_string():
    assert is_numeric('Hello World') == False