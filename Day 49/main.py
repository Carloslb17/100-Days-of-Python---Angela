from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3487303944&keywords=a")
job_search = driver.find_element(By.ID, 'jobs-search-box-keyword-id-ember1939')


