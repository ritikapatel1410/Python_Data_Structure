'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 11:11:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 11:11:38  
 @Title : repeated items of a tuple problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
from copy import deepcopy

def repeative_tuple(given_tuple):
    """
    Description:
        this function is define for repeated items of a tuple
    Parameter:
        given_tuple (tuple) : user defined tuple
    Return:
        repeated_element (tuple) : list of repeated items of a tuple
    """
    repeated_element=[]
    index=1
    for items in given_tuple[:-1]:
        if items in given_tuple[index:]:
            repeated_element.append(items)
        index+=1
    if(len(repeated_element)>0):
        return tuple(repeated_element)
    else:
        return "repeated element not found"


def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call repeative_tuple
    Parameter:
        None
    Return:
        None
    """
    given_tuple=(1,2,3,1,4,2,3,5)
    try:
        return_repeative_element=repeative_tuple(given_tuple)
        if(return_repeative_element!="repeated element not found"):
            print("========================== repeatative element tuple here ==========================\nrepeative element tuple of : {0}  is : {1}".format(given_tuple,repeative_tuple(given_tuple)))
            loggerfile.Logger("info","successfully get repeative element of tuple")
        else:
            print("===========================================\nrepeative element tuple of : {0}  is : {1}".format(given_tuple,repeative_tuple(given_tuple)))
            loggerfile.Logger("info","successfully get repeative element of tuple")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()