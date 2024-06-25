from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Имя")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Фамилия")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@mail.ru")
    input4 = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Test.txt')
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

