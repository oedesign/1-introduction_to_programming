# Ask the user for their age and convert the input to an integer
age = int(input("How old are you? "))

# Calculate the age on the user's next birthday
next_birthday = 1 + age

# Print a message about the user's next birthday
print(f"YAY! You will be {next_birthday} in your next birthday, Happy birthday in advance!")

# Ask the user for the total number of egg cartons and convert the input to an integer
total_cartons = int(input("What is the total number of Egg cartons you have? "))

# Calculate the total number of eggs (12 eggs per carton)
total_num_of_eggs_in_a_cartons = 12 * total_cartons

# Print the total number of eggs
print(f"In a carton they are 12 eggs, so the total number of eggs you have is {total_num_of_eggs_in_a_cartons}")

# Ask the user for the number of cookies and people, and convert inputs to integers
number_of_cookies = int(input("Number of Cookies? "))
number_of_people = int(input("Number of people? "))

# Calculate how many cookies each person gets (may be a float)
cookies_each_person_get = number_of_cookies / number_of_people

# Print how many cookies each person gets
print(f"Each person get {cookies_each_person_get}")