from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def auto_window(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)

        #Get Parent handle
        parent_handle = driver.current_window_handle
        print "Parent handle: ",parent_handle
        #Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)
        #find all handle(all open windows)
        all_handles = driver.window_handles

        for handle in all_handles:

            if handle not in parent_handle:
                driver.switch_to_window(handle)
                print "Switched to window ", handle
                search_box = driver.find_element(By.ID, "search-courses")
                search_box.send_keys("python")
                time.sleep(3)
                break
        driver.switch_to_window(parent_handle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

class_call = SwitchToWindow()
class_call.auto_window()

