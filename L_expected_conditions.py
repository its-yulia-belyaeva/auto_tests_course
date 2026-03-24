import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 30, poll_frequency=0.5)

driver.get("https://suninjuly.github.io/explicit_wait2.html")

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
    price = ("css selector", "#price")
    wait.until(EC.text_to_be_present_in_element(price, "$100"))

    book = driver.find_element("css selector", "#book")
    book.click()

    x_elt = driver.find_element("css selector", "#input_value")
    x = x_elt.text

    answer_field = driver.find_element("css selector", "#answer")
    submit = driver.find_element("css selector", "#solve")

    answer_field.send_keys(calc(x))
    submit.click()

finally:
    time.sleep(10)
    driver.quit()