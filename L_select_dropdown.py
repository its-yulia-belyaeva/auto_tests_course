import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/selects1.html")

try:
    num_1 = driver.find_element("css selector", "#num1")
    num_2 = driver.find_element("css selector", "#num2")
    summ = int(num_1.text) + int(num_2.text)

    dropdown = Select(driver.find_element("css selector", "#dropdown"))

    dropdown.select_by_value(str(summ))

    driver.find_element("css selector", "button.btn").click()

finally:
    time.sleep(10)
    driver.quit()