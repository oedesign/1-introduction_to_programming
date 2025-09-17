import math

#Finding the area of a square
square_length = float(input("What is the length side of the square? "))

area = square_length **2

print(f"The area of the square is: {area}")

#Finding the area of a rectangle
rectangle_length = float(input("What is the length of a triangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))

area = rectangle_length * rectangle_width

print(f"The area of the rectangle is {area}")

#Finding the area of a circle
circle_radius = float(input("What is the radius of the circle? "))

area = math.pi * (circle_radius **2)

print(f"The area of the circle is {area:.1f}")








