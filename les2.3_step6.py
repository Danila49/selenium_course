from selenium import webdriver
import time
import math

def fun(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button=browser.find_element_by_class_name('trollface.btn').click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)

    x=browser.find_element_by_id('input_value').text
    y=fun(int(x))
    input1=browser.find_element_by_id('answer').send_keys(y)
    button2=browser.find_element_by_class_name('btn.btn').click()

finally:
    time.sleep(30)
    browser.quit()

