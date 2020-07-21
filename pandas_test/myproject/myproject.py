import xlwings as xw
import pandas as pd
from selenium import webdriver
import time


def main():
    wb = xw.Book.caller()
    sample = toPandas(wb)
    
    if len(sample) == 0:
        print ("No new additions.")
    else:
        openChrome(sample)

def toPandas(fromExcel):
    try:
        index_df = pd.read_pickle("/Users/kylebeloin/Desktop/ua_undergrad/gsheets_project/gsheetsYuma/pandas_test/myproject/index.pkl")
    except:
        index_df = fromExcel.sheets[0].used_range.options(pd.DataFrame).value.dropna(how="all").reset_index()
        index_df.to_pickle("/Users/kylebeloin/Desktop/ua_undergrad/gsheets_project/gsheetsYuma/pandas_test/myproject/index.pkl")

    updated_df = fromExcel.sheets[0].used_range.options(pd.DataFrame).value.dropna(how="all").reset_index()
    merged_df = index_df.merge(updated_df, how="outer", indicator=True)
    toSelenium = merged_df.loc[merged_df['_merge'] == 'right_only'].iloc[:,:-1].to_dict('index')
    
    index_df.to_pickle("/Users/kylebeloin/Desktop/ua_undergrad/gsheets_project/gsheetsYuma/pandas_test/myproject/index_bkup.pkl")
    merged_df.iloc[:,:-1].to_pickle("/Users/kylebeloin/Desktop/ua_undergrad/gsheets_project/gsheetsYuma/pandas_test/myproject/index.pkl")
    
    return toSelenium

def openChrome(first):
    

    word = first[list(first.keys())[0]]['Last Name']



    chromedriver_location = "/Users/kylebeloin/Desktop/ua_undergrad/gsheets_project/gsheetsYuma/pandas_test/myproject/chromedriver" # Make sure the driver is in the same directory (or list the directory here.)
    driver = webdriver.Chrome(chromedriver_location)
    
    driver.get('https://yuma.arizona.edu/request-info') # Opens the webpage
    
    first_name = '//*[@id="form_913fa45e-b4ad-48d3-a26b-0e15918e3679"]' # These are xpath elements. 
    last_name = '//*[@id="form_647beaf1-ccb7-4511-8a94-8bdadab42987"]'
    email = '//*[@id="form_31880a0a-62ae-4e68-961b-a79cb7b53e76"]'
    text_req = '//*[@id="form_9d8df43b-f59f-4bb4-85b6-8a22247c7c34_1"]'
    semester_start = '//*[@id="form_7ab361b8-930e-497c-b012-75b88f84447d"]'
    program = '//*[@id="form_d88142c1-9660-4835-80f6-6c472d457eb9"]'
    questions = '//*[@id="form_51e0d29e-1078-4f6d-a62a-376e615f7647"]'

    submit = '//*[@id="form_7156f585-1060-4a2d-9bbb-3208433ebd56_container"]/div[3]/button'

     # Test value.
    #driver.find_element_by_xpath(first_name).click()
    
    driver.find_element_by_xpath(first_name).send_keys(word) # sends test vallue to text box element.
    driver.find_element_by_xpath(submit).click() # submit
    
    time.sleep(1000)

    driver.quit()
    #driver.find_element_by_xpath(last_name).click()
    #driver.find_element_by_xpath(email).click()
    #driver.find_element_by_xpath(text_req).click()
    #driver.find_element_by_xpath(semester_start).click()
    #driver.find_element_by_xpath(program).click()
    #driver.find_element_by_xpath(questions).click()
