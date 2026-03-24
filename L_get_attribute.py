import time
import math

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/get_attribute.html")

try:
  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
  x_chest_element = driver.find_element("css selector", "#treasure")
  x = x_chest_element.get_attribute("valuex")
  result = calc(x)
  
  field = driver.find_element("css selector", "#answer")
  field.send_keys(result)
  
  checkbox = driver.find_element("css selector", "#robotCheckbox")
  radiobutton = driver.find_element("css selector", "#robotsRule")
  
  checkbox.click()
  radiobutton.click()
  
  driver.find_element("css selector", "button.btn").click()

finally:
  time.sleep(10)
  driver.quit()