'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 4:50:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 4:50:38  
 @Title : create nested dictionary problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def nested_dict(num_list):
    """
    Description:
        this function is define for create nested dictionary from list 
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        new_dict (dict) : converted nested dictionary
    """
    new_dict = current = {}
    for item in num_list:
        current[item] = {}
        current = current[item]
    return new_dict

def main():
    """
    Description:
        this main function for defind dictionary from the user and call nested_dict function 
    Parameter:
        None
    Return:
        None
    """
    num_list=[1,2,3,4,5]
    print("=============================== created nested dictionary here =====================\n nested dictionary of list {0} is : {1}".format(num_list,nested_dict(num_list)))
    loggerfile.Logger("info","nested dictionary create successfully")
    print("====================================================================================================")
main()   
