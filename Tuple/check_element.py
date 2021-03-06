'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 11:28:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 11:28:38  
 @Title : check whether an element exists within a tuple
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def exist_element(given_tuple,element):
    """
    Description:
        this function is define for check whether an element exists within a tuple
    Parameter:
        given_tuple (tuple) : user defined tuple
    Return:
        True (boolean) : if exist
        False (boolean) : if not exist
    """
    if element in given_tuple:
        return True
    else:
        return False


def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call exist_element
    Parameter:
        None
    Return:
        None
    """
    given_tuple=(1,2,3,4,5,6,7,8,9,10)
    try:
        element=int(input("=================================================\nenter element: "))
        print("========================== repeatative element tuple here ==========================\nelement {0} is in {1} ? {2}".format(element,given_tuple,exist_element(given_tuple,element)))
        loggerfile.Logger("info","successfully check element in tuple")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()