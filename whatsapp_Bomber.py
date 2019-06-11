from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import emoji

print ('save chromedriver.exe in C:\Python27\chromedriver_win32\chromedriver.exe')

try:
    driver = webdriver.Chrome('C:\Python27\chromedriver_win32\chromedriver.exe')
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)

    target = raw_input('Enter the name of user or group : ')
    target = '"'+target+'"'
    print target

    string = raw_input('Enter the message : ')
    print string

    count = int(input('Enter the count : '))

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()


    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    for i in range(count):
        message.send_keys(string)
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
        time.sleep(1)

    driver.close()


except KeyboardInterrupt:
    print "\nKeyboard Interrupt..."




