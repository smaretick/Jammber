# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

desired_cap = {
    'browserName': 'iPad',
        'device': 'iPad Pro',
            'realMobile': 'true',
                'os_version': '11.2'
}

driver = webdriver.Remote(
                          command_executor='http://scottmaretick3:raih4LZQUMZcTcpcQadp@hub.browserstack.com:80/wd/hub',
                          desired_capabilities=desired_cap)
#driver = webdriver.Firefox()
driver.get("http://www.jammber.com")
driver.find_element_by_css_selector(".nav.navbar-nav.navbar-right>li>a").click()
time.sleep(25)
driver.find_element_by_css_selector("#Email").send_keys("scottmaretick51@gmail.com")
time.sleep(25)
driver.find_element_by_css_selector("#Password").send_keys("sm110751")
time.sleep(25)
driver.find_element_by_css_selector("#btnSignIn").click()
time.sleep(25)
print driver.title
driver.quit()

