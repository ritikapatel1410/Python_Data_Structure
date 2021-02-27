'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 11:38:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 11:38:38  
 @Title : convert list into tupple
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def creat_tuple(List):
    """
    Description:
        this function is define for convert list into tupple
    Parameter:
        List (list) : user defined list
    Return:
        Tuple (tuple) : created tuple
    """
    Tuple=tuple(List)
    return Tuple

def main():
    """
    Description:
        this main function for create list from taking input from user and call create_tuple function
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
            print("====================================================\ncreated list : {0} converted into tuple is : {1}".format(List,creat_tuple(List)))
            loggerfile.Logger("info","successfully converted list into tuple")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()