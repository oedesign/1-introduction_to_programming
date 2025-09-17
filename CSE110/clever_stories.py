# Writing 'Mad Libs' in Python

# Collecting user inputs
adjective = input("Enter an adjective: ").lower()
animal = input("Enter the name of an animal: ").title()
verb1 = input("Enter a verb: ").lower()
exclamation1 = input("Enter an exclamation: ").upper()
verb2 = input("Enter another verb: ").lower()
verb3 = input("Enter one more verb: ").lower()
exclamation2 = input("Enter another exclamation: ")
noun = input("Enter a noun: ")
pronoun = input("Enter a pronoun: ")
verb4 = input("Enter a final verb: ").lower()

# Printing the story
print(f"""
MAD LIBS

The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. 
"{exclamation1}!" I yelled. But all I could think to do was to {verb2} over and over. 
Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family. 
{exclamation2.upper()}! My {noun.title()} nearly freaked out when {pronoun.title()} {verb4} the {animal} coming after us. 

THE END
""")
