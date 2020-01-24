from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# open the url
driver.get('https://www.amazon.com/')

button_orders = driver.find_element(By.XPATH, "//div[@id='nav-tools']//a[@id='nav-orders']")

# click button
button_orders.click()

# verify
assert 'Sign-In' in driver.find_element(By.XPATH, "//div[@id='authportal-main-section']//h1[@class='a-spacing-small']").text

# wait for 2 sec
sleep(2)

driver.quit()