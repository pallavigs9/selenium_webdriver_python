from selenium import webdriver

class find_by_Xpath_Css():

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        element_by_Xpath = driver.find_element_by_xpath("/html//select[@id='carselect']")

        if element_by_Xpath is not None:
            print "We found element by Xpath."


        element_by_Css = driver.find_element_by_css_selector("#displayed-text")

        if element_by_Css is not None:
            print "We found element by CSS."


class_obj = find_by_Xpath_Css()
class_obj.test()