from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

webdriver = webdriver.Chrome()
webdriver.get('https://www.amazon.ca')
sleep(5)
webdriver.maximize_window()
search_box = webdriver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("Shoes")
webdriver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
webdriver.quit()


