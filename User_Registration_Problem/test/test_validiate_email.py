'''
 @Author: Ritika Patidar
 @Date: 2021-03-01 16:06:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-03-01 16:06:10  
 @Title : Test cases for valid email id problem
'''
import unittest
import sys
sys.path.insert(0, 'main')
from validiate_email import valid_email

class Test_validiate_email(unittest.TestCase):
    """
    Description:
        This class define for test all case of valid_email method
    """

    def test_valid_email(self):
        """
        Description:
            This method define for test all case of valid_email method of validiate_email.py
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(valid_email("abc.12www@bl.co.in"),"valid email id")
        self.assertNotEqual(valid_email("abc.12www@bl.co.inn"),"valid email id")
        self.assertEqual(valid_email("abc.12ririka@bl.co.org"),"valid email id")
        self.assertEqual(valid_email("abc.12ririka@bl.co.com"),"valid email id")
        self.assertEqual(valid_email("abc.12ririka@b.co.com"),"invalid email id")
        self.assertIsNotNone(valid_email("dipali@1"))
        self.assertRaises(TypeError,valid_email)

if __name__ == '__main__':
    unittest.main()