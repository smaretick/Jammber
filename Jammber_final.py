#MAC OSX HIGH SIERRA VERSION 10.13.3
#FIREFOX 54.0.1 (64-BIT)
# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
browser = webdriver.Firefox()  #QUANTUM
#browser.maximize_window()
browser.get("http://www.jammber.com/")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1.png');
browser.find_element_by_link_text("Log In").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2.png');
browser.find_element_by_id("Email").clear()
browser.find_element_by_id("Email").send_keys("scottmaretick51@gmail.com")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot3.png');
browser.find_element_by_id("Password").clear()
browser.find_element_by_id("Password").send_keys("sm110751")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4.png');
browser.find_element_by_id("btnSignIn").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot5.png');
browser.find_element_by_link_text("Forgot password?").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');
browser.find_element_by_id("Email").clear()
browser.find_element_by_id("Email").send_keys("scottmaretick51@gmail.com")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.find_element_by_id("btnSend").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot8.png');
browser.find_element_by_css_selector("img[alt=\"Jammber\"]").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot9.png');
browser.find_element_by_link_text("Sign up").click()
browser.find_element_by_id("FirstName").clear()
browser.find_element_by_id("FirstName").send_keys("SCOTT")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot10.png');
browser.find_element_by_id("LastName").clear()
browser.find_element_by_id("LastName").send_keys("MARETICK")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot11.png');
browser.find_element_by_id("AccountName").clear()
browser.find_element_by_id("AccountName").send_keys("ABC SOFTWARE LLC")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot12.png');
browser.find_element_by_id("Email").clear()
browser.find_element_by_id("Email").send_keys("scottmaretick51@gmail.com")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot13.png');
browser.find_element_by_id("Password").clear()
browser.find_element_by_id("Password").send_keys("sm110751")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot14.png');
browser.find_element_by_id("register").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot15.png');
browser.find_element_by_id("Password").clear()
browser.find_element_by_id("Password").send_keys("Sm110751!")
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.find_element_by_id("register").click()
browser.find_element_by_id("register").click()
browser.find_element_by_link_text("Request One").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.quit()
