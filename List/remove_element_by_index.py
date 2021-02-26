'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 20:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 20:35:38  
 @Title : delete element by index problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def delete_by_index(List1):
    """
    Description:
        this function is define for delete specific index element
    Parameter:
        List1 (list) : user defined list
    Return:
        List1 (list) : list after delete element
    """
    del List1[0]
    del List1[3]
    del List1[3]
    return List1

def main():
    """
    Description:
        this main function for create list from taking user input and call delete_by_index
    Parameter:
        None
    Return:
        None
    """
    List1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    List2=list(List1)
    try:
        print("=========================================================================================\nList before {0} and after delete element: {1}".format(List2,delete_by_index(List1)))
        loggerfile.Logger("info","deleted element successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   