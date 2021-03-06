def multiply_by_two(x):
    return x * 2

# --- Testing ---
# Use the code below for your own testing
# by clicking the "Run Code" button.
# After you're done, remove the lines below and "Submit Solution".

two_times_two = multiply_by_two(2)
three_times_two = multiply_by_two(3)
five_times_two = multiply_by_two(5)

print("2x2 = {}".format(two_times_two))
print("3x2 = {}".format(three_times_two))
print("5x2 = {}".format(five_times_two))



# --- Testing ---
# Test Five Times Two - RUN TEST
def test_five_times_two():
    assert multiply_by_two(5) == 10
 #Test Two Times Two - RUN TEST
def test_two_times_two():
    assert multiply_by_two(2) == 4