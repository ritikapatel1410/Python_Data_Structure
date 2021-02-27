'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 23:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 23:15:38  
 @Title : get absolute path problem
'''
import os
def get_absolute_path(path_fname):
        return os.path.abspath(path_fname)        
print("Absolute file path: ",get_absolute_path("file_exist.py"))