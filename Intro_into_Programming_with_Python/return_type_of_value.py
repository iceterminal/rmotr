def which_type(val):
    if type(val) == int:
        return 'integer'
    elif type(val) == str:
        return 'string'
    elif type(val) == float:
        return 'float'
    elif type(val) == bool:
        return 'boolean'
    else:
        return None


# Test Type Int - RUN TEST
def test_type_int():
    assert which_type(42) == 'integer'
# Test Type String - RUN TEST
def test_type_string():
    assert which_type('squirrel') == 'string'
# Test Type Float - RUN TEST
def test_type_float():
    assert which_type(3.14) == 'float'
# Test Type Boolean - RUN TEST
def test_type_boolean():
    assert which_type(True) == 'boolean'