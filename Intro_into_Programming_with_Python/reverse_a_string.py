def reverse_string(a_string):
    reverse = ''
    for i in a_string:
        reverse = i + reverse
    return reverse



#Test With Large String - RUN TEST
def test_with_large_string():
    assert reverse_string('Python is Awesome') == 'emosewA si nohtyP'
 #Test With Short String - RUN TEST
def test_with_short_string():
    assert reverse_string('Python') == 'nohtyP'