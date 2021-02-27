'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:00:38  
 @Title : append a list to the second list problem 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def append_list(List1,List2):
    """
    Description:
        this function is define for append a list to the second list 
    Parameter:
        List1 (list) : user defined list
        List2 (list) : use defined list
    Return:
        List3 (list) : append list
    """
    List3=List1+List2
    return List3

def main():
    """
    Description:
        this main function for create list from taking user input and call append_list function
    Parameter:
        None
    Return:
        None
    """
    List1=[1,2,3]
    List2=[1,2,7,8]
    try:
        print("=========================================================\n append of {0} and {1} is : {2}".format(List1,List2,append_list(List1,List2)))
        loggerfile.Logger("info","append list successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   