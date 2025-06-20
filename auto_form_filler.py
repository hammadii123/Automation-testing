import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(By.ID, "userName").send_keys("Hammad Mustafa")
driver.find_element(By.ID, "userEmail").send_keys("hammadworks123@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Nazimabad")
driver.find_element(By.ID, "permanentAddress").send_keys("As Mentioned")

submit = driver.find_element(By.XPATH, "//*[@id='submit']")
driver.execute_script("arguments[0].click()", submit)

time.sleep(5)
