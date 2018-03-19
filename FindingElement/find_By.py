from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def element_By(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)

        element_by_Id = driver.find_element(By.ID, "name")
        if element_by_Id is not None:
            print "we found element by Id."

        element_by_Xpath = driver.find_element(By.XPATH, "/html//input[@id='displayed-text']")

        if element_by_Xpath is not None:
            print "we found element by XPath."

        element_by_link_text = driver.find_element(By.LINK_TEXT, "Login")

        if element_by_link_text is not None:
            print "we found element by Link Text."

class_obj = ByDemo()
class_obj.element_By()
    