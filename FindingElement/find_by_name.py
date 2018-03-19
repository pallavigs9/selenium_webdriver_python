from selenium import webdriver

class find_by_id_name():

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        element_by_id = driver.find_element_by_id("name")
        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_id and element_by_name is not None:
            print "We found element by Id."
            print "We found element by name."


class_obj = find_by_id_name()
class_obj.test()