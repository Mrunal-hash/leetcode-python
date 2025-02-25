"""
Statement: Generate a password

Conditions: 
1. Should contain one capital letter
2. Should contain one camel case letter
3. Should contain one number
4. Should contain one special character
5. Should be atleast 8 characters long
6. Should not have same character repeated simultaneously (more than 2 times) (Eg: 111, aaa)
"""
import random
import string

# Define the characters to be used in the string
characters = string.ascii_letters + string.digits + "@#!$%^&*"
n = int(input("Number of characters for the password: "))
# Generate a random string of length 10
random_string = ''.join(random.choice(characters) for i in range(n))

print(random_string)
