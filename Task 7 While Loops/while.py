# Get user to input a number and store as 'user_num'

user_num = int(input("Please enter a number : "))

count = 0    # set initial count value to zero
total = 0    # set initial toatl value to zero

# Set the condition to commence the loop

while user_num != -1:

    count += 1             # Count increment by 1
    total += user_num      # Total increases by the addition of each number entered

    print(f"Count is {count}") 
    print(f"Total is {total}")

    print("Please try again! ")
    user_num = int(input("Enter another number (or -1 to stop) : "))

    # Set output for when the loop condition is met

    if user_num == -1:
        avg_num = round((total / count), 2)
        print(f'''
Very well! I shall cease!
Here is the average : {avg_num}
''')
