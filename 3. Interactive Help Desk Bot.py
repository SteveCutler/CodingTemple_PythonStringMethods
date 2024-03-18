# Objective:
# The aim of this assignment is to create an interactive help desk bot 
# that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it 
# contains one of the predefined commands (e.g., "help", "issue", "contact support"). 
# If a command is found, print a response related to the command.

commands = ["help", "issue", "contact support"]
userCommand = input("Please enter your command.\n")

for word in commands:
    if word.lower() in userCommand.lower():
        if word.lower() == "help":
            print("What can I help you with?")
        elif word.lower() == "issue":
            print("What seems to be the issue?")
        elif word.lower() == "contact support":
            print("You can contact support at: info@CodingTemple.com")
    else:
        continue

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue 
# based on keywords such as "login", "performance", "error", etc. Print out 
# the category of the issue for the support team.
        
commands = ["help", "issue", "contact support"]
userCommand = input("Please enter your command.\n")
issueCategories = ["login", "performance", "error"]

for word in commands:
    if word.lower() in userCommand.lower():
        if word.lower() == "help":
            print("What can I help you with?")
        elif word.lower() == "issue":
            for category in issueCategories:
                if category in userCommand.lower():
                    print(f"@support: Issue '{userCommand}' corresponds to category {category.upper()}")
                else:
                    continue
        elif word.lower() == "contact support":
            print("You can contact support at: info@CodingTemple.com")
    else:
        continue
