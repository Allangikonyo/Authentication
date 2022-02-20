'''
create a class that holds instance objects for our users
'''

class User:
#  create a empty list to track user data 

    userlist= [] # class attribute that can be accessed directly through the class (User.userlist)

    def __init__(self, firstname, lastname, username, password):
        '''
        create init method to intialize necessary attributes 
        '''

        self.firstname = firstname
        self.lastname = lastname 
        self.usernmae = username 
        self.password = password 

    def save_user(self):
        '''
        create method to add user info into our userlist 
        '''

        User.userlist.append(self) 

    def delete_user(self):

        '''
         method deletes user info from our userlist

        '''
        User.userlist.remove(self)
    @classmethod
    def display_users(cls):
        '''
        class method that returns all user info stored in class list 
        '''
        return cls.userlist

    @classmethod
    def find_by_number(cls, number):

        '''
        a class method that finds the user that based on their number
        '''

        for user in cls.userlist:
            if user.password == number:
                return user

    @classmethod
    def user_exist(cls, number):

        '''
        a class method that tests whether the user exists 
        '''
        for user in cls.userlist:
            if user.username == number:
                return True 
            else:
                return False

'''
create a class that generates new instances of credentials 
'''

class Credentials: 
#  create a empty list to track account credentials data 

    accounts= [] # class attribute that can be accessed directly through the class (credentials.accounts)

    def __init__(self, accountusername, accountname, accountpassword):
        '''
        create init method to intialize necessary attributes 
        '''

        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword

    def save_account(self):
        '''
        create method to add account info into our accountlist 
        '''

        Credentials.accounts.append(self) 

    def delete_account(self):

        '''
         method deletes user account from our accountist

        '''
        Credentials.accounts.remove(self)


 



   



