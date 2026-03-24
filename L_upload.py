import time
import os

from selenium import webdriver
driver = webdriver.Chrome()

#Местоположение файла в текущей директории
#cur_dir = os.path.abspath(os.path.dirname(__file__))
#file_path = os.path.join(cur_dir, "test.txt")

driver.get("https://suninjuly.github.io/file_input.html")

try:
    name = driver.find_element("css selector", "[name='firstname']")
    surname = driver.find_element("css selector", "[name='lastname']")
    email = driver.find_element("css selector", "[name='email']")
    upload = driver.find_element("css selector", "[name='file']")
    submit = driver.find_element("css selector", "button.btn")

    name.send_keys("Name")
    surname.send_keys("Surname")
    email.send_keys("email@example.com")
    upload.send_keys(f"{os.getcwd()}\\auto_lessons\\test.txt")
    submit.click()

finally:
    time.sleep(10)
    driver.quit()