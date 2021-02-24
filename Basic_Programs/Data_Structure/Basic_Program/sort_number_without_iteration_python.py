'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : sort three number without using loop and if else condition
'''
import sys
import os
#import logger file 
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def sort_number(a,b,c):
    """
    Description:
        sort of three number without using for or while loop
    Parameter:
        a (int) = input from the user
        b (int) = input from the user
        c (int) = input from user
    Return:
        sorted of number sequence
    """
    max_number=max(a,b,c)
    min_number=min(a,b,c)
    middle_number=(a+b+c)-max_number-min_number
    return min_number,middle_number,max_number

try:
    a=int(input("enter first number : "))
    b=int(input("enter second number : "))
    c=int(input("enter third number : "))
    print("=================================================================\nsorted number is {0}".format(sort_number(a,b,c)))
except ValueError as error:
    loggerfile.Logger("debug","{0} occured".format(error))