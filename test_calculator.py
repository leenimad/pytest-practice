# from calculator import get_gender
# def test_gender():
#     # If the user types a small 'm', it should still return 'Male'
#     assert get_gender("m") == "Male"
# from calculator import count_high_hr
# def test_hr_count():
#     patients = [110, 120, 80, 130]
#     # There are 3 patients over 100.
#     assert count_high_hr(patients) == 3
# from calculator import needs_urgent_care
# def test_urgent_care():
#     # This patient has a fever BUT is NOT dehydrated. 
#     # They should be "Normal" (according to our strict rule).
#     assert needs_urgent_care(38.0, False) == "Normal"
from calculator import *

def test_task_1():
    assert is_valid_id("MED-1234") == True
    assert is_valid_id("MED-1") == False

def test_task_2():
    # 70.5 * 0.123 = 8.6715. Should be rounded to 8.67
    assert calculate_precise_dose(70.5, 0.123) == 8.67

def test_task_3():
    assert average_bp([120, 130, 110]) == 120
    # Testing the "Empty List" safety rule
    assert average_bp([]) == 0

def test_task_4():
    assert categorize_patient(10) == "Child"
    assert categorize_patient(30) == "Adult"
    assert categorize_patient(70) == "Senior"

def test_task_5():
    assert temp_warning(41.0) == "Danger"
    assert temp_warning(34.0) == "Danger"
    assert temp_warning(37.0) == "Safe"