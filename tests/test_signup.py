from pages.signup.signup_page import SignUpPage
import time
import unittest
import pytest
import string
from random import *

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    # Setup
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp, setUp):
        self.si = SignUpPage(self.driver)
        self.allchar = string.ascii_letters + string.punctuation + string.digits
        self.char258 = "".join(choice(self.allchar) for x in range(randint(0, 258)))

    # Click on T&C then Sign up button without filling up any required field
    @pytest.mark.run(order=1)
    def test_error_fields(self):
        self.si.create_error_all_empty_field()
        time.sleep(2)
        name = self.si.verify_name_error()
        assert name == True
        lastname =self.si.verify_last_name_error()
        assert lastname == True
        company = self.si.verify_company_error()
        assert company == True
        job = self.si.verify_job_error()
        assert job == True
        phone = self.si.verify_phone_error()
        assert phone == True

    # Sign up to application with missing password and verify Success
    @pytest.mark.run(order=2)
    def test_missing_password(self):
        self.si.sign_in_missing_password("testname", "testlastname", "testcompany", "test_job_title", "4155555555",
                                         "test@gmail.com")
        time.sleep(2)
        result = self.si.verify_sin_in_password_error()
        assert result == True



