'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : retrive file property problem
'''
#import module
import os.path
import time
print("=============================================================================================================")
# print get file path
print('File         :', __file__)
#print access time
print('Access time  :', time.ctime(os.path.getatime(__file__)))
#print modified time
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
#print change time
print('Change time  :', time.ctime(os.path.getctime(__file__)))
#print size of
print('Size  in byte      :', os.path.getsize(__file__))
