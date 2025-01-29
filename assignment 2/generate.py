import random

""""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Zainab Jamil
Student ID: zjamil4
File created: October 19, 2024
******************************

this file contains a function that generates a random password of a length that is specified. 
The password is generated using characters from four specified character groups: lowercase, uppercase, numbers, and symbols.
The function creates the password by selecting random characters from these groups one at a time
using the random library, and then it returns the entire string.

"""

def generate_password(length): #Function to generate random password of a certain length using a mix of all the groups
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz" #lowercase letters string
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #uppercase letters string
    DIGITS = "0123456789" #digits string
    SYMBOLS = "!@#$%^&*/?-+=,.|~" #symbols string

    # combining all groups of strings into one string
    ALL_CHARS = (LOWERCASE + UPPERCASE + DIGITS + SYMBOLS)

    random_pwd = "" #Initialize empty string to hold generated password

    #loop through the strings one by one and build a password
    for _ in range(length):
        random_char = random.choice(ALL_CHARS)
        random_pwd += random_char

    return random_pwd #once loop is complete, return generated password