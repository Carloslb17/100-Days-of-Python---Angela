from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(By.ID, 'cookie')

cursor_button = driver.find_element(By.ID, 'buyCursor')

cursor_price_text = driver.find_element(By.CSS_SELECTOR, '#store b')
print(cursor_price_text.text)

grandma_button = driver.find_element(By.ID, 'buyGrandma')
factory_button = driver.find_element(By.ID, 'buyFactory')
count = 0


while True:
    time.sleep(0.05)
    cookie_button.click()

    #Refresh price button
    #price_button = int(driver.find_element(By.ID, 'money').text)

    #print(cursor_price_text)
    #grandma_price_text = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split('-')
    #factory_price_text = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split('-')

    #if price_button > int(factory_price_text[1]):
     #   factory_button.click()
    #elif price_button > int(grandma_price_text[1]):
     #   grandma_button.click()
    #if price_button > int(cursor_price_text[1]):
        #cursor_button.click()



