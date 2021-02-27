'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 3:28:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 3:28:38  
 @Title : custom Exception file
'''
class Error(Exception):
    pass

class InvalidKeyException(Error):
    pass

class KeyExist(Error):
    pass

class ElementAlreadyExist(Error):
    pass

class IntesectionNotPossible(Error):
    pass
