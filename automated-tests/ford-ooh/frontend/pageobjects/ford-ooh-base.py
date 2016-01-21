import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys

class Ford_Ooh_Base(unittest.TestCase):

    def setUp(self):
    	self.driver = webdriver.Firefox()
    	self.driver.implicitly_wait(30)
    	self.base_url = "http://qafordbydesign.marketingassociates.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_page_title_click_button(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.assertIn("For By Design. By You.", driver.title)
        

    def tearDown(self):
        #self.driver.close()
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()