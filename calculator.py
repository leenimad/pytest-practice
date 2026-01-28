# def future_age(age_input):
#     # This will crash if age_input is a string!
#     return int(age_input) + 10
#  case sensitivity : 
# def get_gender(letter):
#     if letter.lower() == "m":
#         return "Male"
#     elif letter.lower() == "f":
#         return "Female"
#     else:
#         return "Unknown"

# def count_high_hr(hr_list):
#     count = 0
#     for hr in hr_list:
#         if hr > 100:
#             count = count + 1
#     return count # BUG: This is inside the loop!

# def needs_urgent_care(temp, is_dehydrated):
#     # Requirement: BOTH must be true to be "Urgent"
#     if temp > 37.5 and is_dehydrated == True:
#         return "Urgent"
#     else:
#         return "Normal"
    
# print (needs_urgent_care(38,False))    
# Task 1: Medical ID Validator
# Rule: ID must start with "MED-" and be exactly 8 characters long.
def is_valid_id(medical_id):
    if medical_id.startswith("MED-") and len(medical_id) == 8:
        return True
    else:
        return False

# Task 2: Dosage Rounding
# Rule: Medicine is strong. Dose must be rounded to exactly 2 decimal places.
def calculate_precise_dose(weight, concentration):
    dose = weight * concentration
    dose = round(dose,2)
    return dose

# Task 3: Average Blood Pressure
# Rule: Return the average. If the list is empty, return 0 to avoid a crash.
def average_bp(bp_list):
    if bp_list== []:
           return 0
    else :
            total = sum(bp_list)
            avg = total / len(bp_list)
            return avg

        
    

# Task 4: Patient Category
# Rule: 0-17: "Child", 18-64: "Adult", 65+: "Senior"
def categorize_patient(age):
    if age < 18:
        return "Child"
    # if age > 18:
    #     return "Adult"
    elif age < 65:
         return "Adult"
    else:
        return "Senior"

# Task 5: Temperature Warning
# Rule: Return "Danger" if temp is above 40.0 OR below 35.0. 
# Otherwise return "Safe".
def temp_warning(temp):
    if temp > 40.0 or temp < 35.0:
        return "Danger"
    else:
        return "Safe"