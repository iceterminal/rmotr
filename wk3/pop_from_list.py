this_list_is_poppin = ["have", "a", "great", "day"]

# Replace the ? below with your code to pop!
i_am_really = this_list_is_poppin.pop(2)
print(i_am_really)
print(this_list_is_poppin)



 # Test Pop - RUN TEST
def test_pop():
    assert this_list_is_poppin == ["have", "a", "day"]
    assert i_am_really == "great"