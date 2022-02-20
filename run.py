#!/usr/bin/env python3


# implementing the class in run.py 
# imported user and credentials class 
import string 
from random import *
from user import User 
from user import Credentials 

# creating user functions that implements the behaviour created in user.py

def create_user(firstname, lastname, username, userpassword):

    '''
    function to create a new user
    '''
    newuser = User(firstname, lastname, username, userpassword)
    return newuser

def save_user(user):
    ''''
    function to save user info, calls save user method
    '''
    user.save_user()

def delete_user(user):

    '''
    function to delete user info, calls delete user method
    '''
    user.delete_user()

def find_user(number):
    ''''
    function to find user that takes in a number and calls the User class method
    '''
    return User.find_by_number(number)
 
def display_users(number):
    ''''
    function taht returns all the saved users
    '''
    return User.display_users()
 
# creating user functions that implements the behaviour created in user.py




 




