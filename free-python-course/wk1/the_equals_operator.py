x = 10

# Remove square brackets and complete if statement conditions to make code run
if x == 10:
    message_1 = "Hello World"

if x != 9:
    message_2 = "This is RMOTR"


print(message_1)
print(message_2)



#Test Message 2 - RUN TEST
def test_message_2():
    assert message_2 == 'This is RMOTR'
 #Test Message 1 - RUN TEST
def test_message_1():
    assert message_1 == 'Hello World'