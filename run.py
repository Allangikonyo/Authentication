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
    function that returns all the saved users
    '''
    return User.display_users()
 
# creating account functions that implements the behaviour created in user.py

def create_account(accountusername, accountname, accountpassword):

    '''
     function to create a new account
     '''
    newaccount = Credentials(accountusername, accountname, accountpassword)
    return newaccount
 
def save_account(user):
    ''''
    function to save user account info, calls save account method
    '''
    user.save_account()
 
def delete_account(user):
    '''
    function to delete user account info, calls delete account method
    '''
    user.delete_account()
 
def find_account(number):
    ''''
    function to find user account that takes in a number and calls the credentials class method
    '''
    return Credentials.find_by_number(number)
 
def display_accounts():
    ''''
    function that returns all the saved accounts 
    '''
    return Credentials.display_accounts()


def main():
    '''
    creating main function
    '''
    while True:
       print ("Welcome to Password Manager: Use these short codes to start - CA: create account OR LG :login to begin")
       print ("CA -or- LG ")

       option = input()
       if option == "CA":
        print ("Create Account")
        print ("-"*10)
        print ("Enter your First Name..")
        firstname = input()
        print ("Enter your Last Name")
        lastname = input()
        print ("Set your Username")
        username = input()
        print ("Set your password..")
        userpassword = input()
        save_user(create_user(firstname, lastname, username, userpassword)) # create new user
        print("Your account was created succesfully. Here are your account details")
        print("-"*10)
        print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}" )
        print("\nUse Login to your account with your details")
        print(" \n \n")


 


 




