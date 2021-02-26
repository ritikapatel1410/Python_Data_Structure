'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 22:45:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 22:45:38  
 @Title : get the difference between the two lists 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def difference_list(List1,List2):
    """
    Description:
        this function is define for get the difference between the two lists 
    Parameter:
        List1 (list) : user defined list
        List2 (list) : use defined list
    Return:
        List3 (list) : difference of List1 and List2
    """
    List3=[set(List1).symmetric_difference(set(List2))]
    return List3

def main():
    """
    Description:
        this main function for create list from taking user input and call difference_list function
    Parameter:
        None
    Return:
        None
    """
    List1=[1,2,3]
    List2=[1,2,7,8]
    try:
        print("=========================================================\n difference of {0} and {1} is : {2}".format(List1,List2,difference_list(List1,List2)))
        loggerfile.Logger("info","find difference of list successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   