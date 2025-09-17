#Writting a program that converts Fahrenheit to Celsius

fahrenheit = float(input("What is the temperature in fahrenheit? "))

celcius = (fahrenheit - 32) * 5 / 9

print(f"The temperature in celcius is {celcius:.1f} degrees")