#Ex:1

import sys
import random

base = input("Enter the Base of a Triangle:")
height = input("Enter the Height of a Triangle:")

if not (base  and base.isdigit()):
    sys.exit()
else:
    base = int(base)

if not (height  and height.isdigit()):
    sys.exit()
else:
    height = int(height)

def area_of_triangle(b:int, h:int) -> int:
    """
    Takes two parapmetrs
    Parametrs:
        b: int
        h: int
    Returns area
    """
    area = 1/2 * b * h
    return area

print(f"The area of Triangle: {area_of_triangle(base, height)}")


#Ex:2

text = input("Write a text to reverse.\n")

def reverse(my_str:str) -> str:
    """
    Concatenate the empty string 'r_text' with the value of the iteration variable,
     which will rotate the string one letter at a time.


    Parametrs:
    my_str: str

    By end of the for loop, r_text will contain the given string in reverse order.
    
    """
    r_text = ""
    for i in my_str:
        r_text = i + r_text

    return r_text

print(f"The reversed text will be -> {reverse(text)}")


#Ex:3


sentence = input("Write a sentence and count the number of uppercase and lowercase letters in your sentence.\n\t")

def uppercase_lowercase(calculatee:int) -> int:
    """
    Given a string that contains both upper and lower case characters in it. 
    The task is to count number of upper and lower case characters in it without using in-built functions.

    Parametrs:
    calculatee: int

    Counting upper and lower case characters in a string can be done using the isupper () and islower () functions.

    By the end of the for loop, 'u_l_result' will contain the number of upper and lower case characters.

    """
    u_l_result = {"uppercase":0, "lowercase":0}
    for i in calculatee:
        if i.isupper():
           u_l_result["uppercase"]+=1
        elif i.islower():
           u_l_result["lowercase"]+=1
        else:
           pass

    return u_l_result

print (uppercase_lowercase(sentence))

#Ex:4

palindrome = input("Enter text to find out if it is a palindrome or not\n\t")

def ispalindrome(key:str) ->str:
    left = 0
    right = len(key) - 1
    
    while right >= left:
        if not key[left] == key[right]:
            return False
        left += 1
        right -= 1
    return True
print(ispalindrome(palindrome)) 


#Ex:5


check_to_play = True
rounds = 0
computer_score = 0
user_score = 0
while check_to_play:
    # write the gam
    user_choice = "test"
    # validation of input
    while user_choice not in ('1', '2', '3'):
        user_choice = input('1 for Rock 2 for Paper 3 for Scissors\n')
    else:
        user_choice = int(user_choice)
    # computer_choice
    computer_choice = random.randint(1, 3)

    if computer_choice == user_choice:
        print("It's a draw")
    elif (computer_choice == 1 and user_choice == 2) or (computer_choice == 2 and user_choice == 3)\
            or (computer_choice == 3 and user_choice == 1):
        print("You Win !!!!")
        user_score += 1
    else:
        print("You Lose ((")
        computer_score += 1
    rounds += 1

    check_input = input("Wanna play again? no for exit\n")
    if check_input == 'no':
        check_to_play = False

print(f'You have played {rounds} time and the results\nuser score - {user_score} and computer score - {computer_score}')



