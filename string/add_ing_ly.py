'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 14:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 14:00:38  
 @Title : add ing or if ing already exist then add ly at the end of string problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def extend_string(user_defined_string):
    """
    Description:
        this function is define for add ing or if ing already exist then add ly at the end of string problem
    Parameter:
        user_defined_string (str) : string taken from user
    Return:
        user_defined_string after modified by specified condition
    """
    if(len(user_defined_string)>=3):
        if "ing" in user_defined_string:
            user_defined_string+="ly"
            return user_defined_string
        else:
            user_defined_string+="ing"
            return user_defined_string
    else:
        return user_defined_string

def main():
    """
    Description:
        this main function for take string from user and call extend_string function
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defined_string=input("===================================================================\nenter string: ")
        print("======================================\nstring before {0} and after extend string : {1}".format(user_defined_string,extend_string(user_defined_string)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","extend string successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   