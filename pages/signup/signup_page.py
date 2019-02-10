from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class SignUpPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _register_first_name = "register_first_name"
    _register_last_name = "register_last_name"
    _register_company = "register_company"
    _register_job_title = "register_job_title"
    _register_phone = "register_phone"
    _register_email ="register_email"
    _register_password = "register_password"
    _check_box = "input[class='info-links-checkbox']"
    _register_button = "register_submit"

    _password_error = "//*[@id='form']/fieldset/form/div[5]/div/small"
    _name_error = "//div[@class='text-danger error']//small[text()='Nombre inválido']"
    _last_name_error = "//div[@class='text-danger error']//small[text()='Apellidos inválidos']"
    _company_error = "//*[@id='form']/fieldset/form/div[2]/div/small"
    _job_error = "//*[@id='form']/fieldset/form/div[3]/div[1]/div/div/small"
    _phone_error = "small[ng-if='model.error.phoneEmpty']"



    def register_firstname(self, firstname):
        self.sendKeys(firstname, self._register_first_name, locatorType='id')

    def register_last_name(self, lastname):
        self.sendKeys(lastname, self._register_last_name, locatorType='id')

    def register_company(self, company):
        self.sendKeys(company, self._register_company, locatorType='id')

    def register_job_title(self, job_title):
        self.sendKeys(job_title, self._register_job_title, locatorType='id')

    def register_phone(self, phone):
        self.sendKeys(phone, self._register_phone, locatorType='id')

    def register_email(self, email):
        self.sendKeys(email, self._register_email, locatorType='id')

    def register_password(self, password):
        self.sendKeys(password, self._register_password, locatorType='id')

    def click_check_box(self):
        self.elementClick(self._check_box, locatorType="css")

    def click_register_button(self):
        self.elementClick(self._register_button, locatorType="id")


    def sign_in_missing_password(self, firstname, lastname, company, job_title, phone, email):
        self.click_check_box()
        self.register_firstname(firstname)
        self.register_last_name(lastname)
        self.register_company(company)
        self.register_job_title(job_title)
        self.register_phone(phone)
        self.register_email(email)
        time.sleep(2)
        self.click_check_box()
        self.click_register_button()

    def create_error_all_empty_field(self):
        self.click_check_box()
        self.click_register_button()

    def verify_sin_in_password_error(self):
        result = self.isElementPresent(self._password_error, locatorType="xpath")
        return result

    def verify_name_error(self):
       result = self.isElementPresent(self._name_error, locatorType="xpath")
       return result

    def verify_last_name_error(self):
       result = self.isElementPresent(self._last_name_error, locatorType="xpath")
       return result

    def verify_company_error(self):
       result = self.isElementPresent(self._company_error, locatorType="xpath")
       return result

    def verify_job_error(self):
       result = self.isElementPresent(self._job_error, locatorType="xpath")
       return result

    def verify_phone_error(self):
       result = self.isElementPresent(self._phone_error, locatorType="css")
       return result