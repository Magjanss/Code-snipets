#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys          # For Keys.RETURN
from selenium.webdriver.support.ui import WebDriverWait  # avail since 2.4.0
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

print("Don't forget to start the webserver with 'python3 -m http.server'")

# Se: 2.3. Using Selenium to write tests


class Kvitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_kvitter_enter_text(self):
        print("Testing to enter text... ", end='')
        driver = self.driver
        driver.get("http://0.0.0.0:8000")
        assert "Cheese" not in driver.page_source
        inputElement = driver.find_element_by_id("inputText")
        inputElement.send_keys("Cheese!")
        sendButton = driver.find_element_by_name("sendButton")
        actions = ActionChains(driver)
        actions.click(sendButton).perform()
        # Find a way to get the latest item in the messages list
        # WebDriverWait(driver, 10).until(
        #     lambda driver: driver.title.lower().startswith("cheese!"))
        assert "Cheese" in driver.page_source
        # assert "spunk" in driver.page_source # this is supposed to fail
        print("DONE")

    def test_kvittrer_message_size(self):
        print(\n"Testing sizelimits:")
        driver = self.driver
        driver.get("http://0.0.0.0:8000")
        inputElement = driver.find_element_by_id("inputText")
        # print(inputElement.get_property("vakue"))
        assert "Felmeddelande" not in driver.page_source
        actions = ActionChains(driver)
        print("Testing size 0:", end='')
        driver.implicitly_wait(10)
        inputElement.clear()
        # inputElement.send_keys("Cheese!")
        sendButton = driver.find_element_by_name("sendButton")
        actions.click(sendButton).perform()
        # assert "lorem ipsum" not in driver.page_source
        assert "Felmeddelande" in driver.page_source
        print("DONE")
        # WebDriverWait(driver, 5).until(
        #    lambda driver: driver.title.lower().startswith("cheese!"))
        inputElement.clear()
        inputElement.send_keys(2 * "0123456789")
        actions.click(sendButton).perform()
        print("Testing size 140+:", end='')
        assert "Felmeddelande" not in driver.page_source
        inputElement.clear()
        inputElement.send_keys(15 * "0123456789")
        actions.click(sendButton).perform()
        assert "Felmeddelande" in driver.page_source
        print("DONE")

    def tearDown(self):
        # pass
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
