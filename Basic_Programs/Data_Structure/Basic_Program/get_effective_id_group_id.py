'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 10:28:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 10:28:38  
 @Title : get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process problem
'''
#import module
import os
print("===========================================================================")
#print effective group id
print("Effective group id: ",os.getegid())
#print effective user id
print("Effective user id: ",os.geteuid())
#print effective group id
print("Real group id: ",os.getgid())
#print list of supplemental group ids
print("List of supplemental group ids: ",os.getgroups())
