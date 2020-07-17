from selenium import webdriver
from subprocess import call


def openChrome():
    chromedriver_location = "./chromedriver"
    driver = webdriver.Chrome(chromedriver_location)
    
    driver.get('https://yuma.arizona.edu/request-info')
    driver.implicitly_wait(3)
    first_name = '//*[@id="form_913fa45e-b4ad-48d3-a26b-0e15918e3679"]'
    last_name = '//*[@id="form_647beaf1-ccb7-4511-8a94-8bdadab42987"]'
    email = '//*[@id="form_31880a0a-62ae-4e68-961b-a79cb7b53e76"]'
    text_req = '//*[@id="form_9d8df43b-f59f-4bb4-85b6-8a22247c7c34_1"]'
    semester_start = '//*[@id="form_7ab361b8-930e-497c-b012-75b88f84447d"]'
    program = '//*[@id="form_d88142c1-9660-4835-80f6-6c472d457eb9"]'
    questions = '//*[@id="form_51e0d29e-1078-4f6d-a62a-376e615f7647"]'

    submit = '//*[@id="form_7156f585-1060-4a2d-9bbb-3208433ebd56_container"]/div[3]/button'

    first_gsheets = 'Kyle'
    #driver.find_element_by_xpath(first_name).click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(first_name).send_keys(first_gsheets)
    driver.find_element_by_xpath(submit).click()
    driver.implicitly_wait(100)
    while (True):
        pass
    #driver.find_element_by_xpath(last_name).click()
    #driver.find_element_by_xpath(email).click()
    #driver.find_element_by_xpath(text_req).click()
    #driver.find_element_by_xpath(semester_start).click()
    #driver.find_element_by_xpath(program).click()
    #driver.find_element_by_xpath(questions).click()


openChrome()



