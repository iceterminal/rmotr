# First, we need to set up a variable.
# Replace the ? with how many chickens you think have crossed the road today.
number_of_chickens = 3

# Set up a new list `my_list` containing the number_of_chickens variable! Wooo!
my_list = [number_of_chickens]

length_of_my_list = len(my_list)  # Use the `len` function to count how many items `my_list` has.







#Test List One Elem - RUN TEST
def test_list_one_elem():
    assert my_list == [number_of_chickens], "Your list doesn't contain the number of chickens :("
    assert length_of_my_list == 1