from behave import given, when, then
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

base_url = 'https://account.blip.ai/register?returnUrl=%2Faccount'
name_menu = "FullName"
email_menu = "Email"
phone_menu = "PhoneNumber"
company_menu = "CompanySite"
key_menu = "Password"
element_check = "checkbox__icon"
employee_menu = "CompanyNumberOfEmployees"
select_employee = '//*[@id="ncid-4406"]'

@given(u'que acesso a pagina de cadastro')
def step_impl(context):
    context.web.get(base_url)
    
@when(u'preencho os dados solicitados')
def step_impl(context):
    context.element_menu = context.web.find_element_by_id(name_menu)
    context.element_menu.click()
    context.element_menu.send_keys('teste teste teste teste')
    context.element_email = context.web.find_element_by_id(email_menu)
    context.element_email.click()
    context.element_email.send_keys('teste@teste.com')
    context.element_phone = context.web.find_element_by_id(phone_menu)
    context.element_phone.click()
    context.element_phone.send_keys('00000000000')
    context.element_company = context.web.find_element_by_id(company_menu)
    context.element_company.click()
    context.element_company.send_keys('teste.teste.teste')
    context.element_key = context.web.find_element_by_id(key_menu)
    context.element_key.click()
    context.element_key.send_keys('teste12345')
    context.element_employee_select = context.web.find_elements_by_xpath(select_employee)
    sleep(3)
    print(context.element_employee_select)
    #obj_selected = Select(context.element_employee_select)
    #obj_selected.select_by_index(1)
    
    
@when(u'e os dados digitados nao coincidem com usuario cadastrado,clico na caixa de aceite dos termos e em cadastre-se gratis')
def step_impl(context):
    ...

@then(u'apresentado cadastro realizado com sucesso')
def step_impl(context):
    ...

@then(u'se os dados coincidirem com usuario ja cadastrado o botao cadastre-se gratis nao e habilitado')
def step_impl(context):
    ...

    