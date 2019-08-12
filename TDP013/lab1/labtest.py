# NOTE start webserver with python -m SimpleHTTPServer
# from the folder with html files
print "Don't forget to start the webserver with 'python3 -m SimpleHTTPServer"
# Will try to do this with python3 now...
# Hence obsolete

print "This is old... use python3 version"

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys         # For Keys.RETURN (if implemented :-)
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#import foo.foo.actionChains
import time
import unittest

# Se: 2.3. Using Selenium to write tests

class Kvitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    # def test_google_search_cheese(self):
    #     driver = self.driver
    #     driver.get("http://www.google.com")
    #     self.assertIn("Google", driver.title)

    #     # find the element that's name attribute is q (the google search box)
    #     inputElement = driver.find_element_by_name("q")

    #     # type in the search
    #     inputElement.send_keys("Cheese!")
        
    #     # submit the form (although google automatically searches now without submitting)
    #     inputElement.submit()
    #     # elem.send_keys(Keys.RETURN) # alternate way to send
        
    #     # the page is ajaxy so the title is originally this:
    #     print driver.title
        
    #     #try:
    #     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    #     WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))
        
    #     # You should see "cheese! - Google Search"
    #     print driver.title 
    #     self.assertIn("Cheese", driver.title)




    def test_kvitter_enter_text(self):
        driver = self.driver
        driver.get("http://0.0.0.0:8000")
        inputElement = driver.find_element_by_id("input")
        inputElement.send_keys("Cheese!")
        sendButton = driver.find_element_by_name("sendButton")
        actions = ActionChains(driver)
        actions.click(on_element = sendButton)
        print driver.title
        WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))
        assert "Cheese." in driver.page_source
        
    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()

