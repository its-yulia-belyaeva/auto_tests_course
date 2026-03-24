import time
import math

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/find_link_text")

link_number = str(math.ceil(math.pow(math.pi, math.e)*10000))

driver.find_element("link text", link_number).click()

first_name = driver.find_element("css selector", "[name='first_name']")
last_name = driver.find_element("css selector", "[name='last_name']")
city = driver.find_element("css selector", ".city")
country = driver.find_element("css selector", "#country")

try:
    first_name.send_keys("Name")
    last_name.send_keys("Surname")
    city.send_keys("City")
    country.send_keys("Country")
    driver.find_element("css selector", "div .btn").click()

finally:
    time.sleep(10)
    driver.quit()