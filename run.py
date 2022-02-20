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

       elif option == "LG":
         print(" your username..")
         loginUsername = input()
         print ("your Password..")
         loginPassword=input ()

         if find_user(loginPassword):
            print("/n")
            print ("your can create multiple accounts (MC) and also view them (VC)")
            print ("-"*60)
            print("MC -or- VC")
            choose= input ()
            print ("/n")
            if choose == "MC":
                print("Add Your Account")
                print ("-" *25)
                accountusername = loginUsername
                print("Account Name")
                accountname= input()
                print("\n")
                print("Generate automatic password (A) or Create new password(C)?")
                decision = input()
                if decision == "A":
                    characters=string.ascli_letters + string.digits
                    accountpassword= "" .join(choice(characters)for x in range(randint(6,16)))
                    print("Password: {accountpassword}")
                elif decision == "C":
                    print("Enter your Password")
                    accountpassword= input()
                else:
                       print("please enter a valid password")

                save_account(create_account(accountusername, accountname, accountpassword))
                print("\n")
                print(f"Username: {accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")

            elif choose == "VC":
                if find_account(accountusername):
                     print("Here is a list of yout created accounts: ")
                     print("-"*25)
                     for user in display_accounts():
                         print (f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")
 
                else:
                     print("Invalid credentials")
 
            else:
                 print("Please try again")
                 print("/n")
 
         else:
               print("Invalid username or password please try again!")
               print("\n")
      
       else:
        print("Kindly choose a valid option")
        print("\n")
 
if __name__ == "__main__":
   main()





 


 




