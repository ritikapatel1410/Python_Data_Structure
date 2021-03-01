'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 17:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 17:35:38  
 @Title : find smallest number of list
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile




def min_list(user_defined_list):
    """
    Description:
        this function is define for smallest number of list
    Parameter:
        user_defined_list (list) : user defined list
    Return:
        minimum value of user_defined_list
    """
    return min(user_defined_list)

def main():
    """
    Description:
        this main function for user defind and call min_list
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
            print("====================================================\nmin value of list {0} is : {1}".format(user_defined_list,min_list(user_defined_list)))
            loggerfile.Logger("info","successfully find min value of list")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()