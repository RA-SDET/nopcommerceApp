# log entries we can create itself in test cases
# but log file configuration(creation) & log file format/syntax we r going to define here in this file
#
# 'logging' is a pre defined python package(also module), installed with python v3.10.10

import logging

class LogGen:
    @staticmethod  #making method static so no need to pass self. Also, method can be accessed directly by class-name
    def loggen():    #log file configuration & format/syntax is coded here, under this method().
        #Package.Function()
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True) # using force=True here is very important otherwise..
                                        #..log file will not be created nor written over.
                                        # See below comment\notes

        #obj    #Module.Function() , here whatever Fn. getLogger() returns is stored in obj 'logger'
        logger=logging.getLogger()
        #logger is also class-attribute of user-defined class LogGen
        # obj.method()
        logger.setLevel(logging.INFO)
        return logger

'''
If 'force' keyword argument is specified as true, any existing handlers attached to
the root logger are removed and closed, before carrying out the configuration
as specified by the other arguments.

After Python 3.8: A new option, force, has been made available to automatically
remove the root handlers while calling basicConfig().

It works, because as per-> https://docs.python.org/3/library/logging.html
 "logging.basicConfig()" function does nothing if the root logger already has
  handlers configured for it. 
SHAYAD ISKA MATLAB HAI KI AGAR VS CODE YA KAHI TERMINAL MEIN HUMNE 'logging.basicConfig()'
ko engage ker rakha hai toh yeh Fn. naya handler nahi banayegi, naya handler matlab
woh jo hum yahan Pycharm mein banana chah rahe hai

To understand more search on internet

--------------------------------------------------------------
levels from lowest to highest:
logger.debug("this is debug message by RA")         
logger.info("this is a info message by RA")         
logger.warning("this is a warning message by RA")   
logger.error("this is a error message by RA")       
logger.critical("this is a critical message by RA") 
'''

#---------------------------------------------------------------------------------------------
# correct working code without comments & notes


# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p',
#                             force=True) # using force=True here is very important otherwise
#                                         #..log file will not be created nor written over
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

