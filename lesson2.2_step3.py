from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, "num1").text
    num_2 = browser.find_element(By.ID, "num2").text   
    sum = str(int(num_1)+int(num_2))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(sum)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

