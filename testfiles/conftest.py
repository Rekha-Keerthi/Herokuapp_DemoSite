import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver=None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Selecting browser at runtime")

@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("--browser_name")
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')

    if browsername == "chrome":
        # creating service object to get the path of chrome driver
        service_obj = Service("D:/Python_Course/Selenium_with_Python/drivers/chromedriver.exe")

        # creating driver object to launch the chrome broswer stored in service_obj
        driver = webdriver.Chrome(service=service_obj,options=chrome_options)

    elif browsername == "firefox":
        # creating service object to get the path of chrome driver
        service_obj = Service("D:/Python_Course/Selenium_with_Python/drivers/geckodriver.exe")

        # creating driver object to launch the chrome broswer stored in service_obj
        driver = webdriver.Chrome(service=service_obj)

    elif browsername == "edge":

        service_obj = Service("D:/Python_Course/Selenium_with_Python/drivers/geckodriver.exe")

        # creating driver object to launch the chrome broswer stored in service_obj
        driver = webdriver.Chrome(service=service_obj)

    #driver.get("https://www.amazon.in/ref=nav_logo")
    driver.get("https://the-internet.herokuapp.com/")

    request.cls.driver =driver

    #yield
    #driver.close()



