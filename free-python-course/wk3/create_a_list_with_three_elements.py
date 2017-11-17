# Enter 3 words to describe pizza
word1 = 'cheesy'
word2 = 'chewy'
word3 = 'saucy'

# Now make a list containing each of these words and store in a variable called `pizza_time`.
pizza_time = [word1, word2, word3]




#Test List Three Elem - RUN TEST
def test_list_three_elem():
    assert type(pizza_time) == list
    assert len(pizza_time) == 3
    assert pizza_time == [word1, word2, word3]
    assert type(word1) == str
    assert type(word2) == str
    assert type(word3) == str