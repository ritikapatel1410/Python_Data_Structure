'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 1:09:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 1:09:38  
 @Title :  get the name of the host on which the routine is running problem
'''
#import module
import socket
host_name = socket.gethostname()
#print hostname
print("==============================================================================================")
print("Host name:", host_name)

