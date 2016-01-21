import basepage
from baseelements import BasePageElement
from baselocators import LandingPageLocators
from baselocators import MenuLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import logging

class MenuAssertions(object):
	
  def check_work_link_exists(self):
    try:
        self.driver.find_element(*MenuLocators.WORK_LINK)
    except NoSuchElementException:
        return False
    return True