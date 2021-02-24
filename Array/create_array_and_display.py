'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 12:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 12:15:38  
 @Title : create an array of integers and display the array items problem
'''
#import module
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
#import logger file
import loggerfile 
def create_array(element):
    """
    Description:
        this function define for create an array
    Parameter:
        element (int) : element of array passed by main function
    Return:
        created_list (list) : return created list
    """
    create_list.append(element)
    return create_list

def show_array(create_list):
    """
    Description:
        this function define for show array
    Parameter:
        created_list (list) : created list which is return by create_array function
    Return:
        True (boolean) : return true if this function work properly
    """
    for index in range(len(create_list)):
        print("index {0} element is {1}".format(index,create_list[index]))
    return True

def main():
    """
    Description:
        this main function of code, it will call function
    Parameter:
        None
    Return:
        None
    """ 
    global create_list
    create_list=[]   
    for integer in range(5):
        while True:
            try:
                element=int(input("=========================================================\nenter element of array for {0} index integer only: ".format(integer)))
                #call create function here
                create_array(element)
                break
            except ValueError as error:
                loggerfile.Logger("error","{0} occured".format(error))

    print("==================================== show elment of array here ==============================")
    #call show array function here
    show_array(create_list)
    loggerfile.Logger("debug","code working as excepted")

#main function
main()
