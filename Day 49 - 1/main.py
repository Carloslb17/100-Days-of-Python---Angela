from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

EMAIL = 
PASSWORD = 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)


driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sing_up = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]').click()



email_box = driver.find_element(By.ID, 'username')
password_box = driver.find_element(By.XPATH, '//*[@id="password"]')



email_box.send_keys(EMAIL)
password_box.send_keys(PASSWORD)
sign_up_registration = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
