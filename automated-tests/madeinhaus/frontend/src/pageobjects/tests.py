import pytest
import unittest
import basepage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baseelements import BasePageElement
from baselocators import LandingPageLocators
from baselocators import MenuLocators
from baselocators import WorkLocators
from baseassertions import MenuAssertions
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
import csv

class MadeInHAUSTests(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://madeinhaus.com")

  def test_does_title_match(self):
    landing_page = basepage.LandingPage(self.driver)
    page_title = landing_page.get_title_text()
    assert "HAUS | Maker of Things for Screens" in page_title

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

  def test_correct_case_studies_exist(self):
    #Go to Work Page
    menu = basepage.Menu(self.driver)
    time.sleep(7)
    menu.click_menu_burger_button()
    time.sleep(7)
    menu.click_work_link()
    time.sleep(7)
    work = basepage.Work(self.driver)

    #Open List of Expected Case Descriptions
    case_study_file = open('data/case-studies.csv')
    case_study_Reader = csv.reader(case_study_file)
    case_study_list = list(case_study_Reader)

    #Iterate Over the List - Assert expected case studies exist on site
    prod_counter = 1
    for expected_case_study in case_study_list:
      prod_case_study = self.driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[1]/div/div[%d]/div/a/div/h2'%prod_counter).get_attribute('outerHTML')
      prod_case_study.encode('utf-8')
      assert expected_case_study[0] in prod_case_study
      print expected_case_study[0] + " is contained in " + prod_case_study
      prod_counter +=1

    #Get count of live case studies - Assert no unexpected case studies exist on site
    prod_tile_count = len(self.driver.find_elements_by_class_name("tile"))
    case_study_count = len(case_study_list)

    print "Case Study is %d " %case_study_count
    print "Tile Count is %d " %prod_tile_count

    assert case_study_count == prod_tile_count

  def test_open_every_case_study(self):
    #Click on each actual panel
    menu = basepage.Menu(self.driver)
    time.sleep(7)
    menu.click_menu_burger_button()
    time.sleep(7)
    menu.click_work_link()
    time.sleep(7)
    work = basepage.Work(self.driver)

    #Grab list from locators and click through each actual case study
    expected_case_study_list = basepage.WorkLocators.CASE_STUDY_CLICK_THROUGH_LIST
    for expected_case_study in expected_case_study_list:
        live_case_study = self.driver.find_element_by_xpath('%s' % expected_case_study)  
        live_case_study.click()    
        print expected_case_study
        time.sleep(7)
        menu.go_to_work_page()

  def tearDown(self):
    self.driver.close()

  if __name__ == "__main__":
    unittest.main()

