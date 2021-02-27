'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 23:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 23:15:38  
 @Title : count occurance of element in array problem
'''
from array import *
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def occurance_element(type_array,element):
    """
    Description:
        this function is define for count occurance of given element
    Parameter:
        type_array (array) : user_defind array
        element (int) : element which occourance will count
    Return:
        return occourace of given element
    """
    return type_array.count(element)

def main():
    """
    Description:
        this main function for defind array and call occurance_element function
    Parameter:
        None
    Return:
        None
    """
    
    type_array=array("i",[1,2,2,4,3,4,4,5,6])
    element=4
    print("============================ Occurance of element is here =========================================")
    print("occurence of {0} in {1} is : {2}".format(element,list(type_array),occurance_element(type_array,element)))
    loggerfile.Logger("info","get occurance of element successfully")

main()   