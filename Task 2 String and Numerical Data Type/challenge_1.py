import math

# Ask the user to enter the length of all three sides
# of a triangle
side1 = float(input("Please enter the first length : "))
side2 = float(input("Please enter the second length : "))
side3 = float(input("Please enter the third length : "))

s = (side1 + side2 + side3) / 2

# Calculate the area
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print(f"The area of the triangle is: {area}")