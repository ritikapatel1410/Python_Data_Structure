'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 10:21:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 10:21:38  
 @Title : get system command output
'''

import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir",shell=True,universal_newlines=True)
print("==============================================================================================")
print("dir command to list file and directory : ",returned_text)

