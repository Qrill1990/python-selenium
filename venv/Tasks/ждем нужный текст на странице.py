from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100")
    )
    book = browser.find_element_by_xpath("//button[@id='book']").click()
    number = browser.find_element_by_xpath("//span[@id='input_value']").text
    result = calc(number)
    field = browser.find_element_by_xpath("//input[@id='answer']").send_keys(result)
    submit = browser.find_element_by_xpath("//button[@id='solve']").click()

finally:
    time.sleep(10)
    browser.quit()