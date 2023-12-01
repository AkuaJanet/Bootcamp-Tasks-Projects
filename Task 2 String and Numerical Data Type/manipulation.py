# Ask the user to enter a sentence
str_manip = input("Please enter a sentence : ")

# Calculate and display the length of str_manip
print(len(str_manip))

# Find the last letter in str_manip sentence
last_letter = str_manip[-1]

# Replace every occurence of the last letter wuth @
print(str_manip.replace(last_letter , "@"))

# Print the last 3 characters in str_manip backwards
last_three_backwards = str_manip[-3:][::-1]
print(last_three_backwards)

# Create a five-letter word that is made up of the first three
# characters and the last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print(five_letter_word)