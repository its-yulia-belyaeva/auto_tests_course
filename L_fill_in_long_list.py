import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/huge_form.html")

try:
    fields = driver.find_elements("css selector", "input")
    
    for i in range(len(fields)):
        fields[i].send_keys("test")
    
    driver.find_element("css selector", "div .btn").click()

finally:
    time.sleep(10)
    driver.quit()