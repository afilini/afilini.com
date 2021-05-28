#!/usr/bin/env python3

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://localhost:1313')

driver.execute_script("let e = document.getElementsByTagName('html')[0]; e.style.width = '900px'; e.style.height = '600px'; ")

element = driver.find_element_by_tag_name('html')
element_png = element.screenshot_as_png
with open("./static/images/share.png", "wb") as file:
    file.write(element_png)

driver.quit()
