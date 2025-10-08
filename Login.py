from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# Class for data for username & password
class Data:
    username = "test1@gmail.com"
    password = "Test@123"
    url = "http://3.111.115.65/demo/smart_hospital_src/site/login"
    patient = "Venkat"


# Class for Locators
class Locators:
     ## Login
    username_locator = "username"
    password_locator = "password"
    submit_button = '//button[@type="submit" and contains(@class, "btn") and text()="Sign In"]'

    ## Hospitals_details
    Setup = "//a[contains(@href,'http://3.111.115.65/demo/smart_hospital_src/')]/span[text()='Setup']" 
    Setup_Settings ='//a[@href="http://3.111.115.65/demo/smart_hospital_src/schsettings"]'
    Gendral_settings = "//a[@class='active']"
    Gendral_settings_Hospital_name = '//input[@name="sch_name"]'
    Gendral_settings_Hospital_code = '//input[@name="sch_dise_code"]'
    Gendral_settings_Hospital_Add = '//input[@name="sch_address"]'
    Gendral_settings_Hospital_PH = '//input[@name="sch_phone"]'
    Gendral_settings_Hospital_email = '//input[@name="sch_email"]' 
    Gendral_settings_Hospital_Logo =  '//a[@class="btn btn-primary btn-sm upload_logo"]'
    Gendral_settings_Hospital_Logo_input = '//input[@type="file"]'
    Gendral_settings_Hospital_Logo_Crop = '//button[@id="cropButton"]'
    Gendral_settings_Hospital_Logo_small = '//a[@class="btn btn-primary btn-sm upload_minilogo "]'
    Gendral_settings_Hospital_Logo_small_input = '//input[@type="file"]'
    Gendral_settings_Hospital_QR = '//a[@onclick="generateqr()"]'
    Gendral_settings_Hospital_QR_close = '//span[@class="close"]'
    Gendral_settings_Hospital_save = '//button[@class="btn btn-primary submit_schsetting pull-right edit_setting"]'
    
    
    # #Human resource Setup
    Setup_Humanresources = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/leavetypes"]'
    Setup_HR_Specilization ='//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/specialist"]'
    Add_Specilization = '//a[@class="btn btn-primary btn-sm specialist"]'
    Text_Specilization = '//input[@name="type"]'
    Save_Specilization = '//button[@class="btn btn-info pull-right"]'
    Edit_Specilization = '//a[@onclick="get(12)"]'   
    Delete_Specilization  = '//a[@onclick="deleterecord(12)"]'
    Setup_HR_Designation = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/designation/designation"]'
    Add_Designation = '//a[@class="btn btn-primary btn-sm designation"]'
    Text_Designation = '//input[@name="type"]'
    Save_Designation = '//button[@class="btn btn-info pull-right"]'
    Setup_HR_Department = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/department"]'
    Add_Department = '//a[@class="btn btn-primary btn-sm department"]'
    Text_Department = '//input[@name="type"]'
    Save_Department = '//button[@class="btn btn-info pull-right"]'
    Setup_HR_Leave = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/leavetypes"]'
    Add_Leave = '//a[@class="btn btn-primary btn-sm leavetype"]'
    Text_Leave = '//input[@name="type"]'
    Save_Leave = '//button[@class="btn btn-info pull-right"]'

    # #Human resource
    Human_resources = "//a[@href='http://3.111.115.65/demo/smart_hospital_src/admin/staff']/span[text()='Human Resource']"

    Add_staff ='//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/staff/create"]'
    First_name = '//input[@name="name"]'
    Last_Name = '//input[@name="surname"]'
    Father_Name = '//input[@name="father_name"]'
    Mother_Name = '//input[@name="mother_name"]'
    Gender_Click = '//select[@name="gender"]'
    Gender_male = '//option[@value="Male"]'
    Marital_Status_Click = '//select[@name="marital_status"]' 
    Marital_Status_Single = '//option[@value="Single"]'
    Blood_Group = '//select[@name="blood_group"]'
    Blood_Group_Ove = "//option[@value='1' and normalize-space(text())='O+']"
    Date_Of_Birth = '//input[@name="dob"]'
    Password = '//input[@name="Password"]'
    Languages = "//button[normalize-space(text())='Select Languages']"
    Languages_Azerbaijan = "//input[@type='checkbox' and @id='ms-opt-26']"
    Role = '//select[@name="role"]'
    Role_Doctor = "//option[normalize-space(text())='Doctor']"
    Designation = '//select[@name="designation"]'
    Designation_vascular = "//option[@value='18' and normalize-space(text())='Vascular Surgeon']"
    Department = '//select[@name="department"]'
    Department_vascular = "//option[@value='9' and normalize-space(text())='Neurology']"
    Specialist = "//button[normalize-space(text())='Select Specialist']"
    Specialist_vascular = "//input[@type='checkbox' and @id='ms-opt-1']"
    Date_Of_Joining = '//input[@id="date_of_joining"]' #01/07/2025
    Phone = '//input[@id="mobileno"]'
    Phone_Emergency_Contact = '//input[@id="emgmobileno"]' 
    Email = '//input[@id="email"]'
    Photo = '//input[@class="filestyle form-control"]'
    Current_Address = '//textarea[@name="address"]'
    Permanent_Address = '//textarea[@name="permanent_address"]'
    Qualification = '//textarea[@id="qualification"]'
    Work_Experience = ' //textarea[@id="qualification"]'
    Specialization = ' //textarea[@name="specialization"]'
    Note = ' //textarea[@name="note"]'
    Pan_Number = ' //input[@name="pan_number"]'
    National_Identification_Number = ' //input[@name="identification_number"]'
    Local_Identification_Number = ' //input[@name="local_identification_number"]'

    Add_info = '//a[@data-original-title="Collapse"]'

    Payroll_EPF_No = '//input[@name="epf_no"]'
    Payroll_Basic_Salary = '//input[@name="basic_salary"]'
    Payroll_Contract_Type = '//select[@name="contract_type"]'
    Payroll_Contract_Permanent = '//option[@value="permanent"]'                                                              
    Payroll_Work_Shift = '//input[@id="shift"]'
    Payroll_Work_Location = '//input[@name="location"]'

    Sick_Leave = '//input[@name="alloted_leave_2"]'
    Casual_Leave = '//input[@name="alloted_leave_1"]'

    Bank_Account_Title = '//input[@name="account_title"]'
    Bank_Account_No = '//input[@name="bank_account_no"]'
    Bank_Name = '//input[@name="bank_name"]'
    Bank_IFSC_Code = '//input[@name="ifsc_code"]'
    Bank_Branch_Name = '//input[@name="bank_branch"]'

    Resume = '//input[@name="first_doc"]'	
    Joining_Letter = '//input[@name="second_doc"]'	
    Other_Documents = '//input[@name="fourth_doc"]'	

    Save_ADD_Staff = '//button[@class="btn btn-info pull-right"]'

    Appointment = "//a[contains(@href,'/appointment/index')]/span[text()='Appointment']"
    scroll_target = '//div[contains(@class, "sidebar-menu")]'  # Example element to demonstrate upward scrolling
    Setup_Appointment = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/onlineappointment/"]'
    


    #Hospital Charges
    Setup_Hopital_Charges = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/charges"]'
    Unit_Type = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/unittype"]'
    Unit_Type_Add = '//button[@class="btn btn-primary btn-sm addunittype add_unit_type_modal"]'
    Unit_Type_text = '//input[@id="unit"]'
    Unit_Type_Save = '//button[@class="btn btn-info pull-right"]'

    Tax_Category = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/taxcategory"]'
    Tax_Category_Add = '//a[@class="btn btn-primary btn-sm charge_type"]'
    Tax_Category_text = '//input[@id="name"]'
    Tax_Category_percentage = ' //input[@name="percentage"]'
    Tax_Category_Save = '//button[@class="btn btn-info pull-right"]'

    Charge_Type = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/chargetype"]'
    Charge_Type_Add = '//a[@class="btn btn-primary btn-sm charge_type"]'
    Charge_Type_text = '//input[@name="charge_type"]'
    Charge_Type_Appointmentmod = '//input[@value="opd"]'
    Charge_Type_OPDmod = '//input[@value="appointment"]'
    Charge_Type_Save = '//button[@class="btn btn-info pull-right"]'

    Charge_Category = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/chargecategory/charges"]'
    Charge_Category_Add = '//a[@class="btn btn-primary btn-sm charge_category"]'
    Charge_Category_Charge_Type = '//select[@class="form-control charge_type"]'
    Charge_Category_Appointmentmod = '//option[@value="1" and normalize-space(text())="Appointment"]'
    Charge_Category_OPDmod ='//option[@value="2" and normalize-space(text())="OPD"]'
    Charge_Category_Name = '//input[@class="form-control name"]'
    Charge_Category_Description = '//textarea[@class="form-control description"]'
    Charge_Category_Save = '//button[@class="btn btn-info pull-right"]'

    Charges = '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/charges"]'
    Charges_Add = '//a[@class="btn btn-primary btn-sm charge"]'
    Charges_Charge_Type = '//select[@class="form-control charge_type"]'
    Charges_Charge_Type_Appointmentmod = '//option[@value="1" and normalize-space(text())="Appointment"]'
    Charges_Charge_Type_OPDmod ='//option[@value="2" and normalize-space(text())="OPD"]'
    Charges_Category = '//span[@class="select2-selection__rendered"]'
    Charges_Category_AppointmentCharges = '//option[@value="2" and normalize-space(text())="Appointment Charges"]'
    Charges_Category_OPDmod ='//option[@value="2" and normalize-space(text())="OPD"]'
    Charges_Unit_Type = '//select [@name="charge_unit_id"]'
    Charges_Unit_Type_Rs = '//option[@value="1" and normalize-space(text())="Rs"]'
    Charges_Name = '//input[@id="charge_name"]'
    Charges_tax ='//select[@id="taxcategory"]'
    Charges_tax_category ='//option[@value="1" and normalize-space(text())="CGST"]'
    Charges_Std_Amount = '//input[@name="standard_charge"]'
    Charges_description = '//textarea[@id="description"]'       
    Charges_Type_Save = '//button[@id="formaddbtn"]'   
    Setup_appointment= '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/onlineappointment/"]'
    Appointment_shift= '//a[@href="http://3.111.115.65/demo/smart_hospital_src/admin/onlineappointment/globalshift/"]'
    Appointment_addshift= '//button[@onclick="addShiftModal()"]'
    Shift_name= '//input[@name="name"]'
    Shift_fromtime= '//input[@name="time_from"]'
     










    
   



class Venkat(Data, Locators):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login_and_scroll_up(Login):
        try:
            Login.driver.maximize_window()
            Login.driver.get(Login.url)
            sleep(3)

            # Login Process
            Login.driver.find_element(By.NAME, Login.username_locator).send_keys(Login.username)
            sleep(2)
            Login.driver.find_element(By.NAME, Login.password_locator).send_keys(Login.password)
            sleep(2)
            Login.driver.find_element(By.XPATH, Login.submit_button).click()
            sleep(5)
           

        except Exception as error:
            print("ERROR during login: ", error)
       
   
            # sidebar = WebDriverWait(Login.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, '//aside[@class="main-sidebar affix-top"]'))  # Replace "//aside" with your sidebar locator
            # )
            # # Scroll to the bottom of the sidebar
            # print("Scrolling to the bottom of the sidebar...")
            # Login.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)
            # print("Scroll completed.")
            # sleep(5)


            

        # except NoSuchElementException as e:
        #     print(f"Element not found: {e}")
        # except Exception as error:
        #     print(f"ERROR: {error}")
        # finally:
        #     print("SUCCESS: Automation ends!")
        #     Login.driver.quit()


    # def Hospitals_details(Hospital_details):
    #     try:
    #         # Hospital_details.driver.maximize_window()
    #         # Hospital_details.driver.get(Hospital_details.url)
    #         # sleep(3)

    #         # Login Process
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Setup).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Setup_Settings).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_name).clear()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_name).send_keys("Venkat Hospital")
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_code).clear()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_code).send_keys("66446161")
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Add).clear()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Add).send_keys("Chennai")
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_PH).clear()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_PH).send_keys("9344269524")
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_email).clear()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_email).send_keys("venktrmn2114@gmail.com")
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Logo).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Logo_input).send_keys("C:\\Users\\VENKATARAMANAN S\\Downloads\\6520058.png")
    #         sleep(5)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Logo_Crop).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Logo_small).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Logo_small_input).send_keys("C:\\Users\\VENKATARAMANAN S\\Downloads\\7055819.jpg")
    #         sleep(5)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_Logo_Crop).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_QR).click()
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_QR_close).click()
    #         sleep(2)

    #         Hospital_details.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         sleep(2)
    #         Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_save).click()
    #         sleep(2)
           
    #     except Exception as error:
    #         print("ERROR during login: ", error)

    
    # def Setup_HR(Setup_HR):
    #     try:
           
    #         # Login Process
          
            
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Setup_Humanresources).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Setup_HR_Specilization).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Add_Specilization).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Specilization).clear()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Specilization).send_keys("Vascular Surgeon")
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Save_Specilization).click()
    #         sleep(2)

    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Setup_HR_Designation).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Add_Designation).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Designation).clear()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Designation).send_keys("Vascular Surgeon")
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Save_Designation).click()
    #         sleep(2)

    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Setup_HR_Department).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Add_Department).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Department).clear()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Department).send_keys("Vascular Surgeon")
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Save_Department).click()
    #         sleep(2)

    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Setup_HR_Leave).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Add_Leave).click()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Leave).clear()
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Text_Leave).send_keys("Casual Leave")
    #         sleep(2)
    #         Setup_HR.driver.find_element(By.XPATH, Setup_HR.Save_Leave).click()
    #         sleep(2)
  
    #     except Exception as error:
    #         print("ERROR during login: ", error)

    # def Human_resource(Human_resource):
    #     try:

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Human_resources).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Add_staff).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.First_name).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.First_name).send_keys("Venkata")
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Last_Name).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Last_Name).send_keys("S")
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Father_Name).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Father_Name).send_keys("Venkat's Father")
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Mother_Name).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Mother_Name).send_keys("Venkat's Mother")
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Gender_Click).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Gender_male).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Marital_Status_Click).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Marital_Status_Single).click() 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Blood_Group).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Blood_Group_Ove).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Birth).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Birth).send_keys("11/14/2000") ### 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Password).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Password).send_keys("Venkat@1234")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Languages).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Languages_Azerbaijan).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Role).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Role_Doctor).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Designation).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Designation_vascular).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Department).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Department_vascular).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Specialist).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Specialist_vascular).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Joining).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Joining).send_keys("123")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone).send_keys("123")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone_Emergency_Contact).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone_Emergency_Contact).send_keys("123")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Email).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Email).send_keys("123.abcd")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Photo).send_keys("C:\\Users\\VENKATARAMANAN S\\Downloads\\6520058.png")
    #         sleep(5)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Current_Address).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Current_Address).send_keys("Chennai") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Permanent_Address).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Permanent_Address).send_keys("Chennai") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Qualification).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Qualification).send_keys("MBBS") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Work_Experience).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Work_Experience).send_keys("abc") ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Specialization).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Specialization).send_keys("Vascular surgon") ## Not Needed.
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Note).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Note).send_keys("None") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Pan_Number).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Pan_Number).send_keys("ABCD123F") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.National_Identification_Number).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.National_Identification_Number).send_keys("8877979998989") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Local_Identification_Number).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Local_Identification_Number).send_keys("Chennai") 
    #         sleep(2)

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Add_info).click()
    #         sleep(2)

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_EPF_No).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_EPF_No).send_keys("215454645") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Basic_Salary).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Basic_Salary).send_keys("abcd") ##
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Contract_Type).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Contract_Permanent).click()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Work_Shift).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Work_Shift).send_keys("Morning") ## Not Needed.
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Work_Location).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Work_Location).send_keys("Chennai") 
    #         sleep(2)


    #         Human_resource.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         sleep(2) 



    #         # Human_resource.driver.find_element(By.XPATH, Human_resource.Sick_Leave).clear()
    #         # sleep(2)
    #         # Human_resource.driver.find_element(By.XPATH, Human_resource.Sick_Leave).send_keys("abcd") ##
    #         # sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Casual_Leave).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Casual_Leave).send_keys("abcd") ##
    #         sleep(2)

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Account_Title).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Account_Title).send_keys("Venkat") 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Account_No).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Account_No).send_keys("68464646656463") ##
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Name).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Name).send_keys("SBI") ##
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_IFSC_Code).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_IFSC_Code).send_keys("ICIC0006009") ##  Validication like Invalid IFSC Code or an error occurred. Please try again. sholud not Come in tost message.
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Branch_Name).clear()
    #         sleep(2)   
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_Branch_Name).send_keys("Velachery") 
    #         sleep(2)

            
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Resume).send_keys("C:\\Users\\VENKATARAMANAN S\\Downloads\\6520058.png")
    #         sleep(5) 
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Joining_Letter).send_keys("C:\\Users\\VENKATARAMANAN S\\Downloads\\7055819.jpg")
    #         sleep(5)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Other_Documents).send_keys("C:\\Users\\VENKATARAMANAN S\\Downloads\\7055819.jpg")
    #         sleep(5)
            
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Save_ADD_Staff).click()
    #         sleep(2)


    #         Human_resource.driver.execute_script("window.scrollBy(0, -500);")
    #         Human_resource.driver.execute_script("window.scrollBy(0, -500);")
    #         Human_resource.driver.execute_script("window.scrollBy(0, -500);")  # Scrolls up by 500 pixels
    #         sleep(10 )

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Birth).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Birth).send_keys("11/14/2000") ### 
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Password).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Password).send_keys("Venkat@1234")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Joining).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Date_Of_Joining).send_keys("11/14/2000")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone).send_keys("9344269621")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone_Emergency_Contact).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Phone_Emergency_Contact).send_keys("9344269527")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Email).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Email).send_keys("venktrmn24@gmail.com")  ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Work_Experience).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Work_Experience).send_keys("5") ###
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Basic_Salary).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Payroll_Basic_Salary).send_keys("50000") ##
    #         sleep(2)

    #         Human_resource.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         sleep(2)

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Casual_Leave).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Casual_Leave).send_keys("10") ##
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_IFSC_Code).clear()
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Bank_IFSC_Code).send_keys("SBIN0012747") ##
    #         sleep(2)
    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Save_ADD_Staff).click()
    #         sleep(5)

    #         Human_resource.driver.find_element(By.XPATH, Human_resource.Human_resources).click()
    #         sleep(3)
            
            

    #         # Hospital_details.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         # sleep(2)
    #         # Hospital_details.driver.find_element(By.XPATH, Hospital_details.Gendral_settings_Hospital_save).click()
    #         # sleep(2)

    #     except Exception as error:
    #         print("ERROR during login: ", error)

    # def Hospital_Charges(Hospital_Charges):
    #     try:
           
    #         # Login Process
          
            
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Setup).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Setup_Hopital_Charges).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_Add).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_text).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_text).send_keys("Rs")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_Save).click()
    #         sleep(5)

    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Add).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_text).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_text).send_keys("CGST")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_percentage).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_percentage).send_keys("8")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Save_Designation).click()
    #         sleep(2)

    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Add).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_text).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_text).send_keys("opd")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Appointmentmod).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_OPDmod).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Save).click()
    #         sleep(2)




    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Add).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Charge_Type).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Appointmentmod).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Name).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Name).send_keys("Appointment Charges")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Description).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Description).send_keys("Appointment Charges")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Save).click()
    #         sleep(2)

    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Add).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Charge_Type).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Charge_Type_Appointmentmod).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Category).click()
    #         sleep(2)

    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Category_AppointmentCharges).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Unit_Type).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Unit_Type_Rs).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Name).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Name).send_keys("Appointment charges for doctor")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_tax).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_tax_category).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_tax).click()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Std_Amount).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Std_Amount).send_keys("1")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_description).clear()
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_description).send_keys("something to write here")
    #         sleep(2)
    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Type_Save).click()
    #         sleep(5)

    #         Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Setup).click()
    #         sleep(2)



        

          

        

    #     except Exception as error:
    #         print("ERROR during login: ", error)
 
def Appointment_setup():  
        try:
           
            # Login Process
          
            
            Appoitment_setup.driver.find_element(By.XPATH, Appoitment_setup.Setup).click()
            sleep(2)
            Appoitment_setup.driver.find_element(By.XPATH, Appoitment_setup.Setup_Hopital_Charges).click()
            sleep(2)









            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_Add).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_text).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_text).send_keys("Rs")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Unit_Type_Save).click()
            sleep(5)

            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Add).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_text).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_text).send_keys("CGST")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_percentage).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Tax_Category_percentage).send_keys("8")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Save_Designation).click()
            sleep(2)

            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Add).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_text).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_text).send_keys("opd")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Appointmentmod).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_OPDmod).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Type_Save).click()
            sleep(2)




            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Add).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Charge_Type).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Appointmentmod).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Name).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Name).send_keys("Appointment Charges")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Description).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Description).send_keys("Appointment Charges")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charge_Category_Save).click()
            sleep(2)

            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Add).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Charge_Type).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Charge_Type_Appointmentmod).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Category).click()
            sleep(2)

            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Category_AppointmentCharges).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Unit_Type).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Unit_Type_Rs).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Name).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Name).send_keys("Appointment charges for doctor")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_tax).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_tax_category).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_tax).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Std_Amount).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Std_Amount).send_keys("1")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_description).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_description).send_keys("something to write here")
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Charges_Type_Save).click()
            sleep(5)

            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Setup).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Setup_appointment).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Appointment_shift).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Appointment_addshift).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Shift_name).click()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.Shift_fromtime).clear()
            sleep(2)
            Hospital_Charges.driver.find_element(By.XPATH, Hospital_Charges.shift_fromtime).send_keys("10:00 AM")
            sleep(2)







        

          

        

        except Exception as error:
            print("ERROR during login: ", error)
 

# Main execution function
if __name__ == "__main__":
    venkat = Venkat()
    venkat.login_and_scroll_up()
    venkat.Hospitals_details()
    venkat.Setup_HR()
    venkat.Human_resource()
    venkat.Hospital_Charges()
    # venkat.Appointment_shift() 

   
    
   
    
    
    

    
    
    
    
    
