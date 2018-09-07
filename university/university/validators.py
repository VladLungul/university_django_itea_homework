import re

def phone_validation(phone:str):
   # if phone_number = RegexValidator(regex=r'^\+?1?\d{13,15}$',
    #                             message="Phone number must be entered in the format: '+9999999999999'.")
    #return phone_number
    #True => errors
    #False => not errors
    is_match = re.match(r'^\+?1?\d{13,15}$', phone)
    return is_match


#r'^\+[\d][7,15]$'