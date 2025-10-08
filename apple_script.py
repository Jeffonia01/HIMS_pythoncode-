import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# print("Script is running")



@allure.title("Smart Hospital Automation Test")
def test_hospital_settings():
    driver = webdriver.Chrome()
    driver.get("https://qa-hms.plenome.com/site/login")
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
        elif action == "scroll":
            scroll(element)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Scrolling to element: {element}")
    def scroll(element):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    # Login
    interact(By.NAME, "username", "send_keys", "testing@plenome.com")
    interact(By.NAME, "password", "send_keys", "Test@1234")
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
        interact(By.NAME, name, "send_keys",value)
        print("details")

# Save and Close
    interact(By.XPATH, "//button[contains(@class, 'submit_schsetting')]", "click")
    time.sleep(2)
    print("✅ General settimng did successfully")

# Scroll Down to 'Setup' element
    interact(By.XPATH, "//a[contains(@href,'http://3.111.115.65/php-hms-frontend/')]/span[text()='Setup']", "scroll")
    time.sleep(2)
    print("✅Scroll function done successfully")
    
    
    # interact(By.XPATH, '//a[@class="btn btn-primary btn-sm leavetype"]', "click")
    # interact(By.XPATH, '//input[@name="type"]', "send_keys", "Sick leave")
    # interact(By.XPATH, '//button[@class="btn btn-info pull-right"]', "click")
    # print("✅ Leave type added successfully")
    # time.sleep(3)
    

#set--> Human resources, specialist
    interact(By.XPATH, '//a[@href="http://3.111.115.65/php-hms-frontend/admin/leavetypes"]', "click")  
    interact(By.XPATH, '//a[@class="btn btn-primary btn-sm leavetype"]', "click")
    interact(By.XPATH, '//input[@name="type"]', "send_keys", "Sick")
    interact(By.XPATH, '//button[@class="btn btn-info pull-right"]', "click")
    print("✅ Leave type added successfully")
    time.sleep(5)   
    
# Add specilization 
    interact(By.XPATH, '//a[@href="http://3.111.115.65/php-hms-frontend/admin/specialist"]', "click")
    interact(By.XPATH, '//a[@class="btn btn-primary btn-sm specialist"]', "click")
    interact(By.XPATH, '//input[@name="type"]', "send_keys","surgen")
#save the specilization
    interact(By.XPATH, '//button[@class="btn btn-info pull-right"]', "click")
    print("✅specialization updated successfully!!")
    time.sleep(5)
    
#set--> Human resources, designation
    interact(By.XPATH, '//a[@href="http://3.111.115.65/php-hms-frontend/admin/designation/designation"]', "click")
    interact(By.XPATH, '//a[@class="btn btn-primary btn-sm designation"]', "click")
    interact(By.XPATH, '//input[@name="type"]', "send_keys","Dentist")
    interact(By.XPATH, '//button[@class="btn btn-info pull-right"]', "click")
    print("✅ designation added successfully")
    time.sleep(5)
    
    
    # #set--> Human resources, department
    interact(By.XPATH, '//a[@href="http://3.111.115.65/php-hms-frontend/admin/department"]', "click")
    interact(By.XPATH, '//a[@class="btn btn-primary btn-sm department"]', "click")
    time.sleep(3)
    interact(By.XPATH, '//input[@name="type"]', "send_keys","Surgery")
    interact(By.XPATH, '//button[@class="btn btn-info pull-right"]', "click")
    print("✅ Department added successfully")
    time.sleep(5)
    
#Human resources
    interact(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/staff"]/span[text()="Human Resource"]', "click")
    interact(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/staff/create"]', "click")
    time.sleep(3)
    interact(By.XPATH, '//input[@name="name"]', "send_keys","Venkataa")
    interact(By.XPATH, '//input[@name="surname"]', "send_keys","Ramanan")
    interact(By.XPATH, '//input[@name="father_name"]', "send_keys","venky father")
    interact(By.XPATH, '//input[@name="mother_name"]', "send_keys","venky mother")
    time.sleep(5)
    interact(By.XPATH, '//select[@name="gender"]', "click")
    interact(By.XPATH, '//option[@value="Male"]', "click")
    time.sleep(2)
    
    
    
    interact(By.XPATH, '//button[normalize-space(text())="Select Languages"]', "click") 
    interact(By.XPATH, '//input[@type="checkbox" and @title="Azerbaijan"]', "click")
    print("✅Language selected succesfully")
    
    
    interact(By.XPATH, '//select[@name="role"]', "click")
    time.sleep(2)
    interact(By.XPATH, '//option[normalize-space(text())="Doctor"]', "click")
    interact(By.XPATH, '//select[@name="designation"]',"click")
    interact(By.XPATH, '//select[@name="gender"]', "click")
    interact(By.XPATH, '//option[@value="Male"]', "click")
    interact(By.XPATH, '//select[@name="marital_status"]', "click")
    interact(By.XPATH, '//option[@value="Single"]', "click")
    time.sleep(3)
    interact(By.XPATH, '//select[@name="blood_group"]', "click")
    interact(By.XPATH, '//option[@value="1" and normalize-space(text())="O+"]', "click")
    interact(By.XPATH, '//input[@name="dob"]', "send_keys","14-11-2000")
    interact(By.XPATH, '//input[@name="Password"]',"click")
    interact(By.XPATH, '//input[@name="Password"]',"send_keys","Venkat@123")
    print("✅ Stafff added successfully")
    time.sleep(3)
    
    
    @allure.step("Performing {action} on {locator}")
    def jeffonia(by, locator, action="click", value=None):
        element = wait.until(EC.presence_of_element_located((by, locator)))
        if action == "click":
            element.click()
        elif action == "send_keys":
            element.clear()
            element.send_keys(value)
        elif action == "scroll":
            scroll(element)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

        @allure.step("Scrolling to element: {element}")
        def scroll(element):
         driver.execute_script("arguments[0].scrollIntoView(true);", element)
         time.sleep(0.5)
    
    jeffonia(By.XPATH, '//select[@id="designation"]',"click")
    jeffonia(By.XPATH, '//option[@value="18" and normalize-space(text())="Vascular Surgeon"]', "click")
    jeffonia(By.XPATH, '//select[@name="department"]',"click")
    jeffonia(By.XPATH, '//option[@value="9" and normalize-space(text())="Neurology"]',"click")
    
    jeffonia(By.XPATH, '//button[normalize-space(text())="Select Specialist"]',"click")
    jeffonia(By.XPATH, '//input[@type="checkbox" and @id="ms-opt-1"]',"click")
    jeffonia(By.XPATH, '//input[@id="date_of_joining"]',"send_keys","14-11-2025")
    jeffonia(By.XPATH, '//input[@id="mobileno"]',"click")
    jeffonia(By.XPATH, '//input[@id="mobileno"]',"send_keys","8778728956")
    
    jeffonia(By.XPATH, '//input[@id="emgmobileno"]',"send_keys","8778728957")
    jeffonia(By.XPATH, '//input[@id="email"]',"send_keys","ajeffoi4@gmail.com")
    jeffonia(By.XPATH, '//textarea[@name="address"]',"click")
    print("✅Staff is updated till Email")
    
    jeffonia(By.XPATH, '//textarea[@name="permanent_address"]',"send_keys","chennai")
    jeffonia(By.XPATH, '//textarea[@id="qualification"]',"click")
    jeffonia(By.XPATH, '//textarea[@name="specialization"]',"click")
    jeffonia(By.XPATH, '//textarea[@name="note"]',"send_keys","nothing to write here")
    
    jeffonia(By.XPATH,'//textarea[@id="qualification"]',"send_keys","BE, cse")
    jeffonia(By.XPATH,'//button[@class="btn btn-info pull-right"]',"click")
    print("✅Saved succuessfully")
    
@allure.step("Performing {action} on {locator}")
def Add_staff(by, locator, action="click", value=None):
    element = wait.until(EC.presence_of_element_located((by, locator)))
    if action == "click":
        element.click()
    elif action == "send_keys":
        element.clear()
        element.send_keys(value)
    elif action == "scroll":
        scroll(element)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.step("Scrolling to element: {element}")
def scroll(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)
        
    Add_staff(By.XPATH, '//a[@href="http://3.111.115.65/php-hms-frontend/admin/staff/create"]', "click") 
    Add_staff(By.XPATH,'//input[@name="name"]',"send_keys","Jeffo")     
    Add_staff(By.XPATH,'//input[@name="surname"]',"send_keys","A")
    Add_staff(By.XPATH, '//input[@name="father_name"]', "send_keys","jeff father")
    Add_staff(By.XPATH, '//input[@name="mother_name"]', "send_keys","jeff mother")
    time.sleep(5)
    Add_staff(By.XPATH, '//select[@name="gender"]', "click")
    Add_staff(By.XPATH, '//option[@value="Female"]', "click")
    time.sleep(2)
     
    Add_staff(By.XPATH, '//button[normalize-space(text())="Select Languages"]', "click") 
    Add_staff(By.XPATH, '//input[@type="checkbox" and @id="ms-opt-112"]', "click")
    print("✅Language selected succesfully")
    
    
    Add_staff(By.XPATH, '//select[@name="role"]', "click")
    time.sleep(2)
    Add_staff(By.XPATH, '//option[normalize-space(text())="Doctor"]', "click")
    Add_staff(By.XPATH, '//select[@name="designation"]',"click")
    Add_staff(By.XPATH, '//select[@name="gender"]', "click")
    Add_staff(By.XPATH, '//option[@value="Male"]', "click")
    Add_staff(By.XPATH, '//select[@name="marital_status"]', "click")
    Add_staff(By.XPATH, '//option[@value="Single"]', "click")
    
    Add_staff(By.XPATH, '//select[@name="blood_group"]', "click")
    Add_staff(By.XPATH, '//option[@value="1" and normalize-space(text())="O+"]', "click")
    Add_staff(By.XPATH, '//input[@name="dob"]', "send_keys","14-11-2000")
    Add_staff(By.XPATH, '//input[@name="Password"]',"click")
    Add_staff(By.XPATH, '//input[@name="Password"]',"send_keys","Venkat@123")
    print("✅ Stafff updated till password successfully")
    time.sleep(4)
    
    Add_staff(By.XPATH, '//option[@value="18" and normalize-space(text())="Vascular Surgeon"]', "click")
    Add_staff(By.XPATH, '//select[@name="department"]',"click")
    Add_staff(By.XPATH, '//option[@value="9" and normalize-space(text())="Neurology"]',"click")
    
    Add_staff(By.XPATH, '//button[normalize-space(text())="Select Specialist"]',"click")
    Add_staff(By.XPATH, '//input[@type="checkbox" and @id="ms-opt-1"]',"click")
    Add_staff(By.XPATH, '//input[@id="date_of_joining"]',"send_keys","14-11-2025")
    Add_staff(By.XPATH, '//input[@id="mobileno"]',"click")
    Add_staff(By.XPATH, '//input[@id="mobileno"]',"send_keys","8778798916")
    
    Add_staff(By.XPATH, '//input[@id="emgmobileno"]',"send_keys","8778712957")
    Add_staff(By.XPATH, '//input[@id="email"]',"send_keys","ajeffoni6@gmail.com")
    Add_staff(By.XPATH, '//textarea[@name="address"]',"click")
    print("✅Staff is updated till Email")
    
    Add_staff(By.XPATH, '//textarea[@name="permanent_address"]',"send_keys","chennai")
    Add_staff(By.XPATH, '//textarea[@id="qualification"]',"click")
    Add_staff(By.XPATH, '//textarea[@name="specialization"]',"click")
    Add_staff(By.XPATH, '//textarea[@name="note"]',"send_keys","nothing to write here")
    
    Add_staff(By.XPATH,'//textarea[@id="qualification"]',"send_keys","BE, cse")
    Add_staff(By.XPATH,'//button[@class="btn btn-info pull-right"]',"click")
    time.sleep(5)
    print("✅staff Saved succuessfully")
    
@allure.step("Performing {action} on {locator}")
def Charges(by, locator, action="click", value=None):
    element = wait.until(EC.presence_of_element_located((by, locator)))
    if action == "click":
        element.click()
    elif action == "send_keys":
        element.clear()
        element.send_keys(value)
    elif action == "scroll":
        scroll(element)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    print("Charges")
        
    @allure.step("Scrolling to element: {element}")
    def scroll(element):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    Charges(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/charges"]',"click")
    Charges(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/unittype"]',"click")
    Charges(By.XPATH,'//button[@class="btn btn-primary btn-sm addunittype add_unit_type_modal"]',"click")
    Charges(By.XPATH,'//input[@id="unit"]',"send_keys","Rupee")
    Charges(By.XPATH,'//button[@class="btn btn-info pull-right"]',"click")
    print("✅Unit type added successullyy")

    Charges(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/taxcategory"]',"click")
    Charges(By.XPATH,'//a[@class="btn btn-primary btn-sm charge_type"]',"click")
    Charges(By.XPATH,'//input[@id="name"]',"send_keys","CGST")
    Charges(By.XPATH,'//input[@name="percentage"]',"send_keys","10")
    Charges(By.XPATH,'//button[@class="btn btn-info pull-right"]',"click")
    print("✅Tax category added successullyy")
    
    Charges(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/chargetype"]',"click")
    Charges(By.XPATH,'//a[@class="btn btn-primary btn-sm charge_type"]',"click")
    Charges(By.XPATH,'//input[@name="charge_type"]',"send_keys","Online")
    Charges(By.XPATH,'//input[@name="charge_module[]"]',"click")
    Charges(By.XPATH,'//button[@class="btn btn-info pull-right"]',"click")
    print("✅Charges added successullyy")
          
    time.sleep(2) 
    Charges(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/chargecategory/charges"]',"click")
    
    Charges(By.XPATH,'//a[@class="btn btn-primary btn-sm charge_category"]',"click")
    
    Charges(By.XPATH,'//select[@class="form-control charge_type"]',"click")
    
    Charges(By.XPATH,'//option[@value="1" and normalize-space(text())="Appointment"]',"click")
    
    Charges(By.XPATH,'//input[@class="form-control name"]',"send_keys","Entry fee")
   
    Charges(By.XPATH,'//textarea[@class="form-control description"]',"send_keys","something to write there")
    
    Charges(By.XPATH,'//button[@class="btn btn-info pull-right"]',"click")
    print("✅Charge category added successfully")


     
    Charges(By.XPATH,'//a[@href="http://3.111.115.65/php-hms-frontend/admin/charges"]',"click")
    Charges(By.XPATH,'//a[@class="btn btn-primary btn-sm charge"]',"click")  
    Charges(By.XPATH,'//select[@class="form-control charge_type"]',"click")
    Charges(By.XPATH,'//option[@value="1" and normalize-space(text())="Appointment"]',"click")
    Charges(By.XPATH,'//span[@class="select2 select2-container select2-container--default"]',"click")
    Charges(By.XPATH,"//li[contains(@class, 'select2-results__option') and normalize-space()='Appointment Charge Category']","click")
    Charges(By.XPATH,'//select [@name="charge_unit_id"]',"click")
    time.sleep(2)
    Charges(By.XPATH,'//option[@value="1" and normalize-space(text())="Rs"]',"click")
    Charges(By.XPATH,'//input[@id="charge_name"]', "send_keys", "Appointment")
    Charges(By.XPATH,'//select[@id="taxcategory"]',"click")
    Charges(By.XPATH,'//option[@value="1" and normalize-space(text())="CGST"]',"click")

    Charges(By.XPATH,'//input[@name="standard_charge"]', "send_keys", 100)
    time.sleep(2)
    Charges(By.XPATH,'//textarea[@id="description"]', "send_keys", "something to write there")
    Charges(By.XPATH,'//button[@id="formaddbtn"]',"click")
    print("✅Charges added successfully")
          
          
    
          
   
         
   
         

   
        
        
if __name__ == "__main__":
        test_hospital_settings()
time.sleep(5)
















































