'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 12:12:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 12:12:38  
 @Title : convert an integer to binary keep leading zeros problem
'''
#convert decimal number to binary
bin_converted=bin(50)[2:][:-2]
print("=============================================================================================")
#print expected output 
print("{0},{1}".format(bin_converted.rjust(8, '0'),bin_converted.rjust(10, '0')))