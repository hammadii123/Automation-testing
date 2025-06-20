import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Setup Chrome driver with Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Facebook
driver.get("https://web.facebook.com/")
# driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S2050321934%3A1748946930963212&ec=asw-gmail-globalnav-signin&flowEntry=AccountChooser&flowName=GlifWebSignIn&service=mail")


time.sleep(2)

# Optional: Close the driver after the delay
# driver.quit()

