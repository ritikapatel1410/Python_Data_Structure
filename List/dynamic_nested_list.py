'''
 @Author: Ritika Patidar
 @Date: 2021-02-8 19:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-28 19:00:38  
 @Title :create dynamic nested list problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import random

def created_nested_list(user_defined_column,user_defind_row):
    """
    Description:
        this function is define for create dynamic nested list problem  
    Parameter:
        user_defind_row (int) : row of nested list
        user_defined_column : column of nested list
    Return:
        nested_list (list) : created nested list
    """
    nested_list=[[random.randint(0,(user_defined_column*user_defind_row)) for colomn in range(user_defined_column)] for row in range(user_defind_row)]
    return nested_list

def main():
    """
    Description:
        this main function for take user_defined_row and user_defined_column from user and call nested_list function
    Parameter:
        None
    Return:
        None
    """
    while True:
        try:
            user_defined_row=int(input("enter the row of nested list: "))
            user_defined_column=int(input("enter the column of nested list: "))
            print("=========================================================\nnested list of row {0} and column {1} : {2} ".format(user_defined_column,user_defined_row,created_nested_list(user_defined_column,user_defined_row)))
            loggerfile.Logger("info","created nested list successfully")
            break
        except ValueError as error:
            print("try again you are not giving int value")
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   