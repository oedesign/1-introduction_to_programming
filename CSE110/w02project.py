# Meal Price Calculator

# Get the price of a child's meal from the user
price_of_child_meal = float(input("What is the price of a child's meal? "))

# Get the price of an adult's meal from the user
price_of_adult_meal = float(input("What is the price of an adult's meal? "))

# Get the number of children
number_of_children = int(input("What's the total number of children? "))

# Get the number of adults
number_of_adult = int(input("what's the total number of adult? "))

# Calculate subtotal for children
sub_total_chidren = price_of_child_meal * number_of_children

# Calculate subtotal for adults
sub_total_adult = price_of_adult_meal * number_of_adult

# Calculate overall subtotal
sub_total = sub_total_chidren + sub_total_adult

# Display subtotal
print(f"Subtotal: ${sub_total}")

# Get the sales tax rate from the user
tax_rate = float(input("Sales tax rate? "))

# Calculate sales tax
sales_tax = sub_total * tax_rate / 100

# Calculate total price including tax
total_price_meal = sub_total + sales_tax

# Display total price
print(f"Total price of meal: {total_price_meal}")

# Get the payment amount from the user
payment_amount = float(input("What is the payment amount? "))

# Calculate change to give back
change = payment_amount - total_price_meal

# Display the change, formatted to two decimal places
print(f"Change: {change:.2f}")