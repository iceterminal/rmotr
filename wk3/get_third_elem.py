def get_third_elem(list_of_stuff):
    return list_of_stuff.index(2)



# Test Get Third Elem - RUN TEST
def test_get_third_elem():
    assert get_third_elem(["not this one", "not this either", "this one!!!"]) == "this one!!!"