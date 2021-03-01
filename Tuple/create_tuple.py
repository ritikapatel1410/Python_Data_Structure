'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 10:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 10:35:38  
 @Title : create a tuple
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def creat_tuple(given_list):
    """
    Description:
        this function is define for create a tuple
    Parameter:
        given_list (list) : user defined list
    Return:
        convert_tuple (tuple) : created tuple
    """
    convert_tuple=tuple(given_list)
    return convert_tuple

def main():
    """
    Description:
        this main function for create list from taking input from user and call create_tuple function
    Parameter:
        None
    Return:
        None
    """
    given_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        value=int(input("enter index {0} element: ".format(element)))
                        given_list.append(value)
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\ncreated list : {0} converted into tuple is : {1}".format(given_list,creat_tuple(given_list)))
            loggerfile.Logger("info","successfully create tupple successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()