# Request the input of the time taken for each event of the triathlon
swimming = int(input("Please enter the swim time : "))
cycling = int(input("Please enter the cycling time : "))
running = int(input("Please enter the run time : "))

# Calculate the total time
total_time = swimming + cycling + running 

# Output the total time
print(f"Your total time is {total_time} minutes")

# Determine the conditions for which award to be given based on total time taken. 
if total_time <= 100:
    print("Congratulations! You have been granted the award Provincial Colours.")
elif total_time >= 101 and total_time <= 105:
    print("Congratulations! You have been granted the award Provincial Half Colours.")
elif total_time >= 106 and total_time <= 110:
    print("Congratulations! You have been granted the award Provincial Scroll.")
elif total_time >= 111:
    print("Great effort! Please try again next time to qualify for an award.")