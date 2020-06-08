from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link='http://SunInJuly.github.io/execute_script.html'
    browser.get(link)
    a = browser.find_element_by_xpath("//span[@id='input_value']").text
    b = calc(a)
    browser.execute_script("window.scrollBy(0, 100);")
    field = browser.find_element_by_xpath("//input[@id='answer']")
    field.send_keys(b)
    
    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radio.click()
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

finally:
    time.sleep(7)
    browser.quit()

