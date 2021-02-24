'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 19:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 19:15:38  
 @Title : cheak file exist or not problem
'''
import os.path

if os.path.isfile('file_exist.py'):
    print ("File exist")
else:
    print ("File not exist")
