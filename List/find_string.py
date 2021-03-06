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

def string_list(user_created_list):
    """
    Description:
        this function is define for find count string which len >=2 and first and last element same of list
    Parameter:
        user_created_list (list) : user defined list
    Return:
        count
    """
    count=0
    for string in user_created_list:
        if(len(string)>=2 and string[0]==string[-1]):
            count+=1
    return count

def main():
    """
    Description:
        this main function for user defind and call string_list
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
                        value=input("enter index {0} element: ".format(element))
                        user_created_list.append(value)
                        break
            print("====================================================\nlist {0} element statisfied condition is : {1}".format(user_created_list,string_list(user_created_list)))
            loggerfile.Logger("info","successfully find min value of list")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   
