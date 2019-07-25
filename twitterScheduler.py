from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from datetime import datetime
from datetime import timedelta

import calendar

import os
import threading
import autoit

def handle_dialog(picName):
    attempts = 0
    while attempts <= 5:
        try:
            autoit.control_focus("Open", "Edit1")
            autoit.control_set_text("Open","Edit1",picName)
            autoit.control_send("Open","Edit1","{ENTER}")
            break
        except:
            sleep(.3)
    

def newScheduleDate(scheduleDate):
    return scheduleDate + timedelta(days=7)

def t_scheduler(fName, directory, scheduleDate, loginInfo=["",""]):
    os.chdir(directory)

    driver = webdriver.Chrome()
    driver.get("https://tweetdeck.twitter.com")
    driver.set_window_size(3000, 4000)

    if loginInfo[0] == "":
        driver.minimize_window()
        user = input("Enter email used for client's twitter account: ")
        password = input("Enter password used for client's twitter account: ")
        driver.set_window_size(3000, 4000)
    else:
        user = loginInfo[0]
        password = loginInfo[1]

    element = driver.find_element_by_class_name("Button")
    element.click()

    sleep(2)

    user_element = driver.find_element_by_css_selector("input[type='text']")
    pass_element = driver.find_element_by_css_selector("input[type='password']")


    user_element.send_keys(user)
    pass_element.send_keys(password)

    element = driver.find_element_by_css_selector("div[role='button']")
    element.click()

    # cwd = os.getcwd()
    # directory = os.path.join(cwd, "y")

    # fName = "y.txt"

    # os.chdir(directory)
    sleep(.5)
    attempts = 0
    while attempts <= 4:
        try:
            element = driver.find_element_by_xpath('//span[text()="No, thanks"]')
            element.click()
            break
        except:
            sleep(.5)
        attempts += 1

    sleep(.5)
    
    try:
        element = driver.find_element_by_css_selector("button.js-show-drawer")
        element.click()
        sleep(.3)
        element = driver.find_element_by_css_selector("input.js-compose-stay-open")
        element.click()
    except:
        pass

    scheduleDate = newScheduleDate(scheduleDate)

    attempts = 0
    while attempts <= 10:
        try:
            element = driver.find_element_by_css_selector("button.js-schedule-button")
            element.click()
            break
        except:
            sleep(1)
        attempts += 1


    sleep(.2)

    element.click()

    iterator = 1

    with open(fName, "r") as infile:
        for line in infile:
            element = driver.find_element_by_css_selector("button.js-schedule-button")
            element.click()
            

            title = driver.find_element_by_id("caltitle")
            curDate = title.text.split() #curDate[0] = month curDate[1] = year

            nextMonth = driver.find_element_by_css_selector("i.icon-arrow-r")

            #input (scheduleDate.strftime("%d"))

            while curDate[0] != scheduleDate.strftime("%B") or curDate[1] != scheduleDate.strftime("%Y"):
                nextMonth.click()

                title = driver.find_element_by_id("caltitle")
                curDate = title.text.split()
            element = driver.find_element_by_xpath('//a[@href="' + "#" + scheduleDate.strftime("%d").lstrip("0") + '" and not(@class="caloff")]')
            sleep(.3)
            element.click()
            sleep(.3)



            scheduleDate = newScheduleDate(scheduleDate)

                
            element = driver.find_element_by_css_selector("textarea.js-compose-text")
            
            for part in line.split("$RETURN"):
                element.send_keys(part)
                element.send_keys(Keys.RETURN)
            


            element = driver.find_element_by_css_selector("button.js-add-image-button")
            element.click()


            sleep(1)


            picName = os.path.join(directory, str(iterator) + ".png")
            handle_dialog(picName)
            iterator += 1

            sleep(.3)

            element = driver.find_element_by_css_selector("button.js-send-button")
            element.click()

            sleep(.3)
            sleep(7)

    
    driver.minimize_window()
    input("Finished scheduling twit. Verify & press enter to finish.")
    driver.close()


