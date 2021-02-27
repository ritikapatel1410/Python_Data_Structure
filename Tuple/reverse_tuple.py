'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 11:57:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 11:57:38  
 @Title : reverse tuple problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
from copy import deepcopy

def reverese_Tuple(Tuple):
    """
    Description:
        this function is define for reverse tuple problem
    Parameter:
        Tuple (Tuple) : user defined tuple
    Return:
        reversed_tuple (Tuple) : reverse tuple of given tuple
    """
    reversed_tuple=tuple(list(Tuple)[::-1])
    return reversed_tuple


def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call rreverse_Tuple
    Parameter:
        None
    Return:
        None
    """
    Tuple=(1,2,3,4,5,6,7,8,9,10)
    try:
        print("========================== repeatative element tuple here ==========================\nTuple before : {0}  and after : {1} reversed".format(Tuple,reverese_Tuple(Tuple)))
        loggerfile.Logger("info","successfully reversed tuple")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()