# Create a variable called sentence and assign it the string - The!quick!brown!fox!jumps!over!the!lazy!dog.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace "!" with a blank space and reprint the sentence.
new_sentence = sentence.replace("!" , " ")
print(new_sentence)

print(sentence.replace("!" , " ")) #This is just to show the alternative to replace "!" with a blank space and reprint. 

# Reprint the sentence as THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
print(sentence.upper().replace("!", " ")) 

# Reprint the sentence in reverse
print(sentence[ : : -1])
