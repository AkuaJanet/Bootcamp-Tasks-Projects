'''This is a program that displays what category the user belongs to based on their age.
Children are from ages 0 - 5 years, adults 18 - 60 years and pensioners are above 65 years.
The maximum age is 100. '''

# Request user's age and store in a variable called user_age. 
user_age = int(input("Please enter your age : "))

# Determine the conditions with the respective output

if user_age <= 5:
    print("You are classified as a child")
elif user_age <= 60:
    print("You are classified as an adult")
elif user_age >= 65 and user_age <= 100:
    print("You are classifed as a pensioner")
else:
    print("Unable to classify age, please try again!")
