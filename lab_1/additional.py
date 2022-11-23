from time import sleep

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://demo-store.seleniumacademy.com/customer/account/create/')

    first_name_field = driver.find_element(By.XPATH, '//*[@id="firstname"]')
    middle_name_field = driver.find_element(By.XPATH, '//*[@id="middlename"]')
    last_name_field = driver.find_element(By.XPATH, '//*[@id="lastname"]')
    email_field = driver.find_element(By.XPATH, '//*[@id="email_address"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    confirm_password_field = driver.find_element(By.XPATH, '//*[@id="confirmation"]')

    fake = Faker()
    first_name = fake.first_name()
    print(first_name)
    middle_name = fake.first_name()
    print(middle_name)
    last_name = fake.last_name()
    print(last_name)
    email = fake.email()
    print(email)
    password = fake.password()
    print(password)

    first_name_field.send_keys(first_name)
    middle_name_field.send_keys(middle_name)
    last_name_field.send_keys(last_name)
    email_field.send_keys(email)
    password_field.send_keys(password)
    confirm_password_field.send_keys(password)

    register_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')
    register_button.click()

    sleep(5)

    driver.quit()
