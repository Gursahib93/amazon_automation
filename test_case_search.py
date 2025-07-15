from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

webdriver = webdriver.Chrome()

def test_search():
    webdriver.get('https://amazon.ca')

    webdriver.maximize_window()
    wait = WebDriverWait(webdriver, 10)
    search_box = webdriver.find_element(By.ID,"twotabsearchtextbox")
    search_box.send_keys("Shoes")
    webdriver.find_element(By.ID,"nav-search-submit-button").click()
    sleep(2)
    assert "Shoes" in webdriver.title or "shoes" in webdriver.title.lower()
    webdriver.quit()

