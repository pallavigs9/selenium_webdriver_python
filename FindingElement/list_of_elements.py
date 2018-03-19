from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def elements_list(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)

