import unittest # Importing the unittest module
from user import user # Importing the user class


class Testuser(unittest.Testcase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = user("Allan", "Gikonyo", "2022")

def test_init(self):
    
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.user_name, "Allan")

def test_save_user(self):

    '''
    test_save_contact test case to test if the contact object is saved into the contact list
    '''
    self.new_user.save_user()
    self.assertEqual(len(user.user_list), 1)



