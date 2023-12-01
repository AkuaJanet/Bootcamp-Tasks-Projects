# Request user to input their age and store it in a variable called "age"
age = int(input("Please enter your age : "))

# Create conditions and messages for each age category 
if age > 100:
    print("Sorry, you're dead")
elif age >= 65:
    print("Enjoy your retirement")
elif age >= 40:
    print("You're over the hill")
elif age == 21:
    print("Congrats on your 21st")
elif age < 13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number")