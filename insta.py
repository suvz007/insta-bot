#import modules
from time import sleep
from selenium import webdriver

#import self modules
from credential import *
from driver_path import *

def init_browser():
    browser = webdriver.Firefox(executable_path=driver_path)
    return browser
    
def login_insta(browser):
    browser.get("https://www.instagram.com/")
    sleep(2)
    
    browser.implicitly_wait(30)
    username = browser.find_element_by_name('username')
    username.send_keys(USERNAME)
    browser.implicitly_wait(30)
    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)
    sleep(2)
    
    # Click the login button
    browser.implicitly_wait(30)
    browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
    browser.implicitly_wait(30)
    
    #Save Info, Not Now
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    browser.implicitly_wait(30)
    
    browser.find_element_by_xpath("/html/body/div/div/div/div//div[3]/button[2]").click()
    browser.implicitly_wait(30)
    
if __name__ == "__main__":
    browser = init_browser()
    login_insta(browser)