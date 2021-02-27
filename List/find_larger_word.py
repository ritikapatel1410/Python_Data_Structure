'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 19:35:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 19:35:38  
 @Title : find larger word then n 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def string_list(user_created_list,n):
    """
    Description:
        this function is define for find list of string which are larger than given value
    Parameter:
        user_created_list (list) : user defined list
    Return:
        word (list) : list of string which are larger than given value
    """
    word=[]
    for string in user_created_list:
        if(len(string)>n):
            word.append(string)
    return word

def main():
    """
    Description:
        this main function for create list from taking user input and call string_list
    Parameter:
        None
    Return:
        None
    """
    user_created_list=[]
    while True:
        try:
            size_of_list=int(input("===================================================================\nenter size of list: "))
            n=int(input("=====================================================\nenter the value of n: "))
            for element in range(size_of_list):
                while True:
                        value=input("enter index {0} element: ".format(element))
                        user_created_list.append(value)
                        break
            print("====================================================\nlist {0} list of word which are greater then {1}  : {2}".format(user_created_list,n,string_list(user_created_list,n)))
            loggerfile.Logger("info","successfully find the list of word")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   
