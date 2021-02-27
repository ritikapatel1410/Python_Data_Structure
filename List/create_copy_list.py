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

def duplicate_list(user_defind_list):
    """
    Description:
        this function is define for create duplicate element of list
    Parameter:
        user_defind_list (list) : user defined list
    Return:
        clone_user_defind_list (list) : duplicate list
    """
    clone_user_defind_list=list(user_defind_list)
    return clone_user_defind_list

def main():
    """
    Description:
        this main function for create list from taking input from user and call duplicate_list function
    Parameter:
        None
    Return:
        None
    """
    user_defind_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        value=int(input("enter index {0} element: ".format(element)))
                        user_defind_list.append(value)
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\noriginal list : {0} duplicate list : {1}".format(user_defind_list,duplicate_list(user_defind_list)))
            loggerfile.Logger("info","successfully create duplicate list")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()