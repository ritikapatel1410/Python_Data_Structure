'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 18:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 18:35:38  
 @Title : sorted list by last element of tuple
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile


def sort_list(user_created_list):
    """
    Description:
        this function is define for sorted list by last element of tuple
    Parameter:
        user_created_list (list) : user defined list
    Return:
        sorted_List (list) : sorted List 
    """
    sorted_List=[(element1,element2) for element1,element2 in sorted(user_created_list, key=lambda item:item[1])]
    return sorted_List

def main():
    """
    Description:
        this main function for user defind and call sort_list
    Parameter:
        None
    Return:
        None
    """
    user_created_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            for element in range(size_of_list):
                while True:
                    try:
                        element1=int(input("enter index {0} and tuple oth element: ".format(element)))
                        element2=int(input("enter index {0} and tuple 1st element: ".format(element)))
                        user_created_list.append((element1,element2))
                        break
                    except ValueError as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
                    except Exception as error:
                        loggerfile.Logger("error","{0} error occured".format(error))
            print("====================================================\nList before sort {0} after sort : {1}".format(user_created_list,sort_list(user_created_list)))
            loggerfile.Logger("info","successfully sorted list")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()