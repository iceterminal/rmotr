divisible_by_11 = 11

is_583_divisible_by_11 = None
is_911_divisible_by_11 = None

number_583 = 583

# Remove square brackets and complete if statement condition
if number_583 % divisible_by_11 == 0:
    is_583_divisible_by_11 = True
else:
    is_583_divisible_by_11 = False


is_911_divisible_by_11 = None
number_911 = 911

# Remove square brackets and complete if statement condition
if number_911 % divisible_by_11 == 0:
    is_911_divisible_by_11 = True
else:
    is_911_divisible_by_11 = False




#Test Is 911 Divisible By 11 - RUN TEST
def test_is_911_divisible_by_11():
    assert is_911_divisible_by_11 is False
 #Test Is 583 Divisible By 11 - RUN TEST
def test_is_583_divisible_by_11():
    assert is_583_divisible_by_11 is True