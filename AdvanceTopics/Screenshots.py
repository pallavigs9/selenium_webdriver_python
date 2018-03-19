from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():

    def take_screenshot(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        file_destination = "/home/pallavi/Desktop/screenshot.png"

        try:
            driver.save_screenshot(file_destination)
            print "Screenshot saved to -> ", file_destination
        except NotADirectory:
            print "Not a directory"

class_call = Screenshot()
class_call.take_screenshot()