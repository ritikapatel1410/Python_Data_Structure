'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 17:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 17:35:38  
 @Title : multiply of list element problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def mult_list(user_defined_list):
    """
    Description:
        this function is define for multiply of element of list
    Parameter:
        user_defined_list (list) : user defined list
    Return:
        mult (int) : multiply of all element in list
    """
    mult=1
    for element in user_defined_list:
        mult*=element
    return mult

def main():
    """
    Description:
        this main function for user defind and call mult_list
    Parameter:
        None
    Return:
        None
    """
    user_defined_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        value=int(input("enter index {0} element: ".format(element)))
                        user_defined_list.append(value)
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\nmultiply all element of list {0} is : {1}".format(user_defined_list,mult_list(user_defined_list)))
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()