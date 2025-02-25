"""
Statement: Check if the password satisfies below condition.

Conditions: 
1. Should contain one capital letter
2. Should contain one camel case letter
3. Should contain one number
4. Should contain one special character
5. Should be atleast 8 characters long
6. Should not have same character repeated simultaneously (more than 2 times) (Eg: 111, aaa)
"""
import re 
from itertools import groupby
from cryptography.fernet import Fernet
import pyautogui

# Function to check sequential characters
def sequence_identifier(password):

    res = [''.join(g) for k, g in groupby(password)]

    for i in res:
        if len(i) > 1:
            return False
    return True

# Function to verify password requirements
def password_check(password):
    if len(password) < 8: 
        print("Password should contain minimum 8 characters.")
        return False
    elif re.search('[0-9]',password) is None:
        print("Password should contain a digit from 0-9")
        return False
    elif re.search('[A-Z]', password) is None:
        print("Password should contain a character from A-Z")
        return False
    elif re.search('[a-z]',password) is None:
        print("Password should contain a character from a-z")
        return False
    elif re.search('[!@#$%&]',password) is None:
        print("Password should contain a special character")
        return False
    elif sequence_identifier(password) is False:
        print("Password should not contain repititive characters")
        return False
    return True

# function to encrypt a password
def encrypt(password,key):
    text = Fernet(key)
    encrypted_text = text.encrypt(password.encode())
    return encrypted_text

while True:
    # Take the password input
    # password = input("Please enter your password: ")
    password = pyautogui.password(text='', title='', default='', mask='*')

    check = password_check(password)

    # condition if password is correct
    if check:
        key = Fernet.generate_key()
        encrypt_pwd = encrypt(password,key)
        print("Your password is: " ,encrypt_pwd)
        break
    # if password is incorrect
    else:
        print("Try again!")
        
