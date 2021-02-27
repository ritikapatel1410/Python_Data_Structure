'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 16:40:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 16:40:38  
 @Title : get the last part of a string before a specified character problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def split_string(user_defind_string,specified_character):
    """
    Description:
        this function is define for get the last part of a string before a specified character problem
    Parameter:
        user_defined_string (str) : string taken from the user 
    Return:
        last part of a string by split string specified character 
    """
    if specified_character in user_defind_string:
        return user_defind_string.split(specified_character)[0]
    else:
        return "specified character is not present"

def main():
    """
    Description:
        this main function for take string from user and split_string
    Parameter:
        None
    Return:
        None
    """
    user_defind_string="https://www.w3resource.com/python-exercises"
    try:
        specified_character=input("================================\nenter specified character for {0}: ".format(user_defind_string))
        check_specified_character=split_string(user_defind_string,specified_character)
        if(check_specified_character!="specified character is not present"):
            print("==============================================\nuser_defind_string: {0}\n and last of string: {2}\n before a specified char: {1}".format(user_defind_string,specified_character,check_specified_character))
            loggerfile.Logger("info","successfully split string")
        else:
            print("==============================================\n specified charcter {0} not found".format(specified_character))
            loggerfile.Logger("info","specified charcter not found")
        print("=========================== program finish here =============================")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   