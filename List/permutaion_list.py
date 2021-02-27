'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 22:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 22:35:38  
 @Title : find permutation of list problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import itertools

def permutation_list(user_defined_list):
    """
    Description:
        this function is define for find permutation of given list
    Parameter:
        user_defined_list (list) : user defined list
    Return:
        True (boolean) : if function works
    """
    print(list(itertools.permutations(user_defined_list)))
    return True

def main():
    """
    Description:
        this main function for create list from taking user input and call delete_by_index
    Parameter:
        None
    Return:
        None
    """
    user_defined_list=[1,2,3]
    try:
        print("=========================================================================================")
        permutation_list(user_defined_list)
        loggerfile.Logger("info","find permutation successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   