    # def test_google_search_cheese(self):
    #     driver = self.driver
    #     driver.get("http://www.google.com")
    #     self.assertIn("Google", driver.title)

    #     # find the element that's name attribute is q (the google search box)
    #     inputElement = driver.find_element_by_name("q")

    #     # type in the search
    #     inputElement.send_keys("Cheese!")

    #     # submit the form (although google automatically searches now
    #     #   without submitting)
    #     inputElement.submit()
    #     # elem.send_keys(Keys.RETURN) # alternate way to send

    #     # the page is ajaxy so the title is originally this:
    #     print(driver.title)

    #     # try:
    #     # we have to wait for the page to refresh, the last thing that seems
    #     # to be updated is the title
    #     WebDriverWait(driver, 10).until(
    #         lambda driver: driver.title.lower().startswith("cheese!"))

    #     # You should see "cheese! - Google Search"
    #     print(driver.title)
    #     self.assertIn("Cheese", driver.title)