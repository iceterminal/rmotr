def how_many_days_in(a_month):
    threeone = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    thirty = ['April', 'June', 'September', 'November']
    if a_month in threeone:
        return 31
    elif a_month in thirty:
        return 30
    else:
        return 28


# Test June - RUN TEST
def test_june():
    assert how_many_days_in('June') == 30
# Test December - RUN TEST
def test_december():
    assert how_many_days_in('December') == 31
# Test February - RUN TEST
def test_february():
    assert how_many_days_in('February') == 28