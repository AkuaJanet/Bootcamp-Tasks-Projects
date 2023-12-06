import math

# Create a main menu and store it in a variable called 'menu'
menu = '''  
What would you like to calculate?
Investment - to calculate the amount of interest you will earn on your investment
Bond - to calculate the amount you will have to pain on a home loan
            
Enter either 'Investment' or 'Bond' from the menu above to proceed :  '''


# Display menu to the user and store the chosen option in a variable called 'user_choice'
user_choice = (input(menu).lower())


# If 'investment is chosen, request user to input the deposit amount, interest rate, number of years and interest type.
# Store these in variables called 'deposit' , 'interest_rate' , 'num_years' and 'interest' respectively. 
 
if user_choice == 'investment':

    deposit = float(input("Please enter the deposit amount : "))
    interest_rate = float(input("Please enter the interest rate (exclude % symbol) : ")) / 100
    num_years = int(input("Please enter the number of years : ")) 
    interest = input("Please choose if you want 'simple' or 'compound' interest : ").lower()

    # Determine and display the total amount based on the interest chosen.

    if interest == 'simple':
        simple_amount = float(deposit *(1 + interest_rate * num_years))
        print(f"The total amount is estimated to be {simple_amount} at the end of year {num_years}. ")

    elif interest == 'compound':
        compound_amount = round((deposit * math.pow((1 + interest_rate), num_years)), 2)
        print(f"The total amount is estimated to be {compound_amount} at the end of year {num_years}. ")

    else:
        print("Error! Please choose either 'simple' or 'compound' interest : ")


# If 'bond' is chosen, request user to input the present value of the house, interest rate, and the number of 
# months they plan to take to repay the bond and store in variables called 'present_value' , 'interest_rate' and 'num_month' respectively.  

elif user_choice == 'bond':

    present_value = float(input("Please enter the present value of the house : "))
    interest_rate = float(input("Please enter the interest_rate (exclude % symbol) : ")) / 100
    num_month = int(input("Please enter the number of months for repayment : "))

    # Divide interest rate by 12 to get monthly rate
    new_interest = float(interest_rate / 12)

    # Display the amount the user will have to repay each month
    monthly_pay = round((new_interest * present_value) / (1 - (1 + new_interest) ** (-num_month)), 2)
    print(f"For {num_month} months, the amount to repay each month will be {monthly_pay} ")

else:
    print("Error! Please choose either 'investment' or 'bond' : ")




