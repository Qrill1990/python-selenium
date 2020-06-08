from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    first_name = browser.find_element_by_xpath("//input[@placeholder='Enter first name']").send_keys("Kirill")
    second_name = browser.find_element_by_xpath("//input[@placeholder='Enter last name']").send_keys("Lyubushkin")
    email = browser.find_element_by_xpath("//input[@placeholder='Enter email']").send_keys("123@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    choose = browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

finally:
    time.sleep(10)
    browser.quit()
