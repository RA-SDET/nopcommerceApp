'''
Q How do you call a function/class from a package in Python?
Q How do you call a function/class from a module in Python?
A see folder-> python code with notes(Desktop)/Working with Modules
see link-> https://www.datacamp.com/tutorial/modules-in-python
-----------------------------------------------------------------
Sometimes package is a folder and multiple py files inside it are modules,
module may contain different classes with methods attributes inside them.
Also there can be seperate module functions.
see e.g.
from utilities.readProperties import ReadConfig
from package.module import class or function
'''

# special python package configparser, installed with python only, no need for separate installation
import configparser

'''Becoz we imported full module/package configparser, hence we cannot access its class 'RawConfigParser'
 directly by using code-> config = RawConfigParser() 
So, we have to access it indirectly as shown below'''

#obj = module/package.class()
config = configparser.RawConfigParser() # config is now an object of class RawConfigParser
config.read(".\\Configurations\\config.ini")   # obj is calling read()method of its class RawConfigParser..
                                               #..to read contents of config.ini file by passing relative path/address to file
            #this above is relative path

'''In below sample code by RA
becoz we imported only class RawConfigParser from package configparser, hence we CAN access this
class directly by using code-> config = RawConfigParser()

from configparser import RawConfigParser
config = RawConfigParser()
config.read()
'''

class ReadConfig:  #for each variable (or key-value pair) create a method under this class

    @staticmethod              # i want to access this method getApplicationURL() directly by class-name
    def getApplicationURL():   #..'ReadConfig' without creating an object.So, i made it into a static method.
                               # Also, we dont need to pass 'self' or any other parameter to a static method(), when calling it.
                #obj.method
        url = config.get('common info','baseURL')   # get() method will get 'value' of key 'baseURL' and save in attribute url
        return url                                  #..from section 'common info' of config.ini file
                                                    #..read by config.read() at code-line 18 and
                                                    #..pass/save it to 'url' variable
                                                    # This get() method is specific to RawConfigParser class

    @staticmethod
    def getUseremail():
        useremail = config.get('common info', 'useremail')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password


#--------------------------------------------------------------------------
# # Correct working code without comments/Notes
#
# import configparser
#
# config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
#
#
# class ReadConfig:
#     @staticmethod
#     def getApplicationURL():
#         url = config.get('common info','baseURL')   # get() method will get 'value' of key 'baseURL' and save in attribute url
#         return url
#
#     @staticmethod
#     def getUseremail():
#         useremail = config.get('common info', 'useremail')
#         return useremail
#
#     @staticmethod
#     def getPassword():
#         password = config.get('common info', 'password')
#         return password

















