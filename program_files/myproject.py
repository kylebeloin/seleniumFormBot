import xlwings as xw
import pandas as pd
from selenium import webdriver
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

working_directory = os.getcwd()


def main():
    book = xw.Book.caller()
    new_entries_dict = toPandas(book)
    
    if len(new_entries_dict) == 0:
        Exception ("No new additions.")
    else:
        openChrome(new_entries_dict)

def toPandas(fromExcel):
    try:
        index_df = pd.read_pickle(working_directory + '/cache/index.pkl')
    except:
        index_df = fromExcel.sheets[0].used_range.options(pd.DataFrame).value.dropna(how="all").reset_index()
        index_df.to_pickle(working_directory + '/cache/index.pkl')

    updated_df = fromExcel.sheets[0].used_range.options(pd.DataFrame).value.dropna(how="all").reset_index()
    merged_df = index_df.merge(updated_df, how="outer", indicator=True)
    toSelenium = merged_df.loc[merged_df['_merge'] == 'right_only'].iloc[:,:-1].to_dict('index')
    
    index_df.to_pickle(working_directory + '/cache/bkup_index.pkl')
    merged_df.iloc[:,:-1].to_pickle(working_directory + '/cache/index.pkl')
    
    return toSelenium

def openChrome(new_entries_dict):
    webpage_dict = {
    'first_name': '//*[@id="form_913fa45e-b4ad-48d3-a26b-0e15918e3679"]',
    'last_name': '//*[@id="form_647beaf1-ccb7-4511-8a94-8bdadab42987"]',
    'email': '//*[@id="form_31880a0a-62ae-4e68-961b-a79cb7b53e76"]',
    'phone': '//*[@id="form_4d1766f7-7f38-4a86-8b7f-194ee76dd7ad"]',
    'semester': '//*[@id="form_7ab361b8-930e-497c-b012-75b88f84447d"]',
    'program': '//*[@id="form_d88142c1-9660-4835-80f6-6c472d457eb9"]',
        }
    
    # submit = '//*[@id="form_7156f585-1060-4a2d-9bbb-3208433ebd56_container"]/div[3]/button'


    chromedriver_location = working_directory + "/chromedriver" # Make sure the driver is in the same directory (or list the directory here.)
    driver = webdriver.Chrome(chromedriver_location)

    for entry in new_entries_dict:
        driver.get('https://yuma.arizona.edu/request-info')
        for key in list(webpage_dict.keys()):
            driver.find_element_by_xpath(webpage_dict[key]).send_keys(new_entries_dict[entry][key]) # sends test vallue to text box element.
        time.sleep(3)
        driver
        #driver.find_element_by_xpath(submit).click()
    driver.quit()

    