print("Welcome to the quiz gmae\n")
score = 0

user_input = input("Do you want to start the game? \n").lower()

if user_input == 'yes':
    print("Let's goooo....\n")
else:
    quit()

user_input = input("\nWhat is the name of the capital of Bangladesh? \n").lower()
if user_input == 'dhaka':
    print("Correct")
    score += 1
else:
    print("Incorrect")

user_input = input("\nWhat is the name of the mother company of ChatGPT? \n").lower()
if user_input == 'openai':
    print("Correct")
    score += 1
else:
    print("Incorrect")

user_input = input("\nWhat is the full form of LLM? \n").lower()
if user_input == 'large language model':
    print("Correct")
    score += 1
else:
    print("Incorrect")

user_input = input("\nWho is the father of AI? \n").lower()
if user_input == 'geoffrey hinton':
    print("Correct")
    score += 1
else:
    print("Incorrect")

user_input = input("\nWhat is the full form of RAM? \n").lower()
if user_input == 'random access memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("\nYou have scored " + str(score) + " points")