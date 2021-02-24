'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 23:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 23:15:38  
 @Title : reverse array problem
'''
from array import *
#import module
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
#import logger file
import loggerfile 

def reverse_array(type_array):
    """
    Description:
        this function is define for reverse array of an given array
    Parameter:
        type_array : user_defind array
    Return:
        return reversed array
    """
    return type_array[::-1]

def main():
    """
    Description:
        this main function for defind array and call reverse array
    Parameter:
        None
    Return:
        None
    """
    
    type_array=array("i",[1,2,3,4,5,6])
    print("============================ Reversed Array Here=========================================")
    print("{0} array of revesed array is : {1}".format(type_array,reverse_array(type_array)))
    loggerfile.Logger("debug","get reverse array successfully")

main()    
