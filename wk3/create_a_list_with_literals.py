# Create a list named `heterogeneous` and put a integer, string, and boolean in it.
heterogeneous = [1, 'Test', True]






#Test List Literals - RUN TEST
def test_list_literals():
    assert type(heterogeneous) == list, "Oops, heterogeneous is not a list"

    assert len(heterogeneous) == 3

    assert type(heterogeneous[0]) == int
    assert type(heterogeneous[1]) == str
    assert type(heterogeneous[2]) == bool