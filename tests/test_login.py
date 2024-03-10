from selenium import webdriver
import unittest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        self.driver.get("https://mystore-testlab.coderslab.pl/index.php?controller=authentication&back=my-account")
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)

    def test_valid_login(self):
        """Test login with valid credentials"""
        test_data = [
            {"email": "shelby@peakyblinders.com",
             "password": "123321"},
            {"email": "jaydoe@fake.com",
             "password": "12344321"}
        ]

        for data in test_data:
            email = data["email"]
            password = data["password"]

            self.login_page.enter_email(email)
            self.login_page.enter_password(password)
            self.login_page.click_login_button()
            self.account_page.check_page_title()
            self.account_page.click_sign_out_button()

    def test_invalid_login(self):
        """Test login with invalid credentials:
        1st test with valid email and invalid password
        2nd test with invalid email and valid password"""
        test_data = [
            {"email": "shelby@peakyblinders.com",
             "password": "invalidPassword"},
            {"email": "invalid@email.cu",
             "password": "12344321"}
        ]
        for data in test_data:
            email = data["email"]
            password = data["password"]

            self.login_page.enter_email(email)
            self.login_page.enter_password(password)
            self.login_page.click_login_button()
            self.login_page.check_authentication_failed()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
