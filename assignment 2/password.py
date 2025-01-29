""""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Zainab Jamil
Student ID: zjamil4
File created: October 19, 2024
******************************

This file has two primary functions for determining the strength of a password and examining what it contains.
How many of the four specified character groups from lowercase, uppercase, digits, and symbols are included in a password
that is determined by the first function. Using the helper, the second function checks the password's overall strength
by looking at its length and the range of character groups it contains. The password is automatically assigned the lowest
strength score if it contains invalid characters such as spaces, tabs, or newlines.

"""

def count_groups(pwd): #function to count number of groups in the user password
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz" #check for lowercase letter in password
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #check for uppercase letter in password
    DIGITS = "0123456789" #check for digit in password
    SYMBOLS = "!@#$%^&*/?-+=,.|~" #check for symbol in password

    #Initialize boolean flags to check for different character groups in password
    has_lowercase = False #Will be True if the password has a lowercase letter
    has_uppercase = False #Will be True if the password has an uppercase letter
    has_digits = False #Will be True if the password has a digit
    has_symbols = False #Will be True if the password has a symbol

    #loops through each character in password
    for char in pwd:
        if char in LOWERCASE:
            has_lowercase = True
        elif char in UPPERCASE:
            has_uppercase = True
        elif char in DIGITS:
            has_digits = True
        elif char in SYMBOLS:
            has_symbols = True

    return int(has_lowercase) + int(has_uppercase) + int(has_digits) + int(has_symbols) # return number of groups found

def password_strength(pwd): #function to determine strength of password
    length_pwd = len(pwd) # calculate length of password
    num_groups = count_groups(pwd) # count number of groups

    if any(char in pwd for char in ["\n", "\t", " "]): #if function detects a new line, tab, or space then password has strength of 0
        return 0

    if length_pwd < 5: #if password is less than 5 characters, password has a strength of 0
        return 0

    elif 5 <= length_pwd <= 8: #if password is in between 5-8 characters, password has a strength of 1, 2 or 3 based on number of groups
        if 0 <= num_groups <= 1:
            return 1
        elif 2 <= num_groups <= 3:
            return 2
        else:
            return 3

    elif 9 <= length_pwd <= 12: #if password is in between 9-12 characters, password has a strength of 2, 3 or 4 based on number of groups
        if 0 <= num_groups <= 1:
            return 2
        elif 2 <= num_groups <= 3:
            return 3
        else:
            return 4
    else: #if password is more than 12 character, password has a strength of 3, 4 or 5 based on number of groups
        if 0 <= num_groups <= 1:
            return 3
        elif 2 <= num_groups <= 3:
            return  4
        else:
            return 5












