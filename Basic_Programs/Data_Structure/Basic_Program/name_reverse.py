'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 19:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 19:15:38  
 @Title : Reverse name problem
'''
# import module
import re

def reverse_name(name):
    """
    Description:
        this function define for reverse input name
    Parameter:
        None
    Return:
        return reversed name
    """
    if(len(name)>0):
        if(re.match("^[A-Za-z A-Za-z]*$",name)):
            return name[::-1]
        else:
            user_input()

def user_input():
    """
    Description:
        this function define for take input from user
    Parameter:
        None
    Return:
        return reversed name
    """
    name=str(input("enter name: "))
    print(reverse_name(str(input("enter name: "))))
user_input()