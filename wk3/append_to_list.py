def append_to_list(hungry_list, data):
    hungry_list.append(data)
    return hungry_list



def test_append_empty_list():
    assert append_to_list([], "list food") == ["list food"]


def test_append_bigger_list():
    assert append_to_list(["pizza", "nachos"], "chips") == ["pizza", "nachos", "chips"]