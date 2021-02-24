'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 23:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 23:15:38  
 @Title : get modify and create detail file problem 
'''
#import module
import os.path, time
#print last modified detail
print("Last modified: %s" % time.ctime(os.path.getmtime("Basic_Program/get_current_user.py")))
#print create detail
print("Created: %s" % time.ctime(os.path.getctime("Basic_Program/get_current_user.py")))