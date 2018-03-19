from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class HomeawayExercise():

    def auto_homeaway(self):
        baseUrl = "https://www.homeaway.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #Going to where to searchbox
        destination = driver.find_element(By.XPATH, "//input[@id='searchKeywords']")
        destination.send_keys("Lake Tahoe")
        time.sleep(2)
        #Entering checkin and check-out date
        checkIn = driver.find_element(By.NAME, "from-date")
        checkIn.click()
        check_in_date = driver.find_element_by_xpath('//div[@data-formatted-date="2018-01-18"]')
        check_in_date.click()
        time.sleep(2)
        checkOut= driver.find_element_by_xpath('//div[@data-formatted-date="2018-01-27"]')
        checkOut.click()
        time.sleep(2)

        Guest = driver.find_element_by_xpath("//input[@name='adults']")
        Guest.clear()
        Guest.send_keys('2')
        time.sleep(2)
        search_btn = driver.find_element(By.XPATH, '//button[@data-effect="ripple"]')
        search_btn.click()
        time.sleep(10)
        driver.quit()


class_call = HomeawayExercise()
class_call.auto_homeaway()