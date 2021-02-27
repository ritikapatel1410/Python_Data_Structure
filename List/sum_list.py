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




def sum_list(List):
    """
    Description:
        this function is define for sum of element of list
    Parameter:
        List (list) : user defined list
    Return:
        sum of list element 
    """
    return sum(List)

def main():
    """
    Description:
        this main function for user defind and call sum_list
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
            print("====================================================\nsum of list {0} elements is : {1}".format(List,sum_list(List)))
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   
