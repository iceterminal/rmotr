def knock_three_times():
    knock = 1
    while knock < 4:
        print("Knock Knock")
        knock = knock + 1




#Test Knock Three Times - RUN TEST
def test_knock_three_times():
    with CaptureOutput() as output:
        knock_three_times()

    assert len(output) == 3
    assert output == [
        'Knock Knock',
        'Knock Knock',
        'Knock Knock'
    ]