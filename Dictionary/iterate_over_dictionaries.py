'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 2:18:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 2:18:38  
 @Title : iterate over a dictionary using loop
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def iterate_dictionary(dictionary_input):
    """
    Description:
        this function is define iterate dictionary using loop
    Parameter:
        dictionary_input (dict) : user defined dictionar
    Return:
        True
    """
    for key,value in dictionary_input.items():
        print("======================== iterate Dictionary over here ===============================")
        print("key : {0} value : {1}".format(key,value))
    return True

def main():
    """
    Description:
        this main function for defind dictionary and call iterate_dictionary
    Parameter:
        None
    Return:
        None
    """
    while True:
        dictionary_input={}
        try:
            size_of_dict=int(input("enter the size of dictionary: "))
            for key_value in range(size_of_dict):
                key=input("==========================================================================\nenter key: ")
                assert key not in dictionary_input.keys()
                value=input("=========================================================================\nenter value: ")
                dictionary_input[key]=value
            iterate_dictionary(dictionary_input)
            loggerfile.Logger("info","dictionary iterate successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} occured".format(error))
        except AssertionError as error:
            loggerfile.Logger("error","{0} occured".format(error))

main()   
