from selenium import webdriver

class BrowserInteraction():

    def browser_tests(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        #Maximize Window
        driver.maximize_window()
        #Open URL
        driver.get(base_url)
        #Get Title
        title = driver.title
        print "Web page title is: ", title
        #Get Current_URL
        current_url = driver.current_url
        print "Current Url is: ", current_url
        #Browser Refresh
        driver.refresh()
        #Open another URL
        driver.get("http://book.pythontips.com/en/latest/")
        #Browser Back
        driver.back()
        #Browser Forward
        driver.quit()

class_call = BrowserInteraction()
class_call.browser_tests()