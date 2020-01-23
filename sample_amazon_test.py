from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_button = driver.find_element(By.XPATH, "//div[@id='nav-search']//input[@class='nav-input'][@value='Go']")

search.clear()
search.send_keys('lego')

# wait for 2 sec
sleep(2)

# click search_button
search_button.click()

# verify
assert 'lego' in driver.find_element(By.XPATH, "//div[@id='search']//span[@class='a-color-state a-text-bold']").text

driver.quit()