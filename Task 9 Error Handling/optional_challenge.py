# This is a program that outputs the average of even numbers from 0 to 100. 

numbers = range(100) # This will give a logical error in the end because 100 will not be included in this range. 
count = 0
total = 0

for num in numbers:
    if num % 2 == 0:
        total += count
        print(f" Current number : {num}, count: {count}")

# Runtime error here because count was not updated in the loop so it remained at zero.
# Logical error as well because total should be the summation of all even numbers from 0 to 100. 
average_num = total/count  
print(f"The average is {average_num}")
