from selenium import webdriver

class find_by_class_name():

    def testing_class_name(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)

        element_by_ClassName = driver.find_element_by_class_name("displayed-class")
        element_by_ClassName.send_keys("Testing the element")

        if element_by_ClassName is not None:
            print "We found element by Class Name."

        element_by_tag_name = driver.find_element_by_tag_name("h1")
        text = element_by_tag_name.text

        if element_by_tag_name is not None:
            print "We found element by Tag Name and text on element is: " + text


class_obj = find_by_class_name()
class_obj.testing_class_name()