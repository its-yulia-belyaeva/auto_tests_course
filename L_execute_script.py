import time
import math

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/execute_script.html")

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = driver.find_element("css selector", "#input_value")
    x = x_element.text

    answer_field = driver.find_element("css selector", "#answer")
    checkbox = driver.find_element("css selector", "#robotCheckbox")
    radiobutton = driver.find_element("css selector", "#robotsRule")
    submit = driver.find_element("css selector", "button.btn")

    driver.execute_script("return arguments[0].scrollIntoView(true);", answer_field)

    answer_field.send_keys(calc(x))
    checkbox.click()
    radiobutton.click()
    submit.click()

finally:
    time.sleep(10)
    driver.quit()
