def check_out_of_boundaries(number):
    if number < 0 or number > 10:
        return True
    else:
        return False


#Test Over 10 - RUN TEST
def test_over_10():
    assert check_out_of_boundaries(12) is True
# Test In Boundaries - RUN TEST
def test_in_boundaries():
    assert check_out_of_boundaries(7) is False
 #Test Negative - RUN TEST
def test_negative():
    assert check_out_of_boundaries(-3) is True