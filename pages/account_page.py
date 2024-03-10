from seleniumpagefactory.Pagefactory import PageFactory


# jaydoe@fake.com 12344321
# qra@fake.com 12344321

class AccountPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "sign_out_button": ("XPATH", "//*[@id='_desktop_user_info']/div/a[1]")

    }

    def click_sign_out_button(self):
        self.sign_out_button.click()

    def check_page_title(self):
        actual_title = self.driver.title
        expected_title = "My account"

        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
