import math  # Import the math module for mathematical operations

# Finding the area of a square
square_length = float(input("What is the length side of the square? "))  # Get the length of the square's side from the user

area = square_length ** 2  # Calculate the area of the square

print(f"The area of the square is: {area}")  # Display the area of the square

# Finding the area of a rectangle
rectangle_length = float(input("What is the length of a triangle? "))  # Get the length of the rectangle from the user (input prompt should say "rectangle")
rectangle_width = float(input("What is the width of the rectangle? "))  # Get the width of the rectangle from the user

area = rectangle_length * rectangle_width  # Calculate the area of the rectangle

print(f"The area of the rectangle is {area}")  # Display the area of the rectangle

# Finding the area of a circle
circle_radius = float(input("What is the radius of the circle? "))  # Get the radius of the circle from the user

area = math.pi * (circle_radius ** 2)  # Calculate the area of the circle

print(f"The area of the circle is {area:.1f}")  # Display the area of the circle rounded to 1 decimal place








