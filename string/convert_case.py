'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 16:20:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 16:20:38  
 @Title : convert string into upper and lower case
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def convert_string(user_defind_string):
    """
    Description:
        this function is define for convert string into upper and lower case
    Parameter:
        user_defined_string (str) : string taken from the user 
    Return:
        lower_case (str) : string converted into lower case
        upper_case (str) : string converted into upper case
    """
    lower_case=user_defind_string.lower()
    upper_case=user_defind_string.upper()
    return lower_case,upper_case

def main():
    """
    Description:
        this main function for take string from user and convert_string
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defind_string=input("===============================================\nenter string here : ")
        lower_case,upper_case=convert_string(user_defind_string)
        print("======================================\nuser_defind_string : {0} \nlower case : {1}\nupper case : {2}".format(user_defind_string,lower_case,upper_case))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","successfully converted user_defind_string into upper and lower case")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   