"""This is a python program demonstrating the use of list and dictionaries"""

# Create a list of items sold in a cafe.
menu = ['coffee', 'tea', 'muffin', 'sandwich', 'panini']

# Create a dictionary to show the stock of each item.
stock = {
    'coffee' : 25,
    'tea' : 30,
    'muffin' : 20,
    'sandwich' : 18,
    'panini' : 15
    }

# Create a dictionary to show the price of each item.
price = {
    'coffee' : 4,
    'tea' : 2,
    'muffin' : 5,
    'sandwich' : 8,
    'panini' : 6
    }

# Create a variable called total_stock and assign an initial value of zero.
total_stock = 0

# Use for loop to iterate through the menu list and calculate the total value
# of each item by referencing the dictionary keys.
# With each iteration, total_stock increases with the value of item_total.
for item in menu:

    item_total = stock[item] * price[item]
    total_stock += item_total

    print(f"The total value of {item} in stock is £{item_total:.2f}")

print("")

print(f"The overall worth of all items in the cafe is £{total_stock:.2f}")
