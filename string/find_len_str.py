'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 13:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 13:35:38  
 @Title : find lenghth of string 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def find_length(user_defined_string):
    """
    Description:
        this function is define for find lenghth of string 
    Parameter:
        user_defined_string (str) : string taken from user
    Return:
        length_string (int) : length of string taken from user
    """
    length_string = len(user_defined_string)
    return length_string

def main():
    """
    Description:
        this main function for take string from user and call find_length function here
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defined_string=input("===================================================================\nenter string: ")
        print("=========================== length of string =========================\nlength of string {0} is {1}".format(user_defined_string,find_length(user_defined_string)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","find length of string successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   