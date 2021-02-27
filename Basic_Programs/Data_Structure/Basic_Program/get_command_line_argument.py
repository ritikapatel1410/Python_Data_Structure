'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : get command line argument problem
'''
import sys
print("=========================================================================================================")
print("This is the name/path of the script: {0}".format(sys.argv[0]))
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))