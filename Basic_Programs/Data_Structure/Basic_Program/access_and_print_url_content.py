'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 10:09:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 10:09:38  
 @Title :  access and print a URL's content to the console problem
'''
#import module
from http.client import HTTPConnection
#make connection to the host 
conn = HTTPConnection("google.com")
#get response of from the host
conn.request("GET", "/") 
#get response to host 
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print("======================================================\n",contents)