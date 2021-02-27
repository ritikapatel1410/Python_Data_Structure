'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 00;42:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 00:42:38  
 @Title : add new key to dictionary
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def add_key(dictionary,key,value):
    """
    Description:
        this function is define for add new key into dictionary
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        updated dictionary
    """
    dictionary[key]=value
    return dictionary

def main():
    """
    Description:
        this main function defined for call add_key function and defined dictionary
    Parameter:
        None
    Return:
        None
    """
    old_dictionary={0: 10, 1: 20}
    dictionary={0: 10, 1: 20}
    key=input("enter key : ")
    value=input("enter value : ")
    print("============================ Occurance of element is here =========================================")
    print("dictionary {0} after added new key : {1}".format(old_dictionary,add_key(dictionary,key,value)))
    loggerfile.Logger("info","new key added successfully")

main()   