def traffic_light(color):
    if color == 'red':
        return 'stop'
    if color == 'yellow':
        return 'slow down'
    if color == 'green':
        return 'go'


# Test Red Light - RUN TEST
def test_red_light():
    assert traffic_light('red') == 'stop'
# Test Yellow Light - RUN TEST
def test_yellow_light():
    assert traffic_light('yellow') == 'slow down'
 #Test Green Light - RUN TEST
def test_green_light():
    assert traffic_light('green') == 'go'