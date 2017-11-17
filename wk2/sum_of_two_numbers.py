def sum_of_two_numbers(a, b):
    return a + b


#Test Add Large Numbers - RUN TEST
def test_add_large_numbers():
    assert sum_of_two_numbers(8, 80) == 88
 #Test Add Small Numbers - RUN TEST
def test_add_small_numbers():
    assert sum_of_two_numbers(1, 2) == 3