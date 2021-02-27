'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:35:38  
 @Title : add element to the set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
sys.path.insert(0, os.path.abspath('custom_exception'))
import custom_exception_file

def add_element_set(element,created_set):
    """
    Description:
        this function is define for add element into a set
    Parameter:
        created_set (set) : created set in main proram
    Return:
        created_set (set) : after adding a element in set
    """
    created_set.add(element)
    return created_set

def main():
    """
    Description:
        this main function for take user input and call add_element_set function here
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
            if(element in created_set):
                raise custom_exception_file.ElementAlreadyExist
            print("===========================add element in set =========================\nbefore add element {0} after add element {1}".format(old_created_set,add_element_set(element,created_set)))
            print("=========================== program finish here =============================")
            loggerfile.Logger("info","element successfully added successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except custom_exception_file.ElementAlreadyExist as error:
            loggerfile.Logger("error","ElementAlreadyExist occured")
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   