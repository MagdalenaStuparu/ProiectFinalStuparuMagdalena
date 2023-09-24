import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Test2(unittest.TestCase):

    HOME_Page = (By.CLASS_NAME, 'fa-home')
    Sign_upbtn = (By.CLASS_NAME, 'fa-lock')
    Signup_form = (By.CLASS_NAME, 'signup-form')
    Name_new_user = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[2]')
    Email_nwe_user = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[3]')
    Signup_btn = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/button')
    Login_form = (By.CLASS_NAME, 'text-center')
    Mrs_box = (By.ID, 'id_gender2')
    Password_form = (By.ID, 'password')
    Days_select = (By.ID, 'days')
    Name_form = (By.ID, 'name')
    Email_form = (By.ID, 'email')
    Enter_acount = (By.XPATH, '/html/body/section/div/div/div/div[1]/h2/b')
    First_name = (By.ID, 'first_name')
    Last_name = (By.ID, 'last_name')
    Company_fild = (By.ID, 'company')
    Address_1 = (By.ID, 'address1')
    Country_drop_down = (By.ID, 'country')
    State_fild = (By.ID, 'state')
    City_fild = (By.ID, 'city')
    Zipcode_fild = (By.ID,'zipcode')
    Mobile_number = (By.ID, 'mobile_number')
    Create_account = (By.XPATH, '/html/body/section/div/div/div/div[1]/form/button')
    Continue_btn = (By.LINK_TEXT, 'Continue')
    Message_existing_email = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/p')
    Existind_user_email = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/input[2]')
    Password_existing_user = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/input[3]')
    Login_btn = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/button')
    Login_out = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[4]/a')
    Message_incorect_password_email = (By.XPATH, '/html/body/section/div/div/div[1]/div[1]/form/p')
    Susbscribe_email = (By.ID,'susbscribe_email')
    Subscribe_btn = (By.ID,'subscribe')
    Subscribe_successful = (By.XPATH, '/html/body/footer/div[1]/div/div/div[1]/div/div')

    CONTACT_US_LINK = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[8]/a')
    Name_fild = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[1]/input")
    Email_fild = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[2]/input')
    Subject_fild = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[3]/input')
    Message_fild = (By.XPATH, '//*[@id="message"]')
    Submit_btn = (By.XPATH, '/html/body/div/div[2]/div[1]/div/div[3]/form/div[6]/input')
    Result = (By.CLASS_NAME, 'alert-success')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://automationexercise.com/')
        self.chrome.implicitly_wait(5)


    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://automationexercise.com/'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_home_page_title(self):
        self.chrome.find_element(*self.HOME_Page).click()
        actual = self.chrome.title
        expected = 'Automation Exercise'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_sing_up_and_login_page_title(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        actual = self.chrome.title
        expected = 'Automation Exercise - Signup / Login'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_New_User_Signup_form_is_visible(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        elem = self.chrome.find_element(*self.Signup_form)
        self.assertTrue(elem.is_displayed(), 'New User Signup form nu e vizibil')

    def test_new_user_login(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        self.chrome.find_element(*self.Name_new_user).send_keys('Magdalena')
        self.chrome.find_element(*self.Email_nwe_user).send_keys('magda11ro@yahoo.com')
        self.chrome.find_element(*self.Signup_btn).click()
        self.chrome.find_element(*self.Mrs_box).click()
        self.chrome.find_element(*self.Password_form).send_keys('Magdalena22')
        day = Select(self.chrome.find_element(By.ID, "days"))
        day.select_by_visible_text("17")
        months = Select(self.chrome.find_element(By.ID, "months"))
        months.select_by_visible_text('May')
        years = Select(self.chrome.find_element(By.ID, "years"))
        years.select_by_visible_text('1980')
        self.chrome.find_element(*self.First_name).send_keys('Magdalena')
        self.chrome.find_element(*self.Last_name).send_keys('Stuparu')
        self.chrome.find_element(*self.Company_fild).send_keys('Smart Business')
        self.chrome.find_element(*self.Address_1).send_keys('Satu Mare')
        country = Select(self.chrome.find_element(By.ID, 'country'))
        country.select_by_visible_text("Canada")
        self.chrome.find_element(*self.State_fild).send_keys('Canada')
        self.chrome.find_element(*self.City_fild).send_keys('Satu Mare')
        self.chrome.find_element(*self.Zipcode_fild).send_keys('440123')
        self.chrome.find_element(*self.Mobile_number).send_keys('074555844855')
        sleep = 30
        self.chrome.find_element(*self.Create_account).click()
        self.chrome.find_element(*self.Continue_btn).click()


    def test_existing_email(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        self.chrome.find_element(*self.Name_new_user).send_keys('Magdalena')
        self.chrome.find_element(*self.Email_nwe_user).send_keys('magda99ro@yahoo.com')
        self.chrome.find_element(*self.Signup_btn).click()
        elem = self.chrome.find_element(*self.Message_existing_email)
        self.assertTrue(elem.is_displayed(), 'Email Address already exist!')

    def test_Login_to_your_account(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        self.chrome.find_element(*self.Existind_user_email).send_keys('magda99ro@yahoo.com')
        self.chrome.find_element(*self.Password_existing_user).send_keys('Magdalena22')
        self.chrome.find_element(*self.Login_btn).click()
        self.chrome.find_element(*self.Login_out).click()

    def test_incorect_email_or_password(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        self.chrome.find_element(*self.Existind_user_email).send_keys('magda99ro@yahoo.com')
        self.chrome.find_element(*self.Password_existing_user).send_keys('Magdalena2')
        self.chrome.find_element(*self.Login_btn).click()
        elem = self.chrome.find_element(*self.Message_incorect_password_email)
        self.assertTrue(elem.is_displayed(), 'Your email or password is incorrect!')

    def test_email_subscribed_option(self):
        self.chrome.find_element(*self.Sign_upbtn).click()
        self.chrome.find_element(*self.Susbscribe_email).send_keys('magda99ro@yahoo.com')
        slep=30
        self.chrome.find_element(*self.Subscribe_btn).click()
        elem = self.chrome.find_element(*self.Subscribe_successful)
        self.assertTrue(elem.is_displayed(), 'You have been successfully subscribed!')




    def test_Contact_page_url(self):
        self.chrome.find_element(*self.CONTACT_US_LINK).click()
        self.chrome.implicitly_wait(10)
        actual = self.chrome.current_url
        expected = 'https://automationexercise.com/contact_us'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_page_title(self):
        self.chrome.find_element(*self.CONTACT_US_LINK).click()
        actual = self.chrome.title
        expected = 'Automation Exercise - Contact Us'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_login(self):
        self.chrome.find_element(*self.CONTACT_US_LINK).click()

        self.chrome.find_element(*self.Name_fild).send_keys('Magdalena')
        self.chrome.find_element(*self.Email_fild).send_keys('magda99ro@yahoo.com')
        self.chrome.find_element(*self.Subject_fild).send_keys('Testare')
        self.chrome.find_element(*self.Message_fild).send_keys('Testare Automata')
        sleep= 80
        self.chrome.find_element(*self.Submit_btn).click()
        sleep = 50
        obj = self.chrome.switch_to.alert
        obj.accept()
        actual_result = self.chrome.find_element(By.CLASS_NAME, 'alert-success').text
        expected_result = "Success! Your details have been submitted successfully."
        assert actual_result == expected_result, "Error: The result text is incorrect"
