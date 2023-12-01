# Request user to input name of favorite restaurant
# and store into variable called "string_fav"

string_fav = input("Please enter the name of your favorite restaurant : ")

# Request user to input favorite number and store as an integer 
# variable called "int_fav"

int_fav = int(input("Please enter your favorite number : "))

print(string_fav)
print(int_fav)

print(int(string_fav))  # This came back as an error because "string_fav" is not a numeric value