from selenium.webdriver.common.by import By 

class LandingPageLocators(object):
	"""A class for main page locators.  All main page locators should come here"""
	FEATURED_WORK_BUTTON = (By.CLASS_NAME, 'fancy-button')

class MenuLocators(object):
	MENU_BURGER_BUTTON = (By.XPATH, '//div[@id="app"]/div/div/div/div/span[3]')
	MENU_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.patties')
	WORK_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[3]/ul/li/a')
	REEL_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[3]/ul/li[2]/a')
	STUDIO_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[3]/ul/li[3]/a')
	CONTACT_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[3]/ul/li[5]/a')
	CAREERS_LINK = (By.XPATH, '//div[@id="app"]/div/div/div[3]/ul/li[4]/a')

class WorkLocators(object):
	WORK_BURGER_BUTTON = (By.XPATH, '//div[@id="app"]/div/div/div/div')

	BLB_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[1]/div/a')
	HYUNDAI_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[2]/div/a')
	DRAGON_AGE_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[3]/div/a')
	SURFACE_AIR_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[4]/div/a')
	DNG_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[5]/div/a')
	NETFLIX_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[6]/div/a')
	AMERICAN_ODYSSEY_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[7]/div/a')
	HONDA_HRV_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[8]/div/a')
	NISSAN_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[9]/div/a')
	BANANA_BOAT_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[10]/div/a')
	TAYLOR_MADE_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[11]/div/a')
	MUSTANG_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[12]/div/a')
	GREY_GOOSE_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[13]/div/a')
	POWERADE_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[14]/div/a')
	PLAYSTATION_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[15]/div/a')
	MEAN_STINKS_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[16]/div/a')
	LUNESTRA_CASE_STUDY = (By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div[17]/div/a')

	CASE_STUDY_CLICK_THROUGH_LIST = ['//*[@id="app"]/div/main/div/div[1]/div/div[1]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[2]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[3]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[4]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[5]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[6]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[7]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[8]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[9]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[10]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[11]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[12]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[13]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[14]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[15]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[16]/div/a','//*[@id="app"]/div/main/div/div[1]/div/div[17]/div/a']


