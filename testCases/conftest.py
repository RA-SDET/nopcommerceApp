from selenium import webdriver
import pytest  # becoz pytest will make below piece of code available through-out project.

# Pieces of codes used again n again in project are stored here, then called by Fn name (e.g. setup)
# where-ever required in project. This helps to reduce code redundancy(repetition) in project.
# not only Fixtures but other things r also stored/coded here, in conftest.py file


# Fixture Fns in conftest.py file are made available to test .py files stored in same directory/folder/package
# Any method/Fn etc of any test .py file with name 'setup' as I/P parameter will get value returned by 'setup'
#..Fn as argument, pytest makes sure of it.
@pytest.fixture()
def setup(browser):           # Also calling 'browser' pytest Fixture/Fn as  parameter/argument
    if browser == "chrome":
        driver = webdriver.Chrome()
        print (" Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print(" Launching Firefox browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print(" Launching Microsoft Edge browser")
    else:
        driver = webdriver.Chrome()
        print(" Launching Default browser Chrome")
    return driver
# To study more on pytest fixtures goto-> pg15 of pytest_tutorial by tutorialspoint.com.pdf

####################### cross browser testing, to run test on desired browser ####################################
#we need to create 2 more Fns & edit setup() code, to run tests on browser name we provided/entered in command line
#1.this one will capture browser name from command line and store it in.....
def pytest_addoption(parser):  # this will get the value of CLI/Hooks
    parser.addoption("--browser")
# above 2 lines of codes are related to pytest, just learn this syntax as it is.

#2.this is a fixture and will make brower name captured by pytest_addoption()Fn available/passed
#..to setup()Fn above. Becoz name of this Fixture/Fn is mentioned as I/P parameter in setup() Fn above
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
# technically this Fn will intake browser value and pass it as argument to setup()Fn
# above 2 lines of codes are related to pytest, just learn this syntax as it is.

#now make necessary changes in setup() code

# Now, pass browser name as argument in command line, using any 1 code line in command line frm below.
# pytest -v -s testCases/test_login.py --browser chrome
# pytest -v -s testCases/test_login.py --browser firefox
# pytest -v -s testCases/test_login.py --browser edge
# pytest -v -s testCases/test_login.py --browser ie

########################## to run tests parallely ################################
''' 
install package(plug-in)  pytest-xdist ,
To install for current project in Pycharm (as shown in 1st video):
goto file > Settings > Project: nopcommerceApp > Python Interpreter > click '+' in below tab >
> in search bar type pytest-xdist > mouse select pytest-xdist from below list > click Install Package >
wait for it to install and flash installed successful message > close open window > click OK 

Now type any below code in command line. Use any 1 code line in command line
pytest -v -s -n=2 testCases/test_login.py --browser chrome
pytest -v -s -n=2 testCases/test_login.py 

here -n=2 means u have 2 tests in yr file and u want to run them parallely, if u have 4 or more tests
in yr file still u should not give more then -n=3 , becoz running more then 3 tests parallely will very 
slow down yr PC
'''
############################# code to Generate pytest HTML reports ###################################
'''                      code to Generate pytest Reports (in HTML format)

becoz reports are common to all tests, So, common things we need to put in the conftest.py ,
thats why we create/code to Generate pytest HTML reports in conftest.py

install package(plug-in) pytest-html , same procedure as described above.
Now type any below code in command line. Use any 1 code line in command line.
pytest -v -s -n=2 --html=Reports\report1.html testCases/test_login.py --browser chrome
pytest -v -s -n=2 --html=Reports/report2.html testCases/test_login.py --browser chrome
pytest -v -s -n=2 --html=Reports/report3.html testCases/test_login.py
pytest -v -s --html=Reports/report.html testCases/test_login.py
                   #RELATIVE PATH to Reports folder and file inside
                   
pytest will automatically create report.html (if not already present) and over-write on it. 
Here we generate reports in Default Format with default fields,values,parameters,arguments etc.

To generate pytest Reports as per yr desired configuration use below code.  
In this, we need to create 2 more Fns(hooks). 
1st Fn will add some DESIRED details to Environment section of yr html reports , DESIRED is upto coder.
2nd Fn will remove some UN-DESIRED details from Environment section of yr html reports , UN-DESIRED is also upto coder.               
'''
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'RajPavan'
    config._metadata['xyz'] = 'abc'   #u can add whatever u want
    # u can add more details here

# # It is hook for deleting/Modifying Environment info in HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#     #u can delete more details (by coding) here

'''  ABOVE CODE(line 98-103) IS RUNNING BUT GIVING BELOW WARNING , so i replaced it with below code(line 119-123),
 which is not giving any warning, and deleting environment info as per code inside it.
================================================== warnings summary ===================================================
testCases/conftest.py:99
  C://Users//ADMIN//PycharmProjects//nopcommerceApp//testCases//conftest.py:99: PytestDeprecationWarning: The hookimpl pytest_
metadata uses old-style configuration options (marks or attributes).
  Please use the pytest.hookimpl(optionalhook=True) decorator instead
   to configure the hooks.
   See https://docs.pytest.org/en/latest/deprecations.html#configuring-hook-specs-impls-using-markers

pytest Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
'''

# It is hook for deleting/Modifying Environment info in HTML Report
@ pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None) # some old format of pytest html reports shows 'JAVA_HOME' field in Environment section
                                    # but not my version of reports, toh pata nahi yeh code line yahan kya karega
    metadata.pop("Plugins", None) # successfully deletes Plugins from Environment table
    # u can delete more details (by coding) here


# Use below code to show logs also in pytest html reports. Use code in command line.
# pytest -v --html=Reports/report4.html testCases/test_login.py
# I removed -s , as per an online forum: pytest v3... does not capture logs in html reports if -s is specified
#..in command. pytest v2...captured logs in html reports even if -s is specified in command.


# i dont know about these 3 Fns above related to pytest html reports, just learn their code,
# when have extra time understand them.
