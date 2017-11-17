language = "Python"
name = "Guido Van Rossum"

string_template = "{name} is the creator of {language}"
text = string_template.format(name=name, language=language)

length_of_language = len(language)
length_of_name = len(name)
length_of_text = len(text)




#Test Length Of Language - RUN TEST
def test_length_of_language():
    assert length_of_language == 6
# Test Length Of Text - RUN TEST
def test_length_of_text():
    assert length_of_text == 41
 #Test Length Of Name - RUN TEST
def test_length_of_name():
    assert length_of_name == 16