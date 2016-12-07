from baseelements import BasePageElement
from baselocators import LandingPageLocators
from baselocators import MenuLocators
from baselocators import WorkLocators
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
	 	return self.driver.title


class Menu(BasePage):
	"""Menu actions"""

	def go_to_work_page(self):
		self.driver.get("https://madeinhaus.com/work")

	def click_menu_burger_button(self):
		element = self.driver.find_element(*MenuLocators.MENU_BURGER_BUTTON)
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

class Work(BasePage):
	"""Work page actions"""

	def get_description(self):
		description = self.driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[1]/div/div[2]/div/a/div/h2').get_attribute('outerHTML')
		return description

	def click_work_burger_button(self):
		element = self.driver.find_element(*WorkLocators.WORK_BURGER_BUTTON)
		element.click()

	def click_alice_case_study(self):
		element = self.driver.find_element(*WorkLocators.ALICE_CASE_STUDY)
		element.click()

	def click_ford_by_design_case_study(self):
		element = self.driver.find_element(*WorkLocators.FORD_BY_DESIGN_CASE_STUDY)
		element.click()

# class MainPage(BasePage):
# 	"""Main page action methods"""

