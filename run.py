#!/usr/bin/env python3


# implementing the class in run.py 
# imported user and credentials class 
import string 
from random import *
from user import User 
from user import Credentials 

# creating functions that implement the behaviour created 

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


 




