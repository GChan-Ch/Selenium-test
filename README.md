🧪 Automated UI Test: SauceDemo with Selenium & Pytest

This repository contains an automated UI test script for SauceDemo built using Selenium WebDriver, Pytest, and Headless Firefox.

The test simulates a full e-commerce user journey:

    Logging in as a standard user

    Adding multiple items to the cart

    Removing items from the cart

    Proceeding to checkout

    Completing the order

    Logging out from the session
    
🔧 Features

    ✔️ Headless browser execution (no popup window)

    ✔️ Detailed log output in terminal for each process step

    ✔️ Easily extendable for more test cases

    ✔️ Cross-platform (tested on Linux & Windows)

run test :
- pytest test_saucedemo.py -s -v

run test & save log output :
- pytest test_saucedemo.py -s -v > log.txt 2>&1

