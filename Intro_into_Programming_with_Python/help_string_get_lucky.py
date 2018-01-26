def get_lucky(poor_string, lucky_number):
    newstring = ''
    while lucky_number > 0:
        if lucky_number > 0:
            newstring += '7'
            lucky_number = lucky_number - 1
    return poor_string + newstring

# Test Luckiness - RUN TEST
def test_luckiness():
    assert get_lucky("shiny penny", 5) == "shiny penny77777"
# Test Luckiness - RUN TEST
def test_luckiness():
    assert get_lucky("shiny penny", 3) == "shiny penny777"