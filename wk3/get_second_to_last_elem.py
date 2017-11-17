def get_second_to_last_elem(list_of_stuff):
    return list_of_stuff.index(-2)




# Test Second To Last Elem - RUN TEST
def test_second_to_last_elem():
    assert get_second_to_last_elem([1, 2, 3, 4, 5, 6, 7, 8, 'MEMEMEMEMEEEE', 9]) == 'MEMEMEMEMEEEE'