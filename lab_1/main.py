from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/math.html')

    x = int(driver.find_element(By.ID, 'input_value').text)
    print(f'x = {x}')

    y = log(abs(12 * sin(x)))
    print(f'y(x) = ln(abs(12 * sin(x))) = {y}')

    answer_field = driver.find_element(By.ID, 'answer')
    answer_field.clear()
    answer_field.send_keys(y)

    robot_checkbox = driver.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radio = driver.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    try:
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('No alerts are present')

    driver.quit()
