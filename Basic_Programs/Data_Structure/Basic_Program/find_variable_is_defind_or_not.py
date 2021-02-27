'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 10:36:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 10:36:38  
 @Title :  find variable is define or not problem
'''
#use try and except block here
print("======================================================================================")
try:
    variable_defind=1
    #print if variable defind
    print("Variable is defined.")
except NameError:
    #print if variable not defind
    print("Variable is not defined....!")

#use try and except block here    
try:
    variable_not_defind
    print("Variable is defined.")
except NameError:
    print("Variable is not defined....!")