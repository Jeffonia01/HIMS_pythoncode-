import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("Smart Hospital Automation Test")
def test_hospital_settings():
    driver = webdriver.Chrome()
    driver.get("http://3.111.115.65/demo/smart_hospital_src/site/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Helper function with Allure step
    @allure.step("Performing {action} on {locator}")
    def interact(by, locator, action="click", value=None):
        element = wait.until(EC.presence_of_element_located((by, locator)))
        if action == "click":
            element.click()
        elif action == "send_keys":
            element.clear()
            element.send_keys(value)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    # Login
    interact(By.NAME, "username", "send_keys", "test1@gmail.com")
    interact(By.NAME, "password", "send_keys", "Test@123")
    interact(By.XPATH, "//button[@type='submit']", "click")

    # Navigate to Hospital Settings
    interact(By.XPATH, "//span[text()='Setup']", "click")
    interact(By.XPATH, "//a[contains(@href, 'schsettings')]", "click")

    # Update Hospital Details
    details = {
        "sch_name": "New Hospital",
        "sch_dise_code": "HOS123",
        "sch_address": "123 Street",
        "sch_phone": "9876543210",
        "sch_email": "hospital@example.com"
    }
    for name, value in details.items():
        interact(By.NAME, name, "send_keys", value)

    # Save and Close
    interact(By.XPATH, "//button[contains(@class, 'submit_schsetting')]", "click")
    time.sleep(2)
    driver.quit()
