"""This is a python program demonstrating user-defined functions"""

# Start by importing random module for one of the functions.
import random as rd

# Create a function called hotel_cost which takes one parameter that
# represents the number of nights in the hotel. The logic is to multiply
# the number of nights by a fixed price, store the result in a variable
# called total_cost and return this variable

def hotel_cost(nights):
    total_cost = nights * 65
    return total_cost

# Create a function called plane_cost which takes one parameter that
# represents the destination. Randomize the cost which is stored in a variable
# called city, then return this variable
def plane_cost(city):
    if city == 'Abidjan':
        city = rd.randint(999, 1999)
        return city
    elif city == 'Accra':
        city = rd.randint(1499, 2999)
        return city
    elif city == 'Cairo':
        city = rd.randint(899, 1599)
        return city
    elif city == 'Lagos':
        city = rd.randint(1599, 3999)
        return city
    elif city == 'Nairobi':
        city = rd.randint(1099, 2499)
        return city
    elif city == 'Marrakesh':
        city = rd.randint(1199, 1799)
        return city

# Create a function called car_rental which takes one parameter that
# represents the number of days a car will be hired. The logic is to multiply
# the number of days by a fixed price, store the result in a variable called
# rental_cost, then return this variable
def car_rental(days):
    rental_cost = days * 20
    return rental_cost

# Create a function called holiday_cost which takes three parameters that
# represent the hotel cost, plane cost and rental cost. The logic is to sum up
# the respective functions, store the result in a variable called overall_cost,
# then return this variable
def holiday_cost(nights, city, days):
    overall_cost = hotel_cost(nights) + plane_cost(city) + car_rental(days)
    return overall_cost

# Create a welcome menu for the user and display the destination cities.
print('''Welcome to Serenity. Your personal holiday planner. \
Here are the destinations we currently offer below:
Abidjan
Accra
Cairo
Lagos
Nairobi
Marrakesh
''')

# Create a list of cities
cities = ['Abidjan' ,'Accra', 'Cairo', 'Lagos', 'Nairobi', 'Marrakesh']

# Start a while loop to take in the user's inputs and display appropriate outputs.
while True:

    # Request user to input a city from the options.
    city_flight = input("Please choose your destination from the cities given: ").capitalize()

    # Use if-else statement to verify user's input then calculate the flight amount
    # or display an error message accordingly.
    if city_flight in cities:

        flight_amount = plane_cost(city_flight)
        print(f"The cost of your flight to {city_flight} is £{flight_amount:.2f}")

    else:

        print("You have entered an incorrect value, please choose a city \
from the options!")
        continue

    # Request user to input the number of nights at the hotel
    num_nights = input("Please enter the number of nights you will be \
spending at the hotel : ")

    # Use if-else statement to verify the input then display an error message
    # or calculate the hotel cost accordingly.
    if not num_nights.isdigit():

        print("You have entered an incorrect value, please try again!")
        continue

    else:

        total_nights = hotel_cost(int(num_nights))
        print(f"The cost for {num_nights} nights is £{total_nights:.2f}")

    # Request user to input the number of days they will hire a car for.
    rental_days = input("Please enter the number of days for which you \
will be hiring a car : ")

    # Use if-else statement to verify the input then display an error message
    # or calculate the car rental cost accordingly.
    if not rental_days.isdigit():

        print("You have entered an incorrect value, please try again!")
        continue

    else:

        total_days = car_rental(int(rental_days))
        print(f"The cost for hiring the car for {rental_days} days \
is £{total_days:.2f}")

    # Create a value called overall_cost which sums up the cost of the flight,
    # hotel and car rental. 
    overall_cost = flight_amount + total_nights + total_days

    print(f"The overall cost of your trip is £{overall_cost:.2f}. \
Enjoy your trip and thank you for choosing Serenity.")
    break
