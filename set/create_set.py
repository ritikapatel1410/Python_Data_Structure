'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:15:38  
 @Title : create a set data structure
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def create_set(element):
    """
    Description:
        this function is define for create set
    Parameter:
        element (int) : user input
    Return:
        created_set (set) : created array
    """
    created_set.add(element)
    return created_set

def main():
    """
    Description:
        this main function for take user input and call create_set function
    Parameter:
        None
    Return:
        None
    """
    global created_set
    created_set=set()
    try:
        size_of_set=int(input("===================================================================\nenter size of set: "))
        for size in range(size_of_set):
            element=input("enter the element of set: ")
            set_formed=create_set(element)
        loggerfile.Logger("info","set created successfully")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    print("============================ created set is here =========================================")
    print("created set : {0}".format(set_formed))
    

main()   