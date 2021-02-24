'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 14:47:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 14:47:38  
 @Title : determine executing shell script in 32bit or 64bit mode on operating system problem
'''
#import struct
import struct
#print structure of os
print("=============================================\nstructure of os : {0}".format(struct.calcsize("P") * 8))
