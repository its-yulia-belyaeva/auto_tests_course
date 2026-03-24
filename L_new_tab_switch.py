import time
import math

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/redirect_accept.html")

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    start_btn = driver.find_element("css selector", "button.btn")
    start_btn.click()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    x_elt = driver.find_element("css selector", "#input_value")
    x = x_elt.text

    answer_field = driver.find_element("css selector", "#answer")
    submit = driver.find_element("css selector", "button.btn")

    answer_field.send_keys(calc(x))
    submit.click()

finally:
    time.sleep(10)
    driver.quit()