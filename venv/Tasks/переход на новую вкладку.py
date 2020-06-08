from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    button = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()
    browser.switch_to_window(browser.window_handles[1])
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    result = calc(x)
    field = browser.find_element_by_xpath("//input[@id='answer']").send_keys(result)
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

finally:
    time.sleep(5)
    browser.quit()