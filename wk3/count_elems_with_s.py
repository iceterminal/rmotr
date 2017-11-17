def count_elems_with_s(list_of_treasure):
    for i in list_of_treasure:
        count = 0
        if 's' in list_of_treasure:
            count = count + 1
        return count




# Test Count Elems With S - RUN TEST
def test_count_elems_with_s():
    assert count_elems_with_s(["gold", "silver", "bronze", "steel", "soup"]) == 3