import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/simple_form_find_task.html")

first_name = driver.find_element("css selector", "[name='first_name']")
last_name = driver.find_element("css selector", "[name='last_name']")
city = driver.find_element("css selector", ".city")
country = driver.find_element("css selector", "#country")

try:
    first_name.send_keys("Name")
    last_name.send_keys("Surname")
    city.send_keys("City")
    country.send_keys("Country")
    driver.find_element("css selector", "#submit_button").click()

finally:
    time.sleep(10)
    driver.quit()