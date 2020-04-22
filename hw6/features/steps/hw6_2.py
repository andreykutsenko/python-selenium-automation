from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

BS_LINK_LOCATOR = (By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
PAGE_LINK_TABLE_LOCATOR = (By.CSS_SELECTOR, "#zg_tabs li")
BANNER_TEXT_LOCATOR = (By.ID, 'zg_banner_text_wrapper')


@when('Clicks on Best Sellers link on the top menu')
def click_to_bs_link(context):
    bs_link = context.driver.find_element(*BS_LINK_LOCATOR)
    bs_link.click()

@then('Clicks on each top link and verify that new page opens')
def clicks_and_verifications_of_new_pages(context):
    context.page_list = context.driver.find_elements(*PAGE_LINK_TABLE_LOCATOR)
    # context.banner_text = context.driver.find_element(*BANNER_TEXT_LOCATOR)
    for i in range(len(context.page_list)):
        # context.page_list[i].click()
        context.driver.find_elements(*PAGE_LINK_TABLE_LOCATOR)[i].click()
        context.wait.until(EC.visibility_of_element_located(BANNER_TEXT_LOCATOR))
        # print(f"{context.driver.find_elements(*PAGE_LINK_TABLE_LOCATOR)[i].text} IN {context.driver.find_element(*BANNER_TEXT_LOCATOR).text}")
        assert context.driver.find_elements(*PAGE_LINK_TABLE_LOCATOR)[i].text in context.driver.find_element(*BANNER_TEXT_LOCATOR).text