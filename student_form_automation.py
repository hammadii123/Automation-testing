import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID, "firstName").clear()
driver.find_element(By.ID, "firstName").send_keys("Hammad")
driver.find_element(By.ID, "lastName").clear()
driver.find_element(By.ID, "lastName").send_keys("Mustafa")
driver.find_element(By.XPATH, "//*[@id='userEmail']").clear()
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys("hammadworks123@gmail.com")
driver.find_element(By.XPATH, "//label[@for='gender-radio-2']").click()
driver.find_element(By.ID, "userNumber").clear()
driver.find_element(By.ID, "userNumber").send_keys("03043378880")
dd = driver.find_element(By.ID, "dateOfBirthInput")
driver.execute_script("arguments[0].click()", dd)
driver.find_element(By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[11]").click()
driver.find_element(By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[85]").click()
driver.find_element(By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[3]").click()
driver.find_element(By.ID, "subjectsInput").send_keys("ENGLISH")
driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
hobbies = driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[2]/label")
driver.execute_script("arguments[0].click()", hobbies)
driver.find_element(By.ID, "uploadPicture").send_keys("C:/Users/SAM/Desktop/SAM.jpeg")
driver.find_element(By.ID, "currentAddress").send_keys("Nazimabad")
time.sleep(10)
select = driver.find_element(By.XPATH, "//*[@id='stateCity-label']")
driver.execute_script("arguments[0].click()", select)
Dropdown = driver.find_element(By.XPATH, "//*[@id='state']/div/div[1]/div[1]")
driver.execute_script("arguments[0].click()", Dropdown)
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click()", submit)
time.sleep(15)