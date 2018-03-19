from selenium import webdriver
import time

class ElementState():

    def check_state(self):
        base_url = "http://www.google.com/"
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        search_box_id1 = driver.find_element_by_id("gs_taif0")
        state_of_sb1 = search_box_id1.is_enabled()  # Return True for Enabled and False for disabled.
        print "State is enabled? -> ", state_of_sb1

        search_box = driver.find_element_by_id("lst-ib")
        search_box.send_keys("letskodeit")

        time.sleep(3)

        driver.quit()

class_call = ElementState()
class_call.check_state()

