# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
 
 
# # ---------- Chrome Options ----------
# chrome_options = Options()
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--no-default-browser-check")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-plugins-discovery")
# chrome_options.add_argument("--incognito")  # Temporary session
# chrome_options.add_argument("--start-maximized")
 
# # Disable password manager
# prefs = {
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False,
#     "profile.default_content_setting_values.notifications": 2
# }
# chrome_options.add_experimental_option("prefs", prefs)
 
 
# # ---------- Pytest Fixture ----------
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
 
 
# # ---------- Login Function ----------
# def perform_login(driver, url, username, password):
#     driver.get(url)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
 
#     driver.find_element(By.NAME, "username").send_keys(username)
#     sleep(1)
#     driver.find_element(By.NAME, "password").send_keys(password)
#     sleep(1)
#     driver.find_element(By.XPATH, '//button[text()="Sign In"]').click()
#     sleep(3)

    
    
    
# def perform_Genral_settings(driver, url_1, username_1, passwor_1):
#     driver.get(url)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
 
#     driver.find_element(By.NAME, "username").send_keys(username)
#     sleep(1)
#     driver.find_element(By.NAME, "password").send_keys(password)
#     sleep(1)
#     driver.find_element(By.XPATH, '//button[text()="Sign In"]').click()
#     sleep(3)
#     driver.find_element(By.XPATH, '//a[@href="https://qa-hms.plenome.com/"]/span[text()="Master Setup"]').click()
#     sleep(3)
#     driver.find_element(By.XPATH, '//a[@href="https://qa-hms.plenome.com/schsettings"]').click()
#     sleep(3) 
#     driver.find_element(By.XPATH, '//input[@name="sch_name"]').clear()
#     sleep(3)
#     driver.find_element(By.XPATH, '//input[@name="sch_name"]').send_keys("Tile hospital")
#     sleep(2) 
#     driver.find_element(By.XPATH, '//input[@name="sch_dise_code"]').send_keys("TI23412")
#     sleep(2)

 
 
# # ---------- Test Case ----------
# def test_login_QA(browser):
#     url = "https://qa-hms.plenome.com/site/login"
#     username = "testing@plenome.com"
#     password = "Test@1234"
#     print(" Testing login functionality on QA Server...")
#     perform_login(browser, url, username, password)
#     print("✅ Login successful on QA Server.")
    
    
# def test_Mastersetup(browser):
#     url_1 = "https://qa-hms.plenome.com/site/login"
#     username_1 = "testing@plenome.com"
#     password_1 = "Test@1234"
#     print(" Testing login functionality on QA Server...")
#     perform_Genral_settings(browser, url_1, username_1, passwor_1)
#     print("✅ Login successful on QA Server.")
    
    
    
    
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------- Fixture ----------
@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()

    # Disable automation banner
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Disable password manager & popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Run in incognito & maximized
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()


# ---------- Test ----------
def test_master_setup(browser):
    url = "https://qa-hms.plenome.com/site/login"
    username = "testing@plenome.com"
    password = "Test@1234"

    # ---------- Helper function ----------
    def fill_input(by, locator, value):
        """Wait for element, clear it, and enter value."""
        elem = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((by, locator))
        )
        elem.clear()
        elem.send_keys(value)

    # ---------- Login ----------
    browser.get(url)
    fill_input(By.NAME, "username", username)
    fill_input(By.NAME, "password", password)
    browser.find_element(By.XPATH, '//button[text()="Sign In"]').click()

    # Wait for dashboard page
    WebDriverWait(browser, 15).until(EC.url_contains("dashboard"))

    # ---------- Navigate to Master Setup → Settings ----------
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Master Setup")]'))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "schsettings")]'))
    ).click()

    # ---------- Update Settings ----------
    fill_input(By.NAME, "sch_name", "Tile hospital")
    fill_input(By.NAME, "sch_dise_code", "TI23412")
    fill_input(By.NAME, "sch_phone", "78765643567")
    fill_input(By.NAME, "sch_email", "ajeffonia0121@gmail.com")
    fill_input(By.XPATH, '//*[@id="district"]', "Vellore")
    fill_input(By.XPATH, '//*[@id="pin_code"]', "632009")
    fill_input(By.NAME, "sch_address","Chennai1")
    fill_input(By.XPATH, '//*[@id="hospital_timing_from"]', "09:00")
    fill_input(By.XPATH, '//*[@id="hospital_timing_to"]', "23:00")
    time.sleep(5)
    
    


          
          
          
          
          
          


 
 