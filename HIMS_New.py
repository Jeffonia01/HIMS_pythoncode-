import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------- Setup Chrome ----------
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
options.add_argument("--incognito")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # ---------- Open site and login ----------
    driver.get("https://qa-hms.plenome.com/site/login")
    driver.find_element(By.NAME, "username").send_keys("testing@plenome.com")
    driver.find_element(By.NAME, "password").send_keys("Test@1234")
    driver.find_element(By.XPATH, '//button[text()="Sign In"]').click()
    WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))

    # ---------- Navigate to Master Setup → Settings ----------
    driver.find_element(By.XPATH, '//span[contains(text(), "Master Setup")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "schsettings")]').click()

    # ---------- Fill the form ----------
    driver.find_element(By.NAME, "sch_name").clear()
    driver.find_element(By.NAME, "sch_name").send_keys("Tile hospital")

    driver.find_element(By.NAME, "sch_dise_code").clear()
    driver.find_element(By.NAME, "sch_dise_code").send_keys("TI23412")

    driver.find_element(By.NAME, "sch_phone").clear()
    driver.find_element(By.NAME, "sch_phone").send_keys("7876563567")

    driver.find_element(By.NAME, "sch_email").clear()
    driver.find_element(By.NAME, "sch_email").send_keys("ajeffonia0121@gmail.com")

    driver.find_element(By.XPATH, '//*[@id="district"]').clear()
    driver.find_element(By.XPATH, '//*[@id="district"]').send_keys("Vellore")

    driver.find_element(By.XPATH, '//*[@id="pin_code"]').clear()
    driver.find_element(By.XPATH, '//*[@id="pin_code"]').send_keys("632009")

    driver.find_element(By.NAME, "sch_address").clear()
    driver.find_element(By.NAME, "sch_address").send_keys("Chennai1")

    driver.find_element(By.XPATH, '//*[@id="hospital_timing_from"]').clear()
    driver.find_element(By.XPATH, '//*[@id="hospital_timing_from"]').send_keys("09:00")

    driver.find_element(By.XPATH, '//*[@id="hospital_timing_to"]').clear()
    driver.find_element(By.XPATH, '//*[@id="hospital_timing_to"]').send_keys("23:00")

    time.sleep(1)


    # ---------- Upload Hospital Logo ----------
    driver.find_element(By.CLASS_NAME, "upload_logo").click()
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(r"C:\Users\ADMIN\OneDrive\Desktop\Doctor.jpg")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cropButton"))).click()
    time.sleep(1)

    # ---------- Save changes ----------
    driver.find_element(By.XPATH, '//button[contains(@class, "submit_schsetting") and contains(@class, "edit_setting")]').click()
    time.sleep(2)

    print("Hospital logo uploaded ✅")

finally:
    driver.quit()
