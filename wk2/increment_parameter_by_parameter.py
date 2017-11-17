def increment_by(a, b):
    return a + b


#Test Increment Two By Seven - RUN TEST
def test_increment_two_by_seven():
    assert increment_by(2, 7)  == 9
 #Test Increment Five By Three - RUN TEST
def test_increment_five_by_three():
    assert increment_by(5, 3)  == 8