'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 3:28:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 3:28:38  
 @Title : print unique values of dictionary
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 
sys.path.insert(0, os.path.abspath('custom_exception'))
import custom_exception_file
import re

def unique_values(dictionary):
    """
    Description:
        this function is define for find unique values
    Parameter:
        dictionary (dict) : dictionary in which we will find unique values
    Return:
        set of unique values
    """
    return set(dictionary.values())

def main():
    """
    Description:
        this main function for take input from the user and call unique values function
    Parameter:
        None
    Return:
        None
    """
    while True :
        dictionary={}
        try:
            size_of_dictionary=int(input("=============================\nenter the size of dictionary: "))
            for item in range(size_of_dictionary):
                while True:
                    try:
                        key=input("=========================================\nenter key: ")
                        value=input("=========================================\nenter value: ")
                        if(re.match(r'[^,\[\]{}]+(({|\[)[^\[\]{}]*(}|\]))?',key) and re.match(r'[^,\[\]{}]+(({|\[)[^\[\]{}]*(}|\]))?',value)):
                            if(key not in dictionary.keys()):
                                dictionary[key]=value
                                break
                            else: 
                                raise custom_exception_file.KeyExist
                        else: 
                                raise custom_exception_file.InvalidKeyException
                    except  custom_exception_file.KeyExist as error:
                        loggerfile.Logger("error","error {0} occured".format(error))
                    except  custom_exception_file.InvalidKeyException as error:
                        loggerfile.Logger("error","error {0} occured".format(error))

            print("=====================================================\ndictionary {0} unique values are {1}".format(dictionary,unique_values(dictionary)))
            loggerfile.Logger("info","find unique value successfully")
            break 
        except ValueError as error:
            loggerfile.Logger("error","{0} occured".format(error))

main()   
