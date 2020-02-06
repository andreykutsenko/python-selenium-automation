from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//div[@id='csg-search-cu']//input[@type='search'][@id='helpsearch']")
search_button = driver.find_element(By.XPATH, "//div[@id='csg-search-cu']//input[@class='a-button-input'][@type='submit']")

# actions
search.clear()
search.send_keys('Cancel order')

# click search_button
search_button.click()

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']//h1[text()='Cancel Items or Orders']").text

driver.quit()