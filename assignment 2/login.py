from password import *
from generate import *

""""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Zainab Jamil
Student ID: zjamil4
File created: October 19, 2024
******************************

This file controls the interaction between users and creating a password. It asks the user to either use the password generator or create their own password. 
The program will loop continuously until the user inputs a password that is more than or equal to the minimum strength. If the user enters "X" or "x," a 15-character 
random password is created. The strength of every password entered is checked out, and if the password satisfies the strength requirement, the associated feedback is shown. 
If it is strong enough, the software exits; if not, it requests a new input.

"""

def process_password(min_strength): #Function that processes the users password and checks if it meets minimum strength
    while True: #Loops  until a password strong enough is given
        #Ask the user to input a password or type x for a randomly generated one
        user_password = input("Type in a new password or type an X for a randomly generated password: " )

        # if user inputs 'x', a random password with the length of 15 characters will be generated.
        if user_password.lower() == "x":
            password = generate_password(15)
            strength = password_strength(password)
            print("Your password: ", password) #prints the generated password
            print("Your password has a strength of " + str(strength)) #prints the strength of the generated password
        else: #If the user enters their own password
            password = user_password
            strength = password_strength(password)
            print("You entered: ", password) #prints the user entered password
            print("Your password has a strength of " + str(strength)) #prints the strength of the user entered password

        if strength >= min_strength: #if the strength of password is more than or equal than the minimum strength, let the user know their password is strong enough
            print("Your password is strong enough! Thank you.")
            break #exit loop
        else: #if the strength of password is less than the minimum strength, let the user know their password is not strong enough.
            print("Your password is not strong enough. Please create a new password that is stronger.")
