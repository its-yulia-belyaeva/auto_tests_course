import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/registration2.html")

first_name = driver.find_element("css selector", ".first_block .first")
last_name = driver.find_element("css selector", ".first_block .second")
email = driver.find_element("css selector", ".first_block .third")

try:
    first_name.send_keys("Name")
    last_name.send_keys("Surname")
    email.send_keys("Email")

    driver.find_element("css selector", "div .btn").click()
    time.sleep(1)

    welcome_text_elt = driver.find_element("css selector", "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    driver.quit()
