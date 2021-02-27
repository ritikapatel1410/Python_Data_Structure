'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 19:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 19:40:38  
 @Title : find reverse string of given string
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def reverse_string(user_defined_string):
    """
    Description:
        this function is define find reverse string of given string
    Parameter:
        user_defined_string (str) : user defined string
    Return:
        reversed string of given string
    """
    return user_defined_string[::-1]

def main():
    """
    Description:
        this main function for user defind string and call reverse_string function
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defined_string=input("========================================\nenter string: ")
        print("==============================================\nreversed string: {0}".format(reverse_string(user_defined_string)))
        loggerfile.Logger("info","successfully find reversed string")
        print("=========================== program finish here =============================")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   