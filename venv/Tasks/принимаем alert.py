from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    journey = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    confirm = browser.switch_to_alert().accept()
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    result = calc(x)
    field = browser.find_element_by_xpath("//input[@id='answer']").send_keys(result)
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

finally:
    time.sleep(7)
    browser.quit()