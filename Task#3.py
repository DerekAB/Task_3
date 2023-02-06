def greeting(userName):
    if len(userName) < 2:
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
            print("Username requires at least 1 number.")
            return True
    
userNameInput = input("Please enter a username. Username should have at least 1 capital letter and 1 number: ")

while greeting(userNameInput):
    userNameInput = input("Please enter a username. Username should have at least 1 capital letter and 1 number: ")