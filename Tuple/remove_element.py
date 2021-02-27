'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 11:42:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 11:42:38  
 @Title : remove element from tuple
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
from copy import deepcopy

def remove_element(Tuple,element):
    """
    Description:
        this function is define for remove element from tuple
    Parameter:
        Tuple (Tuple) : user defined tuple
    Return:
        new_tuple (Tuple) : new tuple after removing element
    """
    remove_tuple=deepcopy(Tuple)
    remove_tuple=list(remove_tuple)
    if element in Tuple:
        remove_tuple.remove(element)
        new_tuple=list(remove_tuple)
    return new_tuple


def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call remove_element
    Parameter:
        None
    Return:
        None
    """
    Tuple=(1,2,3,4,5,6,7,8,9,10)
    try:
        element=int(input("=======================================================\nenter element: "))
        print("========================== repeatative element tuple here ==========================\nTuple before : {0}  and after : {1} remove element : {2}".format(Tuple,remove_element(Tuple,element),element))
        loggerfile.Logger("info","successfully remove element")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()