
# Task 1: Phone Number Cleaner
# Rule: Remove all dashes "-", spaces " ", and dots "." from a phone number.
from calculator import *

def test_task_1():
    assert clean_phone("059-123 45.67") == "0591234567"

def test_task_2():
    assert bmi_risk(22.0) == "Normal"
    assert bmi_risk(35.0) == "Obese"

def test_task_3():
    assert total_dose([200, -50, 400]) == 600

def test_task_4():
    assert find_patient("Leen Maswadeh", "leen") == True

def test_task_5():
    assert convert_glucose(5.0, "mmol/L") == 90.0
    assert convert_glucose(100, "unknown") == 0.0

def test_task_6():
    result = get_unique_meds(["Asprin", "Asprin", "Panadol"])
    assert len(result) == 2
    assert "Asprin" in result

def test_task_7():
    assert calc_duration(10, 14) == 4
    assert calc_duration(23, 1) == 2 # 11 PM to 1 AM
    
# # # # from calculator import get_gender
# # # # def test_gender():
# # # #     # If the user types a small 'm', it should still return 'Male'
# # # #     assert get_gender("m") == "Male"
# # # # from calculator import count_high_hr
# # # # def test_hr_count():
# # # #     patients = [110, 120, 80, 130]
# # # #     # There are 3 patients over 100.
# # # #     assert count_high_hr(patients) == 3
# # # # from calculator import needs_urgent_care
# # # # def test_urgent_care():
# # # #     # This patient has a fever BUT is NOT dehydrated. 
# # # #     # They should be "Normal" (according to our strict rule).
# # # #     assert needs_urgent_care(38.0, False) == "Normal"
# # # from calculator import *
# # ################################################################################
# # # def test_task_1():
# # #     assert is_valid_id("MED-1234") == True
# # #     assert is_valid_id("MED-1") == False

# # # def test_task_2():
# # #     # 70.5 * 0.123 = 8.6715. Should be rounded to 8.67
# # #     assert calculate_precise_dose(70.5, 0.123) == 8.67

# # # def test_task_3():
# # #     assert average_bp([120, 130, 110]) == 120
# # #     # Testing the "Empty List" safety rule
# # #     assert average_bp([]) == 0

# # # def test_task_4():
# # #     assert categorize_patient(10) == "Child"
# # #     assert categorize_patient(30) == "Adult"
# # #     assert categorize_patient(70) == "Senior"

# # # def test_task_5():
# # #     assert temp_warning(41.0) == "Danger"
# # #     assert temp_warning(34.0) == "Danger"
# # #     assert temp_warning(37.0) == "Safe"
# # ####################################################################33
# # # from calculator import *

# # # def test_task_1():
# # #     assert get_dept("SURG-123") == "SURG"
# # #     assert get_dept("LAB-99") == "LAB"

# # # def test_task_2():
# # #     data = [80, 120, 95, 110]
# # #     assert get_alerts(data) == [120, 110]

# # # def test_task_3():
# # #     # Only one number needs to be high to trigger the alert
# # #     assert is_high_bp(150, 80) == True  # Systolic is high
# # #     assert is_high_bp(120, 95) == True  # Diastolic is high
# # #     assert is_high_bp(120, 80) == False # Both are normal

# # # def test_task_4():
# # #     p = {'name': 'Leen', 'status': 'admitted'}
# # #     result = discharge_patient(p)
# # #     assert result['status'] == 'discharged'

# # # def test_task_5():
# # #     assert recovery_rate(5, 10) == 50.0
# # #     assert recovery_rate(0, 0) == 0.0
# # ##################################################33 
# # from calculator import *

# # def test_task_1():
# #     # Weight 70, Height 1.75 -> BMI should be ~22.9
# #     assert calculate_bmi(70, 1.75) == 22.9

# # def test_task_2():
# #     assert glucose_check(250) == "High"
# #     assert glucose_check(50) == "Low"
# #     assert glucose_check(100) == "Normal"

# # def test_task_3():
# #     assert format_name("Leen", "Maswadeh") == "Maswadeh, Leen"

# # def test_task_4():
# #     # The computer expects a Boolean (True), not a String ("True")
# #     assert is_available(5) == True
# #     assert is_available(0) == False

# # def test_task_5():
# #     assert sum_results([10, 20, 30]) == 60
# ###############################################
# from calculator import *
# import pytest

# def test_task_1():
#     assert normalize_data(15, 10, 20) == 0.5
#     # The Safety Rule: Should not crash if max == min
#     assert normalize_data(10, 10, 10) == 0.0

# def test_task_2():
#     assert detect_trend([70, 80, 90, 85]) == True
#     assert detect_trend([70, 60, 80, 90]) == False
#     # Should not crash on short lists
#     assert detect_trend([70, 80]) == False

# def test_task_3():
#     p_good = {'medical_data': {'blood_pressure': 120}}
#     p_bad = {'name': 'Leen'} # Missing medical_data
#     assert get_bp(p_good) == 120
#     assert get_bp(p_bad) == "N/A"

# def test_task_4():
#     assert check_conflict(["Med_A", "Asprin", "Med_B"]) == "Conflict"
#     assert check_conflict(["Med_A", "Asprin"]) == "Safe"

# def test_task_5():
#     data = [{'name': 'A', 'score': 10}, {'name': 'B', 'score': 50}]
#     result = sort_by_priority(data)
#     assert result[0]['score'] == 50 # Highest score first
#########################################################
