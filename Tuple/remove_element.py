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

def remove_element(given_tuple,element):
    """
    Description:
        this function is define for remove element from tuple
    Parameter:
        given_tuple (tuple) : user defined tuple
    Return:
        clone_given_tuple (Tuple) : new tuple after removing element
    """
    remove_tuple=deepcopy(given_tuple)
    remove_tuple=list(remove_tuple)
    if element in given_tuple:
        remove_tuple.remove(element)
        clone_given_tuple=tuple(remove_tuple)
        return clone_given_tuple
    else:
        return "not found"


def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call remove_element
    Parameter:
        None
    Return:
        None
    """
    given_tuple=(1,2,3,4,5,6,7,8,9,10)
    try:
        element=int(input("=======================================================\nenter element: "))
        found_element=remove_element(given_tuple,element)
        if(found_element!="not found"):
            print("========================== repeatative element tuple here ==========================\nTuple before : {0}  and after : {1} remove element : {2}".format(given_tuple,found_element,element))
        else:
            print("===================================================================\nentered element {0} {1} in {2}".format(element,found_element,given_tuple))
        loggerfile.Logger("info","successfully remove element")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()