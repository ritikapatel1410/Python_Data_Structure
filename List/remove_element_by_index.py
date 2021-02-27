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

def delete_by_index(user_defined_list):
    """
    Description:
        this function is define for delete specific index element
    Parameter:
        user_defined_list (list) : user defined list
    Return:
        user_defined_list (list) : list after delete element
    """
    del user_defined_list[0]
    del user_defined_list[3]
    del user_defined_list[3]
    return user_defined_list

def main():
    """
    Description:
        this main function for create list from taking user input and call delete_by_index
    Parameter:
        None
    Return:
        None
    """
    user_defined_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    clone_user_defined_list=list(user_defined_list)
    try:
        print("=========================================================================================\nList before {0} and after delete element: {1}".format(clone_user_defined_list,delete_by_index(user_defined_list)))
        loggerfile.Logger("info","deleted element successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   