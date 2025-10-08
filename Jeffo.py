import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------- Fixture for pytest ----------
@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# ---------- Helper function ----------
def jeffonia(driver, by, locator, action, value=None, offset=-100):
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator)))
    driver.execute_script("""
        const element = arguments[0];
        const offset = arguments[1];
        const bodyRect = document.body.getBoundingClientRect().top;
        const elemRect = element.getBoundingClientRect().top;
        const scrollTop = elemRect - bodyRect + offset;
        window.scrollTo({top: scrollTop, behavior: 'smooth'});
    """, elem, offset)
    time.sleep(0.3)

    if action == "send_keys":
        elem.clear()
        elem.send_keys(value)
    elif action == "click":
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, locator)))
        elem.click()
    elif action == "upload_file":
        elem.send_keys(value)
    else:
        raise ValueError(f"Unsupported action: {action}")

    return elem

# ---------- Core test logic ----------
def run_master_setup(driver):
    url = "https://qa-hms.plenome.com/site/login"
    username = "testing@plenome.com"
    password = "Test@1234"

    driver.get(url)
    jeffonia(driver, By.NAME, "username", "send_keys", username)
    jeffonia(driver, By.NAME, "password", "send_keys", password)
    jeffonia(driver, By.XPATH, '//button[text()="Sign In"]', "click")
    WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))

    # Navigate to Master Setup → Settings
    jeffonia(driver, By.XPATH, '//span[contains(text(), "Master Setup")]', "click")
    jeffonia(driver, By.XPATH, '//a[contains(@href, "schsettings")]', "click")

    # Fill the form
    jeffonia(driver, By.NAME, "sch_name", "send_keys", "Jeffo hospital")
    jeffonia(driver, By.NAME, "sch_dise_code", "send_keys", "JE23412")
    jeffonia(driver, By.NAME, "sch_phone", "send_keys", "7876563567")
    jeffonia(driver, By.NAME, "sch_email", "send_keys", "ajeffonia0121@gmail.com")
    jeffonia(driver, By.XPATH, '//*[@id="district"]', "send_keys", "Vellore")
    jeffonia(driver, By.XPATH, '//*[@id="pin_code"]', "send_keys", "632009")
    jeffonia(driver, By.NAME, "sch_address", "send_keys", "Chennai1")
    jeffonia(driver, By.XPATH, '//*[@id="hospital_timing_from"]', "send_keys", "09:00")
    jeffonia(driver, By.XPATH, '//*[@id="hospital_timing_to"]', "send_keys", "23:00")
    time.sleep(1)

    # Upload Hospital Logo
    driver.find_element(By.CLASS_NAME, "upload_logo").click()
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(r"C:\Users\ADMIN\OneDrive\Desktop\Doctor.jpg")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cropButton"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class, "submit_schsetting") and contains(@class, "edit_setting")]').click()
    time.sleep(1)
    print("Hospital logo uploaded ✅")

def setup_Humanresource(driver):
    # Navigate to leave types
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/leavetypes"]', "click")
    
    # # Navigate to payroll setup type
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/admin/payroll_setup_type"]', "click")
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/admin/payroll_setup"]', "click")
    # jeffonia(driver, By.XPATH, '//div[@class="box-tools pull-right"]/a[@class="btn btn-primary btn-sm payroll"]',"click")    
    # jeffonia(driver, By.XPATH, '//*[@id="payroll_type"]', "click")
    # jeffonia(driver, By.XPATH, '//select[@id="payroll_type"]//option[@value="19" and normalize-space(text())="Earning"]', "click")
    # time.sleep(2)    
    # jeffonia(driver, By.XPATH, "//label[text()='Payroll Name']/following::input[@id='name']", "send_keys", "Insurance")
    # jeffonia(driver, By.XPATH, "//label[text()='Percentage']/following::input[@id='percentage']", "send_keys", "10")
    # jeffonia(driver, By.XPATH, '//button[@class="btn btn-info pull-right" and normalize-space(text())="Save"]', "click")
    # time.sleep(10)
    
    # # Navigate to specialist 
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/specialist"]', "click")
    # jeffonia(driver, By.XPATH, "//a[@data-target='#myModal']", "click")
    # jeffonia(driver, By.XPATH, "//input[@id='type']", "send_keys", "paediatric")
    # jeffonia(driver, By.XPATH, "//button[@id='formaddbtn']", "click")
    # time.sleep(3)
    
    # # Navigate to department 
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/department"]', "click")
    # jeffonia(driver, By.XPATH,'//a[@class="btn btn-primary btn-sm department"]', "click")
    # jeffonia(driver, By.XPATH,'//input[@id="type"and  @class="form-control"]',"send_keys","Inpatient")
    # jeffonia(driver, By.XPATH,'//button[@id="formaddbtn"and  @class="btn btn-info pull-right"]',"click")
    # time.sleep(2)
    
    # Navigate to designation 
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/designation/designation"]', "click")
    # jeffonia(driver, By.XPATH, '//a[@class="btn btn-primary btn-sm designation"]', "click")
    # jeffonia(driver, By.XPATH, '//input[@id="type" and @class="form-control"]', "send_keys","surgeon")
    # jeffonia(driver, By.XPATH, '//button[@type="submit" and @class="btn btn-info pull-right"]', "click")
    # time.sleep(2)    
    
    
    # Navigate to department 
    # jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/department"]',"click")
    # jeffonia(driver, By.XPATH, '//a[@class="btn btn-primary btn-sm department"]',"click")
    # jeffonia(driver, By.XPATH, '//input[@id="type"  and @class="form-control"]', "send_keys","testing")
    # jeffonia(driver, By.XPATH, '//button[@type="submit" and @class="btn btn-info pull-right"]', "click")
    # time.sleep(2)
     
     
    # Navigate to leave type  
    jeffonia(driver, By.XPATH, '//a[@href="https://qa-hms.plenome.com/admin/leavetypes"]',"click")
    jeffonia(driver, By.XPATH, '//a[@class="btn btn-primary btn-sm leavetype"]',"click")
    jeffonia(driver, By.XPATH, '//input[@name="type"  and @class="form-control"]', "send_keys","testing")
    jeffonia(driver, By.XPATH, '//button[@type="submit" and @class="btn btn-info pull-right"]', "click")
    time.sleep(2)
    
    
    

    
    
    

    
    
            
# ---------- pytest test ----------
def test_master_setup(browser):
    run_master_setup(browser)
    setup_Humanresource(browser)

# ---------- Manual runner ----------
if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        run_master_setup(driver)
        setup_Humanresource(driver)
    finally:
        time.sleep(5)
        

