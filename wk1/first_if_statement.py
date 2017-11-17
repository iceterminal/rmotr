message = None

# Remove square brackets and write condition to make if statement code run
if message == None: 
    message = "Hello World"

print(message)



#Test Equals Hello World - RUN TEST
def test_equals_hello_world():
    assert message == 'Hello World'