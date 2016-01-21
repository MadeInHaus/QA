import unittest
import basepage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baseelements import BasePageElement
from baselocators import LandingPageLocators
from baselocators import MenuLocators
from baseassertions import MenuAssertions
import time
import logging

class MadeInHAUSTests(unittest.TestCase):

  logging.basicConfig( level=logging.DEBUG )

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://madeinhaus.com")
   
  # def test_does_title_match(self):
  #   landing_page = basepage.LandingPage(self.driver)
  #   page_title = landing_page.get_title_text()
  #   print page_title

  def test_menu_links(self):
    menu = basepage.Menu(self.driver)
    time.sleep(7)
    menu.click_burger_button()
    time.sleep(3)
    menu.click_work_link()
    time.sleep(3)
    menu.click_burger_button()
    time.sleep(3)
    menu.click_reel_link()
    time.sleep(3)
    menu.click_burger_button()
    time.sleep(3)
    menu.click_studio_link()
    time.sleep(3)
    menu.click_burger_button()
    time.sleep(3)
    menu.click_contact_link()
    time.sleep(3)
    menu.click_burger_button()
    time.sleep(3)
    menu.click_careers_link()
    time.sleep(3)
    menu.click_burger_button()
    time.sleep(3)

  def tearDown(self):
    self.driver.close()

  if __name__ == "__main__":
    unittest.main()

