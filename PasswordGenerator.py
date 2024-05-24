import re
import random

def password_generator(CharacterAmount, SpecialCharacters, Numbers, UpperCase):

    #Lists of characters
    SpecialCharactersList = "!@#$%^&*()_-+=<>?"
    NumbersList = "0123456789"
    UpperCaseList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LowerCaseList = "abcdefghijklmnopqrstuvwxyz"

    #The generated password
    Password = ""

    for i in range(CharacterAmount):
        X = random.randint(0, 3)

        #If the user wants special characters, numbers, or uppercase letters in their password, the program will add them to the password
        if SpecialCharacters == True and X == 0:
            Password += SpecialCharactersList[random.randint(0, 13)]
        elif UpperCase == True and X == 1:
            Password += UpperCaseList[random.randint(0, 25)]
        elif Numbers == True and X == 2:
            Password += NumbersList[random.randint(0, 9)]
        elif X == 3:
            Password += LowerCaseList[random.randint(0, 25)]
        else:
            Password += LowerCaseList[random.randint(0, 25)]

    print(f"Your password is: {Password}")

#User input
while True:
    Characteramount_Input = input("How many characters do you want in your password? ")

    #If the user enters a valid number, the program will break out of the loop
    if re.match("^[0-9]+$", Characteramount_Input):
        Characteramount_Input = int(Characteramount_Input)
        break
    else:
        print("Please enter a valid number")

while True:
    SpecialCharacters_Input = input("Do you want special characters in your password? ")

    #If the user enters a valid answer, the program will break out of the loop
    if re.match("^(Ye?s?|ye?s?)$", SpecialCharacters_Input):
        SpecialCharacters_Input = True
        break
    elif re.match("^(No?|no?)$", SpecialCharacters_Input):
        SpecialCharacters_Input = False
        break
    else:
        print("Please enter a valid answer")

while True:
    Numbers_Input = input("Do you want numbers in your password? ")

    if re.match("^(Ye?s?|ye?s?)$", Numbers_Input):
        Numbers_Input = True
        break
    elif re.match("^(No?|no?)$", Numbers_Input):
        Numbers_Input = False
        break
    else:
        print("Please enter a valid answer")

while True:
    UpperCase_Input = input("Do you want uppercase letters in your password? ")

    if re.match("^(Ye?s?|ye?s?)$", UpperCase_Input):
        UpperCase_Input = True
        break
    elif re.match("^(No?|no?)$", UpperCase_Input):
        UpperCase_Input = False
        break
    else:
        print("Please enter a valid answer")

password_generator(Characteramount_Input, SpecialCharacters_Input, Numbers_Input, UpperCase_Input)