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

def creat_tuple(created_list):
    """
    Description:
        this function is define for convert list into tupple
    Parameter:
        created_list (list) : user defined list
    Return:
        converted_tuple (tuple) : created tuple
    """
    converted_tuple=tuple(created_list)
    return converted_tuple

def main():
    """
    Description:
        this main function for create list from taking input from user and call create_tuple function
    Parameter:
        None
    Return:
        None
    """
    created_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        value=int(input("enter index {0} element: ".format(element)))
                        created_list.append(value)
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\ncreated list : {0} converted into tuple is : {1}".format(created_list,creat_tuple(created_list)))
            loggerfile.Logger("info","successfully converted list into tuple")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()