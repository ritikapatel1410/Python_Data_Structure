'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 00;18:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 00:18:38  
 @Title : sort dictionary by value
'''
#import module
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
#import logger file
import loggerfile 

def sort_value(dictionary):
    """
    Description:
        this function is define for sorted dictionary by value
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        sorted by value dictionary
    """
    dictionary={key:value for key,value in sorted(dictionary.items(),key=lambda item:item[1])}
    return dictionary

def main():
    """
    Description:
        this main function for defind array and sort_value function
    Parameter:
        None
    Return:
        None
    """
    dictionary={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print("============================ Occurance of element is here =========================================")
    print("dictionary {0} after sorted by value : {1}".format(dictionary,sort_value(dictionary)))
    loggerfile.Logger("debug","sorted dictionary by value")

main()   