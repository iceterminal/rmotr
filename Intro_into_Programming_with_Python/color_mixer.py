def color_mixer(color1, color2):
    if color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
        return 'Magenta'
    if color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
        return 'Green'
    if color1 == 'yellow' and color2 == 'red' or color1 == 'red' and color2 == 'yellow':
        return 'Orange'


# Test Yellow Blue - RUN TEST
def test_yellow_blue():
    assert color_mixer('yellow', 'blue') == 'Green'
# Test Red Yellow - RUN TEST
def test_red_yellow():
    assert color_mixer('red', 'yellow') == 'Orange'
# Test Blue Yellow - RUN TEST
def test_blue_yellow():
    assert color_mixer('blue', 'yellow') == 'Green'
# Test Yellow Red - RUN TEST
def test_yellow_red():
    assert color_mixer('yellow', 'red') == 'Orange'
# Test Red Blue - RUN TEST
def test_red_blue():
    assert color_mixer('red', 'blue') == 'Magenta'
# Test Blue Red - RUN TEST
def test_blue_red():
    assert color_mixer('blue', 'red') == 'Magenta'