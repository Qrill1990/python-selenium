from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/selects2.html'
    browser.get(link)
    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text
    x = int(number1)
    y = int(number2)
    number3 = x+y
    number4 = str(number3)
    select = Select (browser.find_element_by_tag_name("select"))
    select.select_by_value(number4)
    submit = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()