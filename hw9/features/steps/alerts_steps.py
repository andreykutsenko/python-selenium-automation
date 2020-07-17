from behave import when, then

@when('Alert is open')
def hover_over_button(context):
    context.app.alerts.create_alert()

@then('We can close Alert')
def verify_tooltip_shown(context):
    context.app.alerts.close_alert()

@when('Confirm is open')
def hover_over_button(context):
    context.app.alerts.create_confirm()

@then('We can close confirm')
def verify_tooltip_shown(context):
    context.app.alerts.close_confirm()

@when('Prompt is open')
def hover_over_button(context):
    context.app.alerts.create_prompt()

@then('We can close Prompt')
def verify_tooltip_shown(context):
    context.app.alerts.close_prompt()

