from behave import when

@when('Click on hamburger menu')
def click_hamburger_menu_button(context):
    context.app.hamburgermenu_page.click_hamburger_menu()

@when('Click on Amazon Music menu item')
def click_amazon_menu_item(context):
    context.app.hamburgermenu_page.click_amazon_music_menu()