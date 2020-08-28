#--------------------------
#Instagram Log In Bot
#Creator: Brian Walheim
# Version: 1.0.0
#   Automatically logins in to instagram on google chrom
#   Requires to download webdriver
#--------------------------

#---------------
#Imports
#---------------

#Webdriver imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Time import
import time

#----------------
#Variables
#----------------

#Path to webdriver on computer
PATH = "C:\\webdrivers\\chromedriver.exe" 

#Log in information
username = "username"
password = "password"

#----------------
#Main
#----------------

#Loads webpage
browser = webdriver.Chrome(PATH)
browser.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(1)

#Finds username inpute field and enters username
searchField = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
searchField.send_keys(username)

#Finds password input field and enters password
searchField = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
searchField.send_keys(password)

#Presses enter to log in
searchField.send_keys(Keys.RETURN)
