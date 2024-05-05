from seleniumpagefactory.Pagefactory import PageFactory


class AccountPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "sign_out_button": ("XPATH", "//*[@id='_desktop_user_info']/div/a[1]"),
        "addresses_button": ("XPATH", "//*[@id='addresses-link']/span"),
        "create_new_address_link": ("XPATH", "//*[@id='content']/div[3]/a")

    }

    def click_sign_out_button(self):
        self.sign_out_button.click()

    def check_page_title(self):
        actual_title = self.driver.title
        expected_title = "My account"

        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    def click_addresses_button(self):
        self.addresses_button.click()

    def click_create_new_address_link(self):
        self.create_new_address_link.click()
