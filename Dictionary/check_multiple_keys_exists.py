'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 4:50:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 4:50:38  
 @Title : multiple keys exist problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def multiple_keys(dictionary,key1,key2):
    """
    Description:
        this function is define for check multiple keys exists
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        True or False
    """
    return (dictionary.keys() >= {key1, key2})

def main():
    """
    Description:
        this main function for defind dictionary from the user and call nested_dict function 
    Parameter:
        None
    Return:
        None
    """
    key1=input("==============================================\nenter key 1 value: ")
    key2=input("==============================================\nenter key 2 value: ")
    dictionary={"name":"ritika","education":"b.tech","college":"smvdu"}
    print("=============================== multiple key exist show here =====================\n key {0} key {1} exist in : {2} ? {3}".format(key1,key2,dictionary,multiple_keys(dictionary,key1,key2)))
    loggerfile.Logger("info","nested dictionary create successfully")
    print("====================================================================================================")
main()   
