def get_grade_letter(score):
    if score > 90:
        return 'A'
    if score > 79 and score < 90:
        return 'B'
    if score > 69 and score < 80:
        return 'C'
    if score > 59 and score < 70:
        return 'D'
    else:
        return 'F'

# Test F Score - RUN TEST
def test_F_score():
    assert get_grade_letter(42) == 'F'
# Test C Score - RUN TEST
def test_C_score():
    assert get_grade_letter(75) == 'C'
# Test A Score - RUN TEST
def test_A_score():
    assert get_grade_letter(93) == 'A'
# Test B Score - RUN TEST
def test_B_score():
    assert get_grade_letter(80) == 'B'
 #Test D Score - RUN TEST
def test_D_score():
    assert get_grade_letter(67) == 'D'