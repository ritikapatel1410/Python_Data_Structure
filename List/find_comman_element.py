'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 20:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 20:35:38  
 @Title : find common list intersection proble
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def find_common_element(List1,List2):
    """
    Description:
        this function is define for find lists have common element or not
    Parameter:
        List1 (list) : user defined list
        List2 (list) : user defined list
    Return:
        True (boolean) : if find common element in lists
        False (boolean) : if not find common element in lists 
    """
    list_intersection=set(List1).intersection(set(List2))
    if(len(list_intersection)>0):
        return True
    else:
        return False

def main():
    """
    Description:
        this main function for create list from taking user input and call find_common_element
    Parameter:
        None
    Return:
        None
    """
    List1=[]
    List2=[]
    List_name={"List1":List1,"List2":List2}
    while True:
        try:
            for list_name in List_name.keys():
                size_of_list=int(input("===============================================\nenter size of {0}: ".format(list_name)))
                for element in range(size_of_list):
                    while True:
                            value=input("enter index {0} element of {1}: ".format(element,list_name))
                            List_name[list_name].append(value)
                            break
             
            print("====================================================\nis any common element between List1 {0} and List2 {1} is ? {2}".format(List1,List2,find_common_element(List1,List2)))
            loggerfile.Logger("info","find common element successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   