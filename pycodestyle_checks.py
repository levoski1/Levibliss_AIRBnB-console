#!/usr/bin/python3

"""
this code get get the user name and welcome him/her to the AIRBnB console project
"""

def name():
    # function that accept users name
    name = str(input('Enter your fucking name '))

    name = f"{name}! Welcome to our first AIRBnB Project."
    return name


print(name())
