from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep

from datetime import datetime
from datetime import timedelta

import calendar

import os
import threading

def newScheduleDate(scheduleDate):
    return scheduleDate + timedelta(days=7)

def f_scheduler(fName, directory, scheduleDate, url=""):
    os.chdir(directory)

    if url == "":
        url = input("\n\nInput the client's facebook URL:\n")
           

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("https://www.facebook.com")
    driver.set_window_size(3000, 4000)

    element = driver.find_element_by_id("email")
    element.send_keys("customerservice@theomcgroup.com")

    element = driver.find_element_by_id("pass")
    element.send_keys(r"/6TB.?85#QNynz{cA")


    element = driver.find_element_by_id("loginbutton")
    element.click()

    driver.get(url+"/publishing_tools/")



    

    scheduleDate = newScheduleDate(scheduleDate)




    iterator = 1
    with open(fName, "r") as infile:
        for line in infile:
            attempts = 0
            while attempts <= 20:
                try:
                    element = driver.find_element_by_xpath('//button[@data-testid="pages_publishing_tool_create_button"]')
                    element.click()
                    break
                except:
                    sleep(2)
                attempts += 1

            attempts = 0
            while attempts <= 10:
                try:
                    element = driver.find_element_by_xpath('//div[@data-testid="photo-video-button"]')
                    element.click()
                    break
                except:
                    sleep(1)
                attempts += 1

            sleep(.5)

            #send photo
            attempts = 0
            while attempts <= 10:
                try:
                    element = driver.find_element_by_xpath('//input[@data-testid="media-attachment-add-photo"]')
                    # action = webdriver.common.action_chains.ActionChains(driver)
                    # action.move_to_element_with_offset(element, 18900, 290)
                    # action.click()
                    # action.perform()
                    # sleep(1)

                    picName = os.path.join(directory, str(iterator)+".png")
                    # handle_dialog(picName)
                    
                    element.send_keys(picName)
                    break
                except:
                    sleep(1)
                attempts += 1


            sleep(.3)
            #########





            #send caption
            element = driver.find_element_by_xpath('//div[@data-testid="status-attachment-mentions-input"]')
            for part in line.split("$RETURN"):
                element.send_keys(part)
                element.send_keys(Keys.RETURN)

            sleep(.5)




            #start scheduling
            element = driver.find_element_by_xpath('//button[@aria-haspopup="true" and @role="button"]')
            element.click()
            sleep(.1)

            element = driver.find_element_by_xpath('//span[text()="Schedule"]')
            element.click()
            sleep(.1)

            element = driver.find_element_by_xpath('//input[@placeholder="mm/dd/yyyy"]')
            element.clear()
            sleep(.1)

            dateAsString = scheduleDate.strftime('%m') + "/" + scheduleDate.strftime('%d') + "/" + scheduleDate.strftime('%Y')
            element.send_keys(dateAsString)

            sleep(.1)

            element = driver.find_element_by_xpath('//button[@action="confirm"]')
            element.click()
            #stop scheduling


            #post button
            element = driver.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]') 
            element.click()

            #add week to date and iterate picture counter
            scheduleDate = newScheduleDate(scheduleDate)
            iterator += 1

            try:
                WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except TimeoutException:
                print("no alert")
    driver.minimize_window()
    input("Finished scheduling facbok. Verify & press enter to finish.")
    driver.close()


