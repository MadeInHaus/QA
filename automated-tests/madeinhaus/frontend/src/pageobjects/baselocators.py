from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LandingPageLocators(object):
	"""A class for main page locators.  All main page locators should come here"""
	FEATURED_WORK_BUTTON = (By.CLASS_NAME, 'fancy-button')

class MenuLocators(object):
	MENU_BURGER_BUTTON = (By.XPATH, '//div[@id="app"]/div/div/div/div/span[3]')
	MENU_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.patties')
	WORK_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[2]/ul/li/a')
	REEL_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[2]/ul/li[2]/a')
	STUDIO_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[2]/ul/li[3]/a')
	CONTACT_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[2]/ul/li[5]/a')
	CAREERS_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[2]/ul/li[4]/a')

class WorkLocators(object):
	WORK_BURGER_BUTTON = (By.XPATH, '//div[@id="app"]/div/div/div/div')
	ALICE_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[1]/div/a') 
	FORD_BY_DESIGN_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[2]/div/a')
	#DESCRIPTION = (By.XPATH '//*[@id="app"]/div/main/div/div[1]/div/div[2]/div/a/div/h3')

	#//*[@id="app"]/div/main/div/div[1]/div/div[2]/div/a	


