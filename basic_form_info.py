import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the webpage
driver.get("https://demoqa.com/text-box")  # Corrected URL spelling
# Maximize the browser window
driver.maximize_window()

driver.find_element(By.ID, "userName").send_keys("Hammad Mustafa")

# Print the title and URL of the page
print(driver.title)
print(driver.current_url)

time.sleep(2)

# Pause execution for 2 seconds

