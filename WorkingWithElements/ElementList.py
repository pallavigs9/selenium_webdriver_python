from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementListAccess():

    def element_list(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        radio_btnList = driver.find_elements(
            By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]") # Advance Xpath
        size = len(radio_btnList)
        print "Size of element list: ", size

        for radio_btn in radio_btnList:
            is_select = radio_btn.is_selected()

            if not is_select:
                radio_btn.click()
                time.sleep(3)


class_call = ElementListAccess()
class_call.element_list()