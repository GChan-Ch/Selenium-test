from selenium import webdriver
from applitools.selenium import Eyes, Target
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Eyes
eyes = Eyes()
eyes.api_key = "YOUR_APPLITOOLS_API_KEY"

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Mulai test visual
    eyes.open(driver, app_name="SauceDemo", test_name="Login Visual Test")

    # 1. Buka halaman
    driver.get("https://www.saucedemo.com/")

    # 2. Visual check halaman login
    eyes.check("Login Page", Target.window())

    # 3. Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 4. Visual check halaman inventory
    eyes.check("Inventory Page", Target.window())

    # Selesai
    eyes.close()

finally:
    driver.quit()
    eyes.abort_if_not_closed()
