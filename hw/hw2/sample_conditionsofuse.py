from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

# actions
button_login = driver.find_element(By.XPATH, "//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner']").click()
button_condi = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']").click()

# verify
assert 'Conditions of Use' in driver.find_element(By.XPATH, "//span[text()='Conditions of Use']").text

driver.quit()