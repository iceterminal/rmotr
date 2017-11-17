def get_average(list_of_numbers):
    for i in list_of_numbers:
        i = i + 1
    return i / len(list_of_numbers)




# Test Get Average - RUN TEST
def test_get_average():
    assert get_average([5, 10, 6]) == 7