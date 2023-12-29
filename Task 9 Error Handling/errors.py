# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


print("Welcome to the error program")  # Syntax error : fixed missing parentheses. 
print("\n")   # A syntax error : fixed incorrect identation and missing parentheses.

# Variables declaring the user's age, casting the str to an int, and printing the result

age_Str = "24"  # Syntax error : fixed incorrect identation and variable assignment operator.

age = int(age_Str)    # Runtime error : cannot cast alphabets to integer. Fixed by removing "years old".

print("I'm" + " " + str(age) + " " + "years old.") # Syntax and runtime error : cannot concantenate integer and no spacing. 
# Fixed by casting to string and added spaces. 


# Variables declaring additional years and printing the total years of age

years_from_now = 3   
total_years = age + years_from_now  # Runtime error : cannot concatenenate integer and string. 
# Fixed by changing "3" to 3.    

print(f"The total number of years: {total_years}") # Syntax and logical error : missing parentheses and unknown variable. 
# Fixed by adding parentheses, correct variable name and f-string. 


# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = (total_years * 12) + 6   # Runtime and logical errors. # Fixed by using correct variable name and formula

print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")  # Runtime error : cannot concatenenate integer and string.
# Fixed by casting integer to string. 

#HINT, 330 months is the correct answer