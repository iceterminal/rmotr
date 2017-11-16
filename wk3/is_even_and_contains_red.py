def is_even_and_contains_red(a_list):
    if 'red' in a_list and len(a_list) % 2 == 0:
        return True
    else:
        return False




#Test Even With Red - RUN TEST
def test_even_with_red():
    assert is_even_and_contains_red(['red', 'blue', 'green', 'white']) == True
# Test Even Without Red - RUN TEST
def test_even_without_red():
    assert is_even_and_contains_red(['black', 'blue', 'green', 'white']) == False
# Test Odd With Red - RUN TEST
def test_odd_with_red():
    assert is_even_and_contains_red(['red', 'blue', 'green']) == False
# Test Odd Without Red - RUN TEST
def test_odd_without_red():
    assert is_even_and_contains_red(['blue', 'green', 'white']) == False