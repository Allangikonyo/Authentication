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
        delete_user method deletes a saved user from the userlist
        '''

 



   



