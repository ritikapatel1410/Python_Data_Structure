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

def creat_tuple(given_list):
    """
    Description:
        this function is define for create a tuple of different data type
    Parameter:
        given_list (list) : user defined list
    Return:
        convert_tuple (tuple) : created tuple
    """
    convert_tuple=tuple(given_list)
    return convert_tuple

def main():
    """
    Description:
        this main function for create list from taking input from user and call create_tuple function
    Parameter:
        None
    Return:
        None
    """
    given_list=["tuple", False, 3.2, 1]
    while True:
        try:
            print("====================================================\ncreated list : {0} converted into tuple is : {1}".format(given_list,creat_tuple(given_list)))
            loggerfile.Logger("info","successfully create tuple with different data type successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()