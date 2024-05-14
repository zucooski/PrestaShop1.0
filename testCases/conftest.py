import os
from datetime import datetime
import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
   if browser == 'edge':
      driver = webdriver.Edge()
      print("Launching Edge browser....")
   elif browser == 'firefox':
      driver = webdriver.Firefox()
      print("Launching Firefox browser....")
   elif browser == 'headless':
      ops = webdriver.ChromeOptions()
      ops.add_argument("--headless")
      driver = webdriver.Chrome(options=ops)
      print("Launching Headless browser....")
   else:
      driver = webdriver.Chrome()
      print("Launching Chrome browser....")
   return driver

@pytest.fixture()
def browser(request): # This will return the Browser value to set up method
   return request.config.getoption("--browser")

def pytest_addoption(parser): # This will get the value from CLI /hooks
   parser.addoption("--browser")

# for report generation path
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
   config.option.htmlpath = os.path.abspath(os.curdir) +"/reports/"+ datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".html"
