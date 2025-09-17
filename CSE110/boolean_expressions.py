men = int(input("How many men are there? "))
women = int(input("How many women are there? "))

total = men + women

# Boolean Variables
total_players_must_be_7 = total == 7
total_women_must_be_4 = women == 4

if total == 7 and women ==4:
    print(f"You can play the game!")
else:
    print(f"The game rules has not been obeyed, you can't play")