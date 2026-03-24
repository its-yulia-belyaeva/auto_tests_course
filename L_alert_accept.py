import time
import math

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/alert_accept.html")

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
    start_btn = driver.find_element("css selector", "button.btn")
    start_btn.click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    
    x_elt = driver.find_element("css selector", "#input_value")
    x = x_elt.text

    answer_field = driver.find_element("css selector", "#answer")
    answer_field.send_keys(calc(x))

    submit = driver.find_element("css selector", "button.btn")
    submit.click()

finally:
    time.sleep(10)
    driver.quit()