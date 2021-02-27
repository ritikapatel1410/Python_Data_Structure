'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : get size of object
'''
import sys
#object
str1 = 123
str2 = "dipu"
str3 = "aastha patel"
#print size of object
print("=======================================================================================================")
print("Memory size of '"+str(str1)+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str(str2)+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str(str3)+"' = "+str(sys.getsizeof(str3))+ " bytes")