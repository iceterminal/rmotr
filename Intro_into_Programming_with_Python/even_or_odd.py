def even_or_odd(a_number):
    if a_number % 2 == 0:
        return 'even'
    else:
        return 'odd'



#Test With Even Number - RUN TEST
def test_with_even_number():
    assert even_or_odd(42) == 'even'
 #Test With Odd Number - RUN TEST
def test_with_odd_number():
    assert even_or_odd(17) == 'odd'