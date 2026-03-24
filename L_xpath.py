import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/find_xpath_form")

first_name = driver.find_element("xpath", "//input[@name='first_name']")
last_name = driver.find_element("xpath", "//input[@name='last_name']")
city = driver.find_element("xpath", "//input[@class='form-control city']")
country = driver.find_element("xpath", "//input[@id='country']")

try:
    first_name.send_keys("Name")
    last_name.send_keys("Surname")
    city.send_keys("City")
    country.send_keys("Country")
    driver.find_element("xpath", "//button[@type='submit']").click()

finally:
    time.sleep(10)
    driver.quit()