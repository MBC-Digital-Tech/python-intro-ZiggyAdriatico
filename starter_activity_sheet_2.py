# starter program week 2 - perhaps this could be a task

def conversation():
    print("Welcome to my conversation program")
    print()

    # combine the next two lines into one command.
    answer = input("Do you like cycling? Answer yes or no ")

    # chenge this so that the user can enter YES as well.
    answerupper = answer.upper()
    if answerupper == "YES":
        print("That's good - you will get very fit")
    else:
        print("Perhaps you like some other sport. ")
    
    print("Goodbye")

# Add command here to run the function
conversation()
# Add a function to ask the user for their name and print a greeting
def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to the program.")
# Call the greet_user function
greet_user()
# Add a function to ask the user for their age and print a message
def ask_age():
    age = int(input("How old are you? "))
    print(f"You are {age} years old.")
# Call the ask_age function
ask_age()

def ask_sport():
    sport = input("What is your favorite sport? ")
    print(f"I like {sport} too!")
# Call the ask_sport function
ask_sport()

def cities():
    english = int(input("How many cities are there in England? "))
    if english == 51:
        print("Correct!")
    else:
        print("Incorrect")
cities()

def number():
    number = int(input("Enter a number bigger than 10: "))
    if number > 10:
        print("That number is bigger than 10")
    else:
        print("That number is not bigger than 10")
number()

def test_results():
    score = int(input("Enter your test score: "))
    if score >= 50:
        print("You passed the test!")
    else:
        print("You failed the test.")
test_results()

def ask_age():
    age = int(input("How old are you? "))
    if age >= 13:
        print("You can have a paper round.")
    else:
        print("You are too young for a paper round.")
ask_age()

def ask_number():
    number = int(input("Enter a number that is not 99: "))
    if number != 99:
        print("That number is not 99.")
    else:
        print("That number is 99.")
ask_number()

