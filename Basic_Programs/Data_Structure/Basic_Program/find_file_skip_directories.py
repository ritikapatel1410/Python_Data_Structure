'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 12:04:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 12:04:38  
 @Title : find files and skip directories of a given directory
'''
#import module
import os
list_file=[f for f in os.listdir('/home/patidar') if os.path.isfile(os.path.join('/home/patidar', f))]
print("============================================= Files Are ======================================================")
print("\n".join(list_file))