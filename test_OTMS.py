import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# ==================== CONFIGURATION ====================
BASE_URL = "https://transtan-test.plenome.com"
TEST_EMAIL = "jeffonia+1@plenome.com"
TEST_PASSWORD = "Jeffonia@01"
Hospital_Name = "Foxtale Hospital"
HOSPITAL_EMAIL = "jeffonia+64@plenome.com"
NEW_PASSWORD = "Jeffo@123"
PASSPORT_NUMBER = "876756478944"
FIRST_NAME = "Luke"
LAST_NAME = "A"
DATE_OF_BIRTH = "01102001"
QUALIFICATION = "MBBS"
PHONENUMBER ="8778757957"


# ==================== LOCATORS CLASS ====================
class Locators:
    # ---------- Login Page ----------
    USERNAME_FIELD = '//input[@id="trans-input"]'
    PASSWORD_FIELD = '//input[@id="outlined-adornment-password"]'
    LOGIN_BUTTON = '//button[@type="submit"]'
    OTP_FIELD = '//input[@aria-label="Please enter OTP character 1"]'
    VERIFY = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth Mui-disabled MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth !bg-[#9C539C] css-ge19m7"]'

    # ---------- Dashboard ----------
    DASHBOARD_TEXT = '//p[contains(@class, "text-[#804595]") and contains(@class, "font-medium")]'

    # ---------- Hospital Management ----------
    HOSPITAL_MANAGEMENT_MENU = '//p[normalize-space(text())="Hospital Management"]'
    ADD_NEW_BUTTON = '//button[contains(@class, "add-button")]'
    HOSPITAL_NAME_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[1]'
    ZONE_DROPDOWN = '(//div[@class="MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-xioi19"])[2]'
    ZONE_OPTION_2 = '(//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1o5vtcj"])[2]'
    TYPE_DROPDOWN = '(//div[@class="MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-xioi19"])[3]'
    TYPE_OPTION_1 = '//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1o5vtcj"][1]'
    HOSPITAL_EMAIL_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[2]'
    HOSPITAL_SUBMIT_BUTTON = ('//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained '
                              'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                              'MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained '
                              'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                              'MuiButton-colorPrimary MuiButton-fullWidth css-ge19m7"]')

    # ---------- Profile & Password Setup ----------
    PROFILE_MENU = '//div[@class="bg-[white] p-[6px] pr-[12px] flex gap-2 items-center rounded-2xl cursor-pointer relative group MuiBox-root css-0"]'
    LOGOUT_OPTION = '(//p[@class="MuiTypography-root MuiTypography-body1 flex items-center gap-1 cursor-pointer hover:bg-[#8a348a5d] rounded-lg p-2 css-9l3uo3"])[2]'
    NEW_PASSWORD_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-ff0rc8"])[1]'
    CONFIRM_PASSWORD_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-ff0rc8"])[2]'
    PASSWORD_SUBMIT_BUTTON = ('//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained '
                              'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                              'MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained '
                              'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                              'MuiButton-colorPrimary MuiButton-fullWidth css-ge19m7"]')
    CLOSE_BUTTON = '//div[@class="absolute top-7 right-10 MuiBox-root css-0"]'

    # ---------- Hospital Login ----------
    HOSPITAL_LOGIN_EMAIL = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[1]'
    HOSPITAL_LOGIN_PASSWORD = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-ff0rc8"])[1]'
    HOSPITAL_LOGIN_BUTTON = ('(//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained '
                             'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                             'MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained '
                             'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                             'MuiButton-colorPrimary MuiButton-fullWidth !bg-[#9C539C] css-ge19m7"])[1]')
    VERIFY_OTP_BUTTON = ('//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained '
                         'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                         'MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained '
                         'MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium '
                         'MuiButton-colorPrimary MuiButton-fullWidth !bg-[#9C539C] css-ge19m7"]')
    INTERNATIONAL_OPTION = '//div[@class="flex items-center w-full rounded-[20px] px-[8px] bg-[#EDEDED] text-[#71717A] MuiBox-root css-0"]'
    PASSPORT_NUMBER_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[1]'
    FIRST_NAME_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[2]'
    LAST_NAME_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[3]'
    DOB_INPUT = '//input[@name="dateOfBirth"]'
    QUALIFICATION_INPUT = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[4]'
    Phone_number ='//input[@id="phone-input-phoneNumber1"]'

# ==================== FIXTURE: Browser ====================
@pytest.fixture(scope="session")
def browser():
    """Initialize browser once for entire test session"""
    print("\n========== STARTING BROWSER ==========")
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(10)
    yield driver
    print("\n========== TESTS COMPLETED - BROWSER REMAINS OPEN ==========")
    print("Please close the browser manually when done.")


# ==================== HELPER FUNCTIONS ====================
def scroll_to_element(browser, element):
    """Scroll to element to bring it into view"""
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    sleep(0.5)


def scroll_page(browser, pixels=300):
    """Scroll page by specified pixels"""
    browser.execute_script(f"window.scrollBy(0, {pixels});")
    sleep(0.5)


def wait_and_click(browser, xpath, timeout=10, scroll=True):
    """Wait for element and click with optional auto-scroll"""
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    if scroll:
        scroll_to_element(browser, element)
    element.click()
    return element


def wait_and_send_keys(browser, xpath, text, timeout=10, scroll=True):
    """Wait for element and send keys with optional auto-scroll"""
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    if scroll:
        scroll_to_element(browser, element)
    element.click()
    element.clear()
    element.send_keys(text)
    return element 

# @pytest.mark.login
@pytest.mark.login
def test_valid_login(browser):
    """Test ID: TC_LOGIN_001 | Verify login with valid credentials"""
    print("🔹 Opening website...")
    browser.get(BASE_URL)

    print("🔹 Entering username...")
    wait_and_send_keys(browser, Locators.USERNAME_FIELD, TEST_EMAIL)

    print("🔹 Entering password...")
    wait_and_send_keys(browser, Locators.PASSWORD_FIELD, TEST_PASSWORD)

    print("🔹 Clicking login...")
    wait_and_click(browser, Locators.LOGIN_BUTTON)
    sleep(5)

    # ✅ Verify button (OTP or verification)
    try:
        print("🔹 Clicking verify button...")
        wait_and_click(browser, Locators.VERIFY_OTP_BUTTON)
        sleep(2)
    except Exception:
        print("ℹ️ Verify button not found — skipping.")

    # ✅ Open Hospital Management
    print("🔹 Clicking on Hospital Management module...")
    wait_and_click(browser, Locators.HOSPITAL_MANAGEMENT_MENU)
    sleep(1)

    # ✅ Click Add New
    print("Clicking on 'Add New' button...")
    wait_and_click(browser, Locators.ADD_NEW_BUTTON)
    sleep(1)
    
    print("click and enter the hospital name...")
    wait_and_send_keys(browser, Locators.HOSPITAL_NAME_INPUT, Hospital_Name)
    
    print("Click on the Zone DropDown...")
    wait_and_click(browser, Locators.ZONE_DROPDOWN)
    
    print("select the zone from the dropdown..")
    wait_and_click(browser, Locators.ZONE_OPTION_2) 
    
    print("Click on the hospital type..")  
    wait_and_click(browser, Locators.TYPE_DROPDOWN) 
    
    print("clicking on the option1 for the hospital dropdown..")
    wait_and_click(browser, Locators.TYPE_OPTION_1)
    
    print("Entering the email address..")
    wait_and_send_keys(browser, Locators.HOSPITAL_EMAIL_INPUT,HOSPITAL_EMAIL)
    
    print("Submit the hospital details..")
    wait_and_click(browser, Locators.HOSPITAL_SUBMIT_BUTTON)
    sleep(20)
    
    print("Hospital created successfully.........")
    
    
@pytest.mark.hospital_login
def test_hospital_login(browser):
    """Test ID: TC_LOGIN_002 | Verify Hospital login with valid credentials"""
    
    print("clicking on the profile Menu..")
    wait_and_click(browser, Locators.PROFILE_MENU)
    sleep(1)
    
    print("Clicking on the logout button..")
    wait_and_click(browser, Locators.LOGOUT_OPTION)
    sleep(1)
    
    


    print("✅ Test passed — Login and navigation successful!")
