x = 15

if x > 10:
    message_1 = "Python is Awesome"

if x < 20:
    message_2 = "Python is Great"

print(message_1)
print(message_2)



#Test Message 2 - RUN TEST
def test_message_2():
    assert message_2 == "Python is Great"
 #Test Message 1 - RUN TEST
def test_message_1():
    assert message_1 == "Python is Awesome"