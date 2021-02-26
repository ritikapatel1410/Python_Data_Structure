'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 17:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 17:35:38  
 @Title : remove duplicate element of list problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def remove_duplicate_element(List):
    """
    Description:
        this function is define for emove duplicate element of list
    Parameter:
        List (list) : user defined list
    Return:
        List_unique (list) : list which have only unique element
    """
    List_unique=list(List)
    index=1
    for element in List[:-1]:
        if(element in List[index:]):
            List_unique.remove(element)
        index+=1
    return List_unique

def main():
    """
    Description:
        this main function for create list from taking input from user and call remove_duplicate_element function
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
            print("====================================================\nlist before {0} and after remove duplicates {1}".format(List,remove_duplicate_element(List)))
            loggerfile.Logger("info","successfully remove duplicate element")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()