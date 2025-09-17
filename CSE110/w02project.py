# Meal Price Calculator

price_of_child_meal = float(input("What is the price of a child's meal? "))
price_of_adult_meal = float(input("What is the price of an adult's meal? "))

number_of_children = int(input("What's the total number of children? "))
number_of_adult = int(input("what's the total number of adult? "))

sub_total_chidren = price_of_child_meal * number_of_children
sub_total_adult = price_of_adult_meal * number_of_adult

sub_total = sub_total_chidren + sub_total_adult

print(f"Subtotal: ${sub_total}")

tax_rate = float(input("Sales tax rate? "))

sales_tax = sub_total * tax_rate / 100

total_price_meal = sub_total + sales_tax

print(f"Total price of meal: {total_price_meal}")

payment_amount = float(input("What is the payment amount? "))

change = payment_amount - total_price_meal

print(f"Change: {change:.2f}")