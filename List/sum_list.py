'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:35:38  
 @Title : sum of list element problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile




def sum_list(user_list):
    """
    Description:
        this function is define for sum of element of list
    Parameter:
        user_list (list) : user defined list
    Return:
        sum of list element 
    """
    return sum(user_list)

def main():
    """
    Description:
        this main function for user defind and call sum_list
    Parameter:
        None
    Return:
        None
    """
    user_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        value=int(input("enter index {0} element: ".format(element)))
                        user_list.append(value)
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\nsum of list {0} elements is : {1}".format(user_list,sum_list(user_list)))
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   
