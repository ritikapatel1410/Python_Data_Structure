'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:25:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:15:38  
 @Title : iterate over a set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def iterate_set(created_set):
    """
    Description:
        this function is define for iterate over a set
    Parameter:
        created_set (set) : created aet in main proram
    Return:
        True : if this function works
    """
    index=0
    for item in created_set:
        print("{0} element is {1}".format(index,item))
        index+=1
    return created_set

def main():
    """
    Description:
        this main function for take user input and call iter_set function here
    Parameter:
        None
    Return:
        None
    """
    created_set=set()
    try:
        size_of_set=int(input("===================================================================\nenter size of set: "))
        for size in range(size_of_set):
            element=input("enter the element of set: ")
            created_set.add(element)
        loggerfile.Logger("info","set iterate successfully")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    print("===========================set {0} iterate over here =========================".format(created_set))
    iterate_set(created_set)
    print("=========================== program finish here =============================")

main()   