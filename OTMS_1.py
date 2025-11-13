import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# ---------- Pytest Fixture ----------
@pytest.fixture(scope="module")
def driver():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
   
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)
   
    # Initialize the driver
    service = Service(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service, options=chrome_options)
   
    yield web_driver
    print("\n--- Closing WebDriver ---")
    web_driver.quit()


# ---------- Data & Locators ----------
class Data:
    username = "jeffonia+1@plenome.com"
    password = "Jeffonia@01"
    url = "https://transtan-test.plenome.com/login"


class Locators:
    username_locator = '//input[@id="trans-input"]'
    password_locator = '//input[@id="outlined-adornment-password"]'
    submit_button = '//button[@type="submit"]'
    transtan_dashboard ='//p[@class="MuiTypography-root MuiTypography-body1 !text-[14px] xl-custom:!text-[16px] text-nowrap text-[#804595] !font-medium css-9l3uo3"]'
    otpfield_click = '//input[@aria-label="Please enter OTP character 1"]'
    verify_button = '//button[@type="submit"]'
    Hospital_module = '//p[@class="MuiTypography-root MuiTypography-body1 !text-[14px] xl-custom:!text-[16px] text-nowrap text-[#804595] !font-medium css-9l3uo3" and normalize-space(text()) ="Hospital Management"]'
    Addnew_hospital ='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary flex gap-x-3 w-full textResponse add-button !p-1.55 shadow-none !rounded-[4px] css-1dnslar"]'
    Hospital_name ='(//div[@class="MuiFormControl-root MuiFormControl-fullWidth css-tzsjye"])[1]'
    Hospital_name_data = '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[1]'
    clickZone_dropdown ='(//div[@class="MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-xioi19"])[2]'
    select_zone='(//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1o5vtcj"])[2]'
    Hospitaltype_dropdown='(//div[@class="MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-xioi19"])[3]'
    Hospitaltype_select='//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1o5vtcj"][1]'
    Email_click='(//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-sizeSmall css-11luafn"])[2]'
    emailinput='(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1oirvji"])[2]'
    hosp_sendemail='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth css-ge19m7"]'
    New_password= '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-ff0rc8"])[1]'
    Confirm_password= '(//input[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-ff0rc8"])[2]'
    Click_login='//div[@class="bg-[white] p-[6px] pr-[12px] flex gap-2 items-center rounded-2xl cursor-pointer relative group MuiBox-root css-0"]'
    Log_out='(//p[@class="MuiTypography-root MuiTypography-body1 flex items-center gap-1 cursor-pointer hover:bg-[#8a348a5d] rounded-lg p-2 css-9l3uo3"])[2]'
    Sub_mit='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth css-ge19m7"]'
    
    
    
# ---------- Test Class ----------
class TestHospitalSetup:
    data = Data
    locators = Locators

    def log_step(self, step_number, description):
        """Prints a formatted log message for test reporting."""
        print(f"\n--- STEP {step_number}: {description} ---")

    
    def test_01_user_login(self, driver):
        """TC_001: User Login - Explicit Selenium calls with logging."""
        self.log_step("1.1", "Navigating to Transtan Login URL.")
        driver.get(self.data.url)
        driver.maximize_window()
        sleep(3)

        self.log_step("1.2", "Entering Username.")
        driver.find_element(By.XPATH, self.locators.username_locator).send_keys(self.data.username)

        self.log_step("1.3", "Entering Password.")
        driver.find_element(By.XPATH, self.locators.password_locator).send_keys(self.data.password)
        sleep(2)

        self.log_step("1.4", "Clicking 'Sign In' button.")
        driver.find_element(By.XPATH, self.locators.submit_button).click()

        sleep(4)
        
        self.log_step("1.5", "Entering OTP and verifying by clicking submit.")
        driver.find_element(By.XPATH, self.locators.otpfield_click).click()
        sleep(20)
        driver.find_element(By.XPATH, self.locators.verify_button).click()
        sleep(1)

        self.log_step("1.6", "Verifying successful login by checking for 'Transtan Dashboard' page.")
        setup_menu = driver.find_element(By.XPATH, self.locators.transtan_dashboard )
        assert setup_menu.is_displayed(), "Login failed: Setup menu not found."
        print("Verification Successful: Transtan dashboard is visible.")

    # @pytest.mark.patient_flow
    def test_07_appointment_and_payment(self, driver):
        """TC_02: .Onboard a new Governement Hospital"""
        try:
            self.log_step("2.1", "Onboarding a Hospital(Government).")
            driver.find_element(By.XPATH, self.locators.Hospital_module).click()
            sleep(2)
            # self.log_step("2.2", "Onboarding a Hospital, clicking on add new button.")
            driver.find_element(By.XPATH, self.locators.Addnew_hospital).click()
            sleep(2)
            # print("It should click on the add new button hospital.")
            driver.find_element(By.XPATH, self.locators.Hospital_name).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Hospital_name_data).send_keys("switch Hospital")
            sleep(2)
            driver.find_element(By.XPATH, self.locators.clickZone_dropdown).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.select_zone).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Hospitaltype_dropdown).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Hospitaltype_select).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Email_click).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.emailinput).send_keys("jeffonia+25@plenome.com")
            sleep(2)
            driver.find_element(By.XPATH, self.locators.hosp_sendemail).click()
            sleep(30)
            
            self.log_step("2.1", "Login to the hospiatl).")
            driver.find_element(By.XPATH, self.locators.Click_login).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Log_out).click()
            sleep(2)
            driver.find_element(By.XPATH, self.locators.New_password).send_keys("Jeffo@123")
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Confirm_password).send_keys("Jeffo@123")
            sleep(2)
            driver.find_element(By.XPATH, self.locators.Sub_mit).click()
            sleep(3)
            
            

        except Exception as error:
            print("ERROR during Appointment and Payment Flow (TC_07): ", error)
            raise  # Re-raise the exception to fail the test correctly
