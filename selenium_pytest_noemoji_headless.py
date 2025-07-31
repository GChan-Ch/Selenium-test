import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

class TestTest1():
    def setup_method(self, method):
        print("Memulai browser Firefox...")
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        #self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        print("Menutup browser...")
        self.driver.quit()

    def test_test1(self):
        print("Membuka halaman SauceDemo...")
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_window_size(550, 691)

        print("Melakukan login...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='username']").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='password']").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='login-button']").click()

        print("Menambahkan produk ke keranjang...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-bike-light']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-fleece-jacket']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-onesie']").click()
        try:
            self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
        except:
            print("Produk terakhir gagal ditambahkan (karena special character?)")

        print("Membuka halaman keranjang...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='shopping-cart-link']").click()

        print("Menghapus beberapa produk dari keranjang...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='remove-sauce-labs-backpack']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='remove-sauce-labs-bike-light']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='remove-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='remove-sauce-labs-onesie']").click()

        print("Melanjutkan belanja...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='continue-shopping']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-backpack']").click()

        print("Checkout...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='shopping-cart-link']").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='checkout']").click()

        print("Mengisi form informasi pembeli...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='firstName']").send_keys("udin")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='lastName']").send_keys("kid")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='postalCode']").send_keys("111")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='continue']").click()

        print("Menyelesaikan pembelian...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='finish']").click()

        print("Kembali ke halaman produk...")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='back-to-products']").click()

        print("Navigasi ke menu About dari sidebar...")
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test='about-sidebar-link']").click()
        self.driver.execute_script("window.scrollTo(0,252)")

        print("Test selesai dengan sukses!")

        self.driver.close()
