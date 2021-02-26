'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:30:38  
 @Title : find common items from two lists problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def common_element(List1,List2):
    """
    Description:
        this function is define for find common items from two lists
    Parameter:
        List1 (list) : user defined list
        List2 (list) : use defined list
    Return:
       List3 (list) : list of common element
    """
    List3=list(set(List1).intersection(set(List2)))
    return List3
   

def main():
    """
    Description:
        this main function for create list from taking user input and call common_element
    Parameter:
        None
    Return:
        None
    """
    List1=[1,2,3,4,5]
    List2=[1,2,7,8,3,6]
    try:
        print("=========================================================\n List1 {0} and List2 {1} common element are : {2}".format(List1,List2,common_element(List1,List2)))
        loggerfile.Logger("info","find common element successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   