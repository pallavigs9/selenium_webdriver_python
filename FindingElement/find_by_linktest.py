from selenium import webdriver

class find_by_linktext_partialtext():

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        element_by_linktext = driver.find_element_by_link_text("Login")

        if element_by_linktext is not None:
            print "We found element by LinkText."


        element_by_partialtext = driver.find_element_by_partial_link_text("Pract") #dont need to provide whole word.

        if element_by_partialtext is not None:
            print "We found element by PartialLinkText."


class_obj = find_by_linktext_partialtext()
class_obj.test()