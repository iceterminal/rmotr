def get_search_match_indexes(list_being_frisked, search_term):
    frisked_list = []
    count = 0
    for i in list_being_frisked:
      if i is "suspicious":
        frisked_list.append(count)
      count = count + 1 
    return frisked_list




# Test Get Search Match Indexes - RUN TEST
def test_get_search_match_indexes():
    assert get_search_match_indexes(["glasses", "suspicious", "pen", "suspicious"], "suspicious") == [1, 3]