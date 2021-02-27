'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 13:50:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 13:50:38  
 @Title : replace string character problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def replace_character(user_defined_string):
    """
    Description:
        this function is define for replace string character problem 
    Parameter:
        user_defined_string (str) : string taken from user
    Return:
        modified_string : user_defined_string after replacing 
    """
    modified_string=user_defined_string[0]+user_defined_string[1:].replace(user_defined_string[0],"$")
    return modified_string

def main():
    """
    Description:
        this main function for take string from user and call replace_character function here
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defined_string=input("===================================================================\nenter string: ")
        print("======================================\nstring before {0} and after replacing first character by $: {1}".format(user_defined_string,replace_character(user_defined_string)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","replace character of string successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   