print("Version 1 : ")
# Create a sentence and store it in a variable called "message"
message = "I am starting to get a hang of this"

# Create a variable called alt_message and make it an empty string. 
# This is the variable that will store the new sentence. 
alt_message = ""   

# Determine and print out the output using for loop and if-else statement
for char in range(len(message)):
    if char % 2 == 0:
        alt_message += message[char].upper()
    else:
        alt_message += message[char].lower()

print(alt_message)

print(" ")

print("Version 2 : ")
# Split the variable message into a list and store in a variable called "index_word"
index_word = message.split()

# Create a variable called "new_message" and make it an empty string. 
# This is the variable that will store the new version of the sentence. 
new_message = ""

# Determine and print out the output using for loop and if-else statement
for word in range(len(index_word)):
    if word % 2 == 0:
        new_message += index_word[word].upper() + " "
    else:
        new_message += index_word[word].lower() + " "

print(new_message.strip())