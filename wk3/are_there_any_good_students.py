def check_for_good_student(good_bad_student_list):
    if 'good_student' in good_bad_student_list:
        return True
    else:
        return False



# Test Not Present In List - RUN TEST
def test_not_present_in_list():
    assert check_for_good_student(['bad_student', 'terrible_student', 'Santiago']) == False
# Test Present In List - RUN TEST
def test_present_in_list():
    assert check_for_good_student(['bad_student', 'good_student', 'decent_student']) == True