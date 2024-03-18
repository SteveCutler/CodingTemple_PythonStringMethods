# Objective:
# The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and 
# last name. Both should be at least 2 characters long. If not, print an error message.

userName = input("Input your name, for example: Steve Cutler").split()

for name in userName:
    if len(name) >= 2:
        print(f"{name} is good")
        continue
    else:
        print(f"{name} is not a valid entry. Each name needs to be at least 2 characters long.")


# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. 
# The password must be at least 8 characters long, contain one uppercase 
# letter, one lowercase letter, and one number. If the password does not 
# meet these criteria, print a message explaining the complexity requirements.

password = input("Enter a new password \n")

def passwordChecker(pw):
    lengthCheck = False
    upperCheck = False
    lowerCheck = False
    numCheck = False
    if len(pw) >= 8:
        lengthCheck = True
        for char in pw:
            if char.isupper():
                upperCheck = True
            elif char.islower():
                lowerCheck = True
            elif char.isdigit():
                numCheck = True     

        if lengthCheck and upperCheck and lowerCheck and numCheck:
            print("Your password is good!")
        else:
            print("Make sure the password you enter is at least 8 characters long, contains one uppercase and one lowercase, and also contains a number.")
    else:
        print(f"Your password needs to be at least 8 characters long.")
        
passwordChecker(password)

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format

emailName = input("Please enter your name for your email address").lower().replace(" ","")


emailTemplate = "{}@codingtemple.com"
email = emailTemplate.format(emailName)
    
print(email)
