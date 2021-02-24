'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 23:36:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 23:36:38  
 @Title : remove first occurance of element in array problem
'''
from array import *
#import module
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
#import logger file
import loggerfile 

def remove_element(type_array,element):
    """
    Description:
        this function is define for remove first occurance of given element
    Parameter:
        type_array (array) : user_defind array
        element (int) : element which occourance will remove
    Return:
        return array after remove element
    """
    type_array.remove(element)
    return type_array

def main():
    """
    Description:
        this main function for defind array and call remove_element function
    Parameter:
        None
    Return:
        None
    """
    type_array=array('i',[1,2,2,4,3,4,4,5,6])
    before_remove_element=array('i',[1,2,2,4,3,4,4,5,6])
    element=4
    print("============================ Occurance of element is here =========================================")
    print("{0} after remove element {1} is : {2} ".format(before_remove_element,element,remove_element(type_array,element)))
    loggerfile.Logger("debug","remove element successfully")
main()   