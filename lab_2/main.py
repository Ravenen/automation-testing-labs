from math import log, sin

import selenium.webdriver.support.expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/explicit_wait2.html')

    found = WebDriverWait(driver, timeout=30).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    if found:
        book_button = driver.find_element(By.ID, 'book')
        book_button.click()

        x = int(driver.find_element(By.ID, 'input_value').text)
        print(f'x = {x}')

        y = log(abs(12 * sin(x)))
        print(f'y(x) = ln(abs(12 * sin(x))) = {y}')

        answer_field = driver.find_element(By.ID, 'answer')
        answer_field.clear()
        answer_field.send_keys(y)

        submit_button = driver.find_element(By.ID, 'solve')
        submit_button.click()

        try:
            alert = driver.switch_to.alert
            print(alert.text)
            alert.accept()
        except:
            print('No alerts are present')

    driver.quit()
