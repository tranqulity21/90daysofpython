#create a password checker for me that does the following
#checks the password length is at least 6 characters long
#check whether it includes an uppercase,lowercase,a digit and a special character
#ask for user email to make sure there's no relation with the passowrd input
def password_checker(password):
  #we assign the variable has_digit to
  #any() is a built in function that checks through the list if any has the quality needed
  #.isdigit() checks if all char in a string are digits an returns true or false
  #for char in password loops through all the characters to find a digit
  has_digit = any(char.isdigit() for char in password)
  has_uppercase = any(char.isupper() for char in password)
  has_lower = any(char.islower() for char in password)
  #.isalnum() method returns True if all characters in the string are alphanumeric else false
  has_specialchar = any(not char.isalnum() for char in password)
  length_greater_than_six = len(password) > 6
  return has_digit and has_uppercase and has_lower and has_specialchar and length_greater_than_six
password = input("check if your password is strong: ")
if password_checker(password):
  print("strong password!")
else:
 print("weak password!")
    
