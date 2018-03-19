from selenium import webdriver
import time

class RadioButtonsCheckboxes():

    def radio_checkbox_test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)

        bmw_radiobtn = driver.find_element_by_id("bmwradio")
        bmw_radiobtn.click()
        time.sleep(3)

        benz_radiobtn = driver.find_element_by_id("benzradio")
        benz_radiobtn.click()
        time.sleep(3)

        bmw_checkbox = driver.find_element_by_id("bmwcheck")
        bmw_checkbox.click()
        time.sleep(3)

        honda_checkbox = driver.find_element_by_id("hondacheck")
        honda_checkbox.click()
        time.sleep(3)

class_call = RadioButtonsCheckboxes()
class_call.radio_checkbox_test()