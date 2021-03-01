'''
 @Author: Ritika Patidar
 @Date: 2021-02-28 1:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-28 1:00:38  
 @Title :  validiate user regestration problem 
'''
import re
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import validiate_name
import validiate_email
import validiate_mobile_number
import validiate_password

def main():
    """
    Description:
        this function is define for validiate mobile number of user 
    Parameter:
       None
    Return:
       None
    """
    while True:
        try:
            print("======================== Give Registration Permission=======================")
            reg_permission=input("do want to registration? enter y or n: ")
            if(reg_permission=="y"):
                print("============================= Give First Name ========================")
                if(validiate_name.valid_first_name(validiate_name.input_name("first_name"))=="valid name"):
                    print("============================= Give Last Name ========================")
                    if(validiate_name.valid_last_name(validiate_name.input_name("last_name"))=="valid name"):
                        print("============================= Give Email Id ========================")
                        if(validiate_email.valid_email(validiate_email.input_email())=="valid email id"):
                            print("============================= Mobile Number ========================")
                            if(validiate_mobile_number.valid_mobile_number(validiate_mobile_number.input_mobile_no())=="valid mobile number"):
                                print("============================= Give Password ========================")
                                if(validiate_password.valid_password(validiate_password.input_password())=="Valid Password"):
                                   loggerfile.Logger("info","user registered")
                                   sys.exit()                
                                else:
                                    print("=======================================\ninvalid password id try again!!!")
                                    main()             
                            else:
                                print("====================================================\ninvalid mobile number id try again!!!")
                                main()
                        else:
                            print("===============================================================\ninvalid email id try again!!!")
                            main()
                    else:
                        print("==================================================================\ninvalid last name try again!!!")
                        main()
                else:
                    print("=========================================================================\ninvalid first name try again!!!")
                    main()
            elif(reg_permission=="n"):
                sys.exit()
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main() 

     


    
