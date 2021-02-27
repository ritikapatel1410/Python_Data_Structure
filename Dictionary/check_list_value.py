'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 4:50:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 4:50:38  
 @Title : check list type in values of dictionary
 '''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def check_list(dictionary):
    """
    Description:
        this function is define for check list in dictionary values
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        count : no of list in values of dictionary
    """
    count =0
    for value in dictionary.values():
        if(type(value)==list):
            count+=1
    return count

def main():
    """
    Description:
        this main function for defind dictionary from the user and call nested_dict function 
    Parameter:
        None
    Return:
        None
    """
    dictionary={1:[1,2,3],2:0,3:[1,3,4,5],6:0}
    print("=========== count of list in values of directory ===============\n count of list in directory {0} ? {1}".format(dictionary,check_list(dictionary)))
    loggerfile.Logger("info","count list successfully")
    print("====================================================================================================")
main()   
