'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 11:11:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 11:11:38  
 @Title : create the colon of a tuple problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
from copy import deepcopy

def clone_tuple(Tuple):
    """
    Description:
        this function is define for create the colon of a tuple
    Parameter:
        Tuple (list) : user defined tuple
    Return:
        duplicate_tuple (tuple) : clone of given tuple
    """
    duplicate_tuple=deepcopy(Tuple)
    return duplicate_tuple

def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call clone_tuple
    Parameter:
        None
    Return:
        None
    """
    Tuple=("Vijay", "patidar", 28, "B.tech",[])
    try:
        duplicate_Tuple=clone_tuple(Tuple)
        Tuple[4].append("iit roorkee")
        print("========================== clone of Tuple here ==========================\ncopy of Tuple : {0}  is : {1}".format(Tuple,duplicate_Tuple))
        loggerfile.Logger("info","successfully clone of Tuple created")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()