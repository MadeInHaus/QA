from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
	"""Bese page class that is initialized on every page object class."""

	def __set__(self, obj, value):
		"""sets the text to the value supplied"""
		driver = obj.driver
		WebDriverWait(driver, 1000).until(
			lambda driver:  driver.find_element_by_name(self.locator))
		driver.find_element_by_name(self.locator).send_keys(value)

	def __get__(self, obj, owner):
		"""Gets the text of the specified object"""
		driver = obj.driver
		WebDriverWait(driver, 1000).until(
			lambda driver:  driver.find_elment_by_name(self.locator))
		element = driver.find_element_by_name(self.locator)
		return element.get_attribute("value")

	def go_to(self, url):
		url = self.base_url + url
		self.driver.get("url")