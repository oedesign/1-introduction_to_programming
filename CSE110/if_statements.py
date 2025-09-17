# The "IF" statement in python 

# temperature = float(input("What is your temperature in degree celcius? "))

# if temperature > 40.5:
#     print("Please, go to the hospital!")
# elif temperature > 39.4:
#     print("Please, call your doctor!")
# else:
#     print("Have a rest for the day!")

# print(f"Your temperature is {temperature}, have a good day!")

# seyi = input("Gender: ")
# seyi_gender = seyi.lower()

# if seyi_gender == "boy":
#   print(f"Seyi is a {seyi_gender}")
# else:
#   print("unknown gender")

animal = input("Enter the name of an animal: ")
animal_s = animal.lower()

sound = ""

if animal_s == "dog":
    sound = "bark"
elif animal_s == "cat":
     sound = "meo"
elif animal_s == "hen":
     sound = "clock"
else:
     sound = "sound unknown"

print(f"The {animal_s} sound is {sound}.")