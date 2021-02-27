'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 10:46:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 10:46:38  
 @Title : create a tuple of different data type
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def creat_tuple(List):
    """
    Description:
        this function is define for create a tuple of different data type
    Parameter:
        List (list) : user defined list
    Return:
        Tuple (tuple) : created tuple
    """
    Tuple=tuple(List)
    return Tuple

def main():
    """
    Description:
        this main function for create list from taking input from user and call create_tuple function
    Parameter:
        None
    Return:
        None
    """
    List=["tuple", False, 3.2, 1]
    while True:
        try:
            print("====================================================\ncreated list : {0} converted into tuple is : {1}".format(List,creat_tuple(List)))
            loggerfile.Logger("info","successfully create tuple with different data type successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()