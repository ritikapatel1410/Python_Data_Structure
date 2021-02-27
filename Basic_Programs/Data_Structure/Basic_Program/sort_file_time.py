'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : sort file by date
'''
#import module
import glob
import os
#sort file which have .py extention
files = glob.glob("*.py")
#sort file by modified time
files.sort(key=os.path.getmtime)
print("\n".join(files))