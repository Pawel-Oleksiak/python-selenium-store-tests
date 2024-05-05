from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.addresses_page import AddressesPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestNewAddress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        self.driver.get("https://mystore-testlab.coderslab.pl/index.php?controller=authentication&back=my-account")
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.addresses_page = AddressesPage(self.driver)

    def test_add_address(self):
        self.login_page.enter_email("shelby@peakyblinders.com")
        self.login_page.enter_password("123321")
        self.login_page.click_login_button()

        self.account_page.check_page_title()
        self.account_page.click_addresses_button()
        self.account_page.click_create_new_address_link()

        self.addresses_page.enter_alias("Peaky Address")
        self.addresses_page.enter_address("Golden Street")
        self.addresses_page.enter_city("London")
        self.addresses_page.enter_postcode("201 201")
        self.addresses_page.enter_phone("404 201 200")
        self.addresses_page.save_new_address()
        self.addresses_page.verify_new_address_is_saved()

        self.account_page.click_sign_out_button()

    def test_remove_address(self):
        self.login_page.enter_email("shelby@peakyblinders.com")
        self.login_page.enter_password("123321")
        self.login_page.click_login_button()

        self.account_page.check_page_title()
        self.account_page.click_addresses_button()

        addresses_list = self.addresses_page.delete_address_button
        addresses_list[1].click()
        self.addresses_page.verify_address_removed()
        self.account_page.click_sign_out_button()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
