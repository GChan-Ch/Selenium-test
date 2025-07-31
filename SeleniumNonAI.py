from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Buka website
driver.get("https://www.saucedemo.com/")

# 2. Input login info
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# 3. Klik tombol login
driver.find_element(By.ID, "login-button").click()

# Tunggu hingga halaman produk dimuat
wait = WebDriverWait(driver, 10)

try:
    inventory = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("✅ Login berhasil!")
except:
    print("❌ Login gagal.")

# 4. Cek elemen UI setelah login
print("\n🔍 Verifikasi UI setelah login:")

# a. Cek logo/header
try:
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    print("✅ Logo ditemukan:", logo.text)
except:
    print("❌ Logo tidak ditemukan.")

# b. Cek dropdown filter produk
try:
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    print("✅ Dropdown filter produk ditemukan.")
except:
    print("❌ Dropdown filter produk tidak ditemukan.")

# c. Cek tombol menu (sidebar)
try:
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    logout_link = wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
    print("✅ Tombol logout tersedia di sidebar.")
except:
    print("❌ Tombol logout tidak ditemukan.")

# d. Cek jumlah produk yang ditampilkan
try:
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"✅ Jumlah produk yang ditampilkan: {len(products)} item.")
except:
    print("❌ Tidak bisa mengambil daftar produk.")

# e. (Opsional) Screenshot
driver.save_screenshot("saucedemo_dashboard.png")
print("📸 Screenshot halaman disimpan sebagai 'saucedemo_dashboard.png'")

# 5. Tutup browser
driver.quit()
