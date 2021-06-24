from selenium.webdriver import Chrome

def before_all(context):
    context.web = Chrome()

def driver_back(context):
    ...

def after_step(context, step):
    print()

def after_all(context):
    ...



