'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : call external cammand problem
'''
#import module
import subprocess

#enter cammand
try:
    command=str(input("enter external command: ")).split(" ")
    result=subprocess.call(command)
except FileNotFoundError as error:
    print("invalid command {0} occured".format(error))
