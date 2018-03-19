from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RunSouthwest():

    def auto_complete(self):
        url = "https://www.southwest.com/"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)

        airport_code = driver.find_element(By.ID, "air-city-departure")
        airport_code.send_keys("New York")
        time.sleep(3)

        airport_select = driver.find_element(By.XPATH,
                                             "//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        airport_select.click()
        time.sleep(3)
        driver.quit()

class_call = RunSouthwest()
class_call.auto_complete()