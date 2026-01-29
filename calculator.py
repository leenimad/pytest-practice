# Task 1: Medical Date Formatter
# Rule: Convert a date from "DD/MM/YYYY" to "YYYY-MM-DD"
def format_date(date_str):
    parts = date_str.split("/")
    # Bug: Check the order of parts
    return parts[2] + "-" + parts[1] + "-" + parts[0]

# Task 2: Patient Risk Score
# Rule: Score = (Age * 0.5) + (Heart_Rate * 0.2). 
# If the patient is a "Smoker", add 10 points to the TOTAL score.
def calculate_risk(age, hr, is_smoker):
    score = age * 0.5 + hr * 0.2
    if is_smoker == "True": # Bug: Check the data type of is_smoker
        score += 10
    return round(score, 1)

# Task 3: Lab Result Cleaner
# Rule: Given a list of results, remove any that are 0.0 (error) and return the rest.
def clean_results(results):
    return [r for r in results if r != 0.0]

# Task 4: Medication Dosage Lookup
# Rule: Return the dose for a given med name. If not found, return "Not Found".
def get_dosage(med_name):
    dosages = {"Asprin": "100mg", "Panadol": "500mg"}
    # Bug: This crashes if the med is not in the dictionary
    return  dosages.get(med_name, "Not Found")

# Task 5: Heart Rate Average (Safe)
# Rule: Average = sum / count. If count is 0, return 0.
def average_heart_rate(hr_list):
    if len(hr_list) > 0:
        avg = sum(hr_list) / len(hr_list)
    # Bug: What happens if len is 0? The function returns None.
    if len(hr_list) == 0:
        return 0
    return avg

# Task 6: Surgery Room Logger
# Rule: Return a string: "Room [X]: [Patient Name]"
def log_surgery(room_number, patient_name):
    # Bug: room_number is an integer, patient_name is a string.
    return "Room " + str(room_number )+ ": " + patient_name

# #  Task 1: Phone Number Cleaner
# # Rule: Remove all dashes "-", spaces " ", and dots "." from a phone number.
# def clean_phone(phone):
#     # Bug: Only one of these is being replaced correctly
#     clean = phone.replace(" ", "").replace("-", "").replace(".","")
#     return clean

# # Task 2: BMI Risk Assessment
# # Rule: BMI < 18.5: "Under", 18.5-24.9: "Normal", 25-29.9: "Over", 30+: "Obese"
# def bmi_risk(bmi):
#     if bmi < 18.5:
#         return "Under"
#     elif 18.5 <= bmi <= 24.9:
#         return "Normal"
#     elif 25.0 <= bmi <= 29.9:
#         return "Over"
#     # Bug: What if the BMI is 30.0 or higher?
#     else:
#         return "Obese"

# # Task 3: Total Daily Dose
# # Rule: Given a list of doses [200, 400, 200], return the total. 
# # Safety: If any dose is negative, ignore it (do not add it).
# def total_dose(doses):
#     total = 0
#     for d in doses:
#         if d > 0:
#             total += d 
#         elif d<0:
#             total= total    
#     return total

# # Task 4: Patient Name Search
# # Rule: Return True if a search term exists in the patient name (Case-Insensitive).
# def find_patient(name, search_term):
#     # Bug: Logic works, but is it case-insensitive?
   
    
#     if  search_term.lower() in name.lower():
#         return True
#     return False

# # Task 5: Lab Result Units
# # Rule: If unit is "mg/dL", return value. If "mmol/L", multiply by 18 to convert.
# def convert_glucose(value, unit):
#     if unit == "mg/dL":
#         return value
#     if unit == "mmol/L":
#         return value * 18
#     # Bug: Should return 0.0 for unknown units
#     else:
#         return 0.0
    
#     return value

# # Task 6: Unique Medications
# # Rule: Given a list of meds (with duplicates), return a list of UNIQUE meds.
# def get_unique_meds(meds_list):
#     # Hint: There is a specific Python data structure for uniqueness
#     # unique_list = []
#     # for m in meds_list:
        
#     #     unique_list.append(m)
        
#     return set(meds_list)

# # Task 7: Appointment Duration
# # Rule: Take start_hour and end_hour (24h format). Return duration.
# # If end_hour is before start_hour, it means it's the next day (e.g., 23 to 01 = 2h).
# def calc_duration(start, end):
#     if end > start:
#         return end - start
    
#     elif start > end :
#         return (24 + end) - start
    
        
#     else:
#         # Bug: Logic for the "Next Day" calculation
#         return start - end
    
# # #def future_age(age_input):
# #     # This will crash if age_input is a string!
# #     return int(age_input) + 10
# #  case sensitivity : 
# # def get_gender(letter):
# #     if letter.lower() == "m":
# #         return "Male"
# #     elif letter.lower() == "f":
# #         return "Female"
# #     else:
# #         return "Unknown"

# # def count_high_hr(hr_list):
# #     count = 0
# #     for hr in hr_list:
# #         if hr > 100:
# #             count = count + 1
# #     return count # BUG: This is inside the loop!

# # def needs_urgent_care(temp, is_dehydrated):
# #     # Requirement: BOTH must be true to be "Urgent"
# #     if temp > 37.5 and is_dehydrated == True:
# #         return "Urgent"
# #     else:
# #         return "Normal"
    
# # print (needs_urgent_care(38,False))    
# ###########################################################################
# # # Task 1: Medical ID Validator
# # # Rule: ID must start with "MED-" and be exactly 8 characters long.
# # def is_valid_id(medical_id):
# #     if medical_id.startswith("MED-") and len(medical_id) == 8:
# #         return True
# #     else:
# #         return False

# # # Task 2: Dosage Rounding
# # # Rule: Medicine is strong. Dose must be rounded to exactly 2 decimal places.
# # def calculate_precise_dose(weight, concentration):
# #     dose = weight * concentration
# #     dose = round(dose,2)
# #     return dose

# # # Task 3: Average Blood Pressure
# # # Rule: Return the average. If the list is empty, return 0 to avoid a crash.
# # def average_bp(bp_list):
# #     if bp_list== []:
# #            return 0
# #     else :
# #             total = sum(bp_list)
# #             avg = total / len(bp_list)
# #             return avg

        
    

# # # Task 4: Patient Category
# # # Rule: 0-17: "Child", 18-64: "Adult", 65+: "Senior"
# # def categorize_patient(age):
# #     if age < 18:
# #         return "Child"
# #     # if age > 18:
# #     #     return "Adult"
# #     elif age < 65:
# #          return "Adult"
# #     else:
# #         return "Senior"

# # # Task 5: Temperature Warning
# # # Rule: Return "Danger" if temp is above 40.0 OR below 35.0. 
# # # Otherwise return "Safe".
# # def temp_warning(temp):
# #     if temp > 40.0 or temp < 35.0:
# #         return "Danger"
# #     else:
# #         return "Safe"
    
#  ###########################################################################3   
# # # Task 1: Department Extractor
# # # Rule: Medical codes look like "SURG-123". Return just the department (the part before the dash).
# # def get_dept(code):
# #     # Hint: Python strings can be split
# #     parts = code.split("-")
# #     return parts[0] 

# # # Task 2: High Heart Rate Alert
# # # Rule: Given a list of heart rates, return a NEW list containing only those above 100.
# # def get_alerts(hr_list):
# #     alerts = []
# #     for hr in hr_list:
# #         if hr > 100:
# #             alerts.append(hr)
# #     return alerts

# # # Task 3: Blood Pressure Checker
# # # Rule: High BP is defined as Systolic >= 140 OR Diastolic >= 90. 
# # # Return True if high, False otherwise.
# # def is_high_bp(systolic, diastolic):
# #     if systolic >= 140 or diastolic >= 90:
# #         return True
# #     else:
# #         return False

# # # Task 4: Patient Dictionary Update
# # # Rule: You are given a dictionary. Update the 'status' to 'discharged' and return the dictionary.
# # def discharge_patient(patient_dict):
    
# #     patient_dict['status'] = 'discharged' # Bug is here
# #     return patient_dict

# # # Task 5: Recovery Percentage
# # # Rule: (Recovered / Total) * 100. Round to 1 decimal place. 
# # # Safety: If Total is 0, return 0.0.
# # def recovery_rate(recovered, total):
# #     if total == 0:
# #         return 0.0
# #     rate = (recovered / total) * 100
# #     return round(rate, 1)
# ###############################################
# # # Task 1: BMI Calculator
# # # Rule: BMI = weight / (height * height). 
# # # Note: Height is in meters. Weight in kg.
# # def calculate_bmi(weight, height):
# #     # Bug: Think about math order of operations (PEMDAS/BODMAS)
# #     bmi = weight / (height * height)
# #     return round(bmi, 1)

# # # Task 2: Glucose Level Alert
# # # Rule: Return "High" if glucose > 200, "Low" if < 70. Otherwise "Normal".
# # def glucose_check(level):
# #     if level > 200:
# #         return "High"
# #     if level < 70:
# #         return "Low"
# #     else:
# #         return "Normal"
# #     # Bug: If it's not high and not low, it should be normal.
# #     # What happens if we forget the final step?
# #     print("Normal")

# # # Task 3: Professional Name Formatter
# # # Rule: Take first name and last name, return "Last, First" (e.g., "Maswadeh, Leen")
# # def format_name(first, last):
   
# #     full_name =  last + ', ' + first
# #     return full_name

# # # Task 4: Medication Availability
# # # Rule: If stock is 1 or more, return True (Boolean). Otherwise return False (Boolean).
# # def is_available(stock_count):
# #     if stock_count >= 1:
# #         return True # Bug is here
# #     else:
# #         return False # Bug is here

# # # Task 5: Lab Result Total
# # # Rule: Sum all values in the lab_results list.
# # def sum_results(lab_results):
# #     total = 0
# #     for val in lab_results:
# #          # Bug is here
# #         total += val
# #     return total
# ################################################
# # # Task 1: Data Normalization (AI Preprocessing)
# # # Rule: Scale a value between 0 and 1 using: (value - min) / (max - min)

# # def normalize_data(value, min_val, max_val):
# #     if max_val == min_val:
# #         return 0.0
# #     result = (value - min_val) / (max_val - min_val)
# #     return round(result, 2)

# # # Task 2: Heart Rate Trend Detector
# # # Rule: Return True if the heart rate has increased for 3 consecutive readings.
# # # Example: [70, 80, 90] -> True. [70, 80, 75] -> False.
# # def detect_trend(readings):
# #     if len(readings) < 3:
# #         return False

# #     count = 0  # count of consecutive increases
# #     for i in range(1, len(readings)):
# #         if readings[i] > readings[i - 1]:
# #             count += 1
# #             if count >= 2:  # 2 increases = 3 consecutive readings
# #                 return True
# #         else:
# #             count = 0  # reset if trend breaks

# #     return False




# # # Task 3: Patient Data Parser (Dictionaries)
# # # Rule: Extract the 'blood_pressure' from a nested dictionary. 
# # # If 'medical_data' or 'blood_pressure' is missing, return "N/A".
# # def get_bp(patient_record):
# #     # Hint: Look at how we check if a key exists in a dictionary

# #      return patient_record.get('medical_data', {}).get('blood_pressure', "N/A")

# # # Task 4: Medication Conflict Checker
# # # Rule: A patient cannot take 'Med_A' and 'Med_B' at the same time.
# # # Return "Conflict" if both are in the list, otherwise "Safe".
# # def check_conflict(current_meds):
# #     found_a = False
# #     found_b = False
# #     for med in current_meds:
# #         if med == "Med_A":
# #             found_a = True
        
# #         if med == "Med_B":
# #             found_b = True

# #             if found_a and found_b:
# #                 return "Conflict"
            
# #     return "Safe"

# # # Task 5: Sorting Patients by Priority
# # # Rule: Sort a list of patients by their 'score' (Highest first).
# # def sort_by_priority(patients):
# #     # patients is a list of dicts like [{'name': 'A', 'score': 10}, ...]
  
# #     sorted_list  =  sorted(patients, key=lambda p: p['score'], reverse=True)
# #     return sorted_list
# #########################################
# #