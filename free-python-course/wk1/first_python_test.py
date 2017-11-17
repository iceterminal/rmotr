your_name = "David"
course = "Intro to Python"

greeting_message = "Welcome {} to the {} course!".format(your_name, course)
print(greeting_message)




#Test Name Is Not Blank - RUN TEST
def test_name_is_not_blank():
    assert your_name != ''