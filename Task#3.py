#Name:                  Task 2.py
#Author:                Derek Baker
#Date Created:          06-02-2023
#Date Last Modified:    06-02-2023
#
#Purpose:
#
#The purpose of this program is to ask the user for a username. The program will require the user to have at least 1 capital letter and 1 number included in the username.
#The program will loop until they enter a valid username.

def greeting(userName):
    if len(userName) < 2:                                           #function that will check the username specifics and loop until a valid username is entered
        print("Username cannot be less than 2 characters.")
        return True
    if len(userName) > 20:
        print("Username cannot be longer than 20 characters.")
        return True
    if userName == userName.lower():
        print("Username should have at least 1 capital letter.")
        return True
    for char in userName:
        if char.isnumeric():
            return False
    print("Username requires at least 1 number.")
    return True

userNameInput = input("Please enter a username. Username should have at least 1 capital letter and 1 number: ")     #The first input the user will see

while greeting(userNameInput):
    userNameInput = input("Please enter a username. Username should have at least 1 capital letter and 1 number: ")     #when the user enters a name, it will go through the function to be checked
    
print("Your username is " + userNameInput.strip())      #print the user's username to them and end the program