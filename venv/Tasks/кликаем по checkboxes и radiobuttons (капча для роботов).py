from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)
x_element = browser.find_element_by_id("treasure")
box = x_element.get_attribute("valuex")
x = box
y = calc(x)
input1 = browser.find_element_by_xpath("//input[@id='answer']")
input1.send_keys(y)
checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
checkbox.click()
radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
radio.click()
submit = browser.find_element_by_xpath("//button[@class='btn btn-default']")
submit.click()

