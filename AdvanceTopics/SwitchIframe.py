from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class auto_iframe():

    def switch_frame(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.execute_script("window.scrollBy(0, 1000);")
        #switch to iframe using id
        driver.switch_to_frame("courses-iframe")

        time.sleep(3)
        #search course
        iframe_searchBox = driver.find_element(By.ID, "search-courses")
        iframe_searchBox.send_keys("Python")
        time.sleep(2)
        #Switch back to parent handle
        driver.switch_to_default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test done!")

class_call = auto_iframe()
class_call.switch_frame()