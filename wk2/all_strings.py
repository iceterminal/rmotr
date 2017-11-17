def all_strings(a, b, c):
    if type(a) == str and type(b) == str and type(c) == str:
        return True
    else:
        return False


# Run Code test. You can remove this:

print(type('hello'))
print(type(True))
print(type(123))




#Test With None - RUN TEST
def test_with_none():
    assert all_strings('hello', None, 'Python') == False
# Test With Empty String - RUN TEST
def test_with_empty_string():
    assert all_strings('', 'rmotr', 'Python') == True
# Test With A Number - RUN TEST
def test_with_a_number():
    assert all_strings(3, 'rmotr', 'Python') == False
 #Test With All Strings - RUN TEST
def test_with_all_strings():
    assert all_strings('j', 'rmotr', 'Python') == True