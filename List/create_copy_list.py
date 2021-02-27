'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 18:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 18:35:38  
 @Title : create duplicate list of original list
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def duplicate_list(List):
    """
    Description:
        this function is define for create duplicate element of list
    Parameter:
        List (list) : user defined list
    Return:
        List_new (list) : duplicate list
    """
    List_new=list(List)
    return List_new

def main():
    """
    Description:
        this main function for create list from taking input from user and call duplicate_list function
    Parameter:
        None
    Return:
        None
    """
    List=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        value=int(input("enter index {0} element: ".format(element)))
                        List.append(value)
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\noriginal list : {0} duplicate list : {1}".format(List,duplicate_list(List)))
            loggerfile.Logger("info","successfully create duplicate list")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()