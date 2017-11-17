def greatest_parameter(a, b, c, d, e):
    return max(a, b, c, d, e)




# Test With Different Numbers - RUN TEST
def test_with_different_numbers():
    assert greatest_parameter(2, 4, 9, 1, 1) == 9
    assert greatest_parameter(42, 4, 9, 1, 1) == 42
    assert greatest_parameter(5, 4, 9, 1, 17) == 17
# Test With Ones And Zeroes - RUN TEST
def test_with_ones_and_zeroes():
    assert greatest_parameter(0, 0, 1, 0, 0) == 1
 #Test With Negative Values - RUN TEST
def test_with_negative_values():
    assert greatest_parameter(0, -1, -1, -1, 0) == 0