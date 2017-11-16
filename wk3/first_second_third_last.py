def insert_human(a_list, position, elem):
    if position == 'first':
        a_list.insert(0, elem)
    if position == 'second':
        a_list.insert(1, elem)
    if position == 'third':
        a_list.insert(2, elem)
    if position == 'last':
        a_list.insert(3, elem)




# Test Second Position - RUN TEST
def test_second_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'second', 'X')
    assert list_1 == ['a', 'X', 'b', 'c']
# Test Last Position - RUN TEST
def test_last_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'last', 'X')
    assert list_1 == ['a', 'b', 'c', 'X']
# Test Third Position - RUN TEST
def test_third_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'third', 'X')
    assert list_1 == ['a', 'b', 'X', 'c']
#Test First Position - RUN TEST
def test_first_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'first', 'X')
    assert list_1 == ['X', 'a', 'b', 'c']