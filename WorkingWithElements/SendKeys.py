from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class click_and_send_keys():

    def click_element(self, username, passwd1):

        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)# waits for 10 second to element to load

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click() # To click on the element

        user_email = driver.find_element(By.ID, "user_email")
        user_email.send_keys(username) # To send keys to the element
        time.sleep(3)

        user_pw = driver.find_element(By.ID, "user_password")
        user_pw.send_keys(passwd1)
        time.sleep(3)

        user_email.clear()
        user_pw.clear()
        time.sleep(3)
        driver.quit()


class_call = click_and_send_keys()
#class_call.click_element()
