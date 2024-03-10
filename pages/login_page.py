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
        "auth_failed_error": ("CSS_SELECTOR", "li.alert.alert-danger")
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

    # FIXME: Assertion is not working properly, error message cannot be found
    def check_authentication_failed(self):
        try:
            error_element = self.auth_failed_error
            error_message_text = error_element.text

            expected_error_message = "Authentication failed."

            self.asserEqual(error_message_text, expected_error_message)
            print(f"{expected_error_message} - expected error message.\n"
                  f"{error_message_text} - error message found on website.")
        except KeyError:
            print("\nError message not found.")
