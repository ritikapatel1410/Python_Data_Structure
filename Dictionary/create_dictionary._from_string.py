'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 3:28:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 3:28:38  
 @Title : create dictionary from string problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 
sys.path.insert(0, os.path.abspath('custom_exception'))
import custom_exception_file

def create_dictionary(user_string):
    """
    Description:
        this function is define for create dictionary by string
    Parameter:
        string (str) : by which we will create dictionary
    Return:
        dictionary (dict) : created dictionary
    """
    dictionary={}
    for key in user_string:
        try:
            if key not in dictionary.keys():
                dictionary[key]=user_string.count(key)
                loggerfile.Logger("info","assigned value to key sucessfully")
            else:
                raise custom_exception_file.KeyExist
        except custom_exception_file.KeyExist as error:
            loggerfile.Logger("error","{0} occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
    return dictionary

def main():
    """
    Description:
        this main function for take input from the user and call create_dictionary function
    Parameter:
        None
    Return:
        None
    """
    string=input("===================================================================\nenter string: ")
    print("=======================================================\ncreated dictionary from string {0} is : {1}".format(string,create_dictionary(string)))
    loggerfile.Logger("info","create dictionary from string successfully")
    print("=====================================================================")
main()   
