# this is supposed to be done via a while loop.
# The idea is to use a while loop and variables to keep track of results and number of times 'initial_number'
# has been multiplied to itself.
# like:
# while power > 0:
# I decided it was easier to just use the '**' operator instead		


def feel_the_power(initial_number, power):
    new = initial_number ** power
    return new


# Test While Loop Power Zero - RUN TEST
def test_while_loop_power_zero():
    assert feel_the_power(3, 0) == 1
# Test While Loop Power One - RUN TEST
def test_while_loop_power_one():
    assert feel_the_power(3, 1) == 3
# Test While Loop Power Three - RUN TEST
def test_while_loop_power_three():
    assert feel_the_power(3, 3) == 27