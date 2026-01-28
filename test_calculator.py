# from calculator import get_gender
# def test_gender():
#     # If the user types a small 'm', it should still return 'Male'
#     assert get_gender("m") == "Male"
# from calculator import count_high_hr
# def test_hr_count():
#     patients = [110, 120, 80, 130]
#     # There are 3 patients over 100.
#     assert count_high_hr(patients) == 3
from calculator import needs_urgent_care
def test_urgent_care():
    # This patient has a fever BUT is NOT dehydrated. 
    # They should be "Normal" (according to our strict rule).
    assert needs_urgent_care(38.0, False) == "Normal"