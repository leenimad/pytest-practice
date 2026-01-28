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

def needs_urgent_care(temp, is_dehydrated):
    # Requirement: BOTH must be true to be "Urgent"
    if temp > 37.5 and is_dehydrated == True:
        return "Urgent"
    else:
        return "Normal"
    
print (needs_urgent_care(38,False))    