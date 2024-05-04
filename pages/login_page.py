from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "email_field": ("ID", "field-email"),
        "password_field": ("ID", "field-password"),
        "submit_button": ("ID", "submit-login"),
        "no_acc_button": ("XPATH", "//*[@id='content']/div"),
        "auth_failed_error": ("CSS", "li.alert.alert-danger")
    }

    def enter_email(self, email):
        self.email_field.clear()
        self.email_field.send_keys(email)

    def enter_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.submit_button.click()

    def click_no_acc_button(self):
        self.no_acc_button.click()

    def check_authentication_failed(self):
        error_message_text = self.auth_failed_error.text

        expected_error_message = "Authentication failed."

        assert error_message_text == expected_error_message
    #    if error_message_text == expected_error_message:
    #        print("\nAssertion True.")
    #    else:
    #        print("\nAssertion False.")
