not_a_lie = ["i", "am", "not", "perfect"]

# Write your code using remove here!
not_a_lie.remove('not')

print(not_a_lie)



# Test Remove - RUN TEST
def test_remove():
    assert not_a_lie == ["i", "am", "perfect"]