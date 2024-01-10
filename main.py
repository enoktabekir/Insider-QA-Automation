import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
url = "https://useinsider.com/"
companyLocator = "//a[contains(text(), 'Company')]"
careersLocator = "//a[contains(text(), 'Careers')]"
qa_jobsLocator = "//a[contains(text(), 'See all QA jobs')]"
locationLocator = ".select2-selection__arrow"


browser.get(url)
browser.maximize_window()

company = browser.find_element(By.XPATH, companyLocator)
company.click()
time.sleep(1)

careers = browser.find_element(By.XPATH, careersLocator)
careers.click()
time.sleep(2)

new_url = "https://useinsider.com/careers/quality-assurance/"
browser.get(new_url)
time.sleep(2)

qa_jobs = browser.find_element(By.XPATH, qa_jobsLocator)
qa_jobs.click()
time.sleep(5)

location = browser.find_element(By.CSS_SELECTOR, locationLocator)
location.click()
time.sleep(5)

