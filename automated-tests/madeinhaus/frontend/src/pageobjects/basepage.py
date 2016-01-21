from baseelements import BasePageElement
from baselocators import LandingPageLocators
from baselocators import MenuLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time

class BasePage(object):
	"""Base class to initialize the base page that will be called from all pages"""

	def __init__(self, driver):
		self.driver = driver

class LandingPage(BasePage):
	"""landing page actions"""

	def get_title_text(self):
	 	return "HAUS - Maker of Things" in self.driver.title


class Menu(BasePage):
	"""Menu actions"""

	def click_burger_button(self):
		element = self.driver.find_element(*MenuLocators.BURGER_BUTTON)
		element.click()

	def click_work_link(self):
		element = self.driver.find_element(*MenuLocators.WORK_LINK)
		element.click()

	def click_reel_link(self):
		element = self.driver.find_element(*MenuLocators.REEL_LINK)
		element.click()

	def click_menu_close_button(self):
		element = self.driver.find_element(*MenuLocators.MENU_CLOSE_BUTTON)
		element.click()

	def click_studio_link(self):
		element = self.driver.find_element(*MenuLocators.STUDIO_LINK)
		element.click()

	def click_contact_link(self):
		element = self.driver.find_element(*MenuLocators.CONTACT_LINK)
		element.click()

	def click_careers_link(self):
		element = self.driver.find_element(*MenuLocators.CAREERS_LINK)
		element.click()

# class MainPage(BasePage):
# 	"""Main page action methods"""

