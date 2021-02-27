
'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 11:52:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 11:52:38  
 @Title :  add leading zeroes to a string problem
'''
#define string
str1='11.12'
print("========================================================================================")
print("Original String: ",str1)
#added leading zeros
print("Added leading zeros:")
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)