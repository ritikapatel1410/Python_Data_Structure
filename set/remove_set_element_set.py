'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:55:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:55:38  
 @Title : discard element to the set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def remove_element(element,created_set):
    """
    Description:
        this function is define for remove element from a set
    Parameter:
        created_set (set) : created set in main proram
    Return:
        created_set (set) : after removing a element in set
    """
    created_set.discard(element)
    return created_set

def main():
    """
    Description:
        this main function for take user input and call remove_element function here
    Parameter:
        None
    Return:
        None
    """
    old_created_set={0,1,2,3,4,5,6}
    created_set={0,1,2,3,4,5,6}
    while True:
        try:
            element=int(input("===================================================================\nenter element: "))
            print("===========================remove element in set =========================\nbefore remove element {0} after remove element {1}".format(old_created_set,remove_element(element,created_set)))
            print("=========================== program finish here =============================")
            loggerfile.Logger("info","element removed successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
main()   