from selenium import webdriver

chromedriver_location = "./chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.instagram.com/')

