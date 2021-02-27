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

def remove_duplicate(user_defined_list):
    """
    Description:
        this function is define for remove duplicates from a list of lists problem
    Parameter:
        user_defined_list (str) : user defined list
    Return:
       clone_user_defined_list (list) : unique value list
    """
    check_duplicate=False
    clone_user_defined_list=list(user_defined_list)
    index=1
    for element in user_defined_list[:-1]:
        if(element in user_defined_list[index:]):
            check_duplicate=True
            clone_user_defined_list.remove(element)
        index+=1
    return check_duplicate,clone_user_defined_list
   

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
        user_defined_list=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        check_duplicate,clone_user_defined_list=remove_duplicate(user_defined_list)
        if(check_duplicate==True):
            print("=========================================================\n user_defined_list {0} after deleted duplicate element : {1}".format(user_defined_list,clone_user_defined_list))
        else:
            print("==========================================================\n user_defined_list no duplicate element found")
            loggerfile.Logger("info","duplicate element deleted successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   