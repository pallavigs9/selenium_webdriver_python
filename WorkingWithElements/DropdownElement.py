from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():

    def dropdown_select(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(30)

        dropdown_element = driver.find_element_by_id("carselect")
        select_items = Select(dropdown_element)

        select_items.select_by_value("benz")
        print "benz by value selected."
        time.sleep(2)

        select_items.select_by_index(2)
        print "Honda selected by index."
        time.sleep(2)

        select_items.select_by_visible_text("BMW")
        print "Bmw selected by Text"

class_call = DropdownSelect()
class_call.dropdown_select()

