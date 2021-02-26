'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:30:38  
 @Title : remove duplicates from a list of lists problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def remove_duplicate(List):
    """
    Description:
        this function is define for remove duplicates from a list of lists problem
    Parameter:
        List (str) : user defined list
    Return:
       List1 (list) : unique value list
    """
    List1=list(List)
    index=1
    for element in List[:-1]:
        if(element in List[index:]):
            List1.remove(element)
        index+=1
    return List1
   

def main():
    """
    Description:
        this main function for string take from user and call remove_duplicate
    Parameter:
        None
    Return:
        None
    """
    try:
        List=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print("=========================================================\n list {0} after deleted duplicate element : {1}".format(List,remove_duplicate(List)))
        loggerfile.Logger("info","duplicate element deleted successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   