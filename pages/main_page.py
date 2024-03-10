from seleniumpagefactory.Pagefactory import PageFactory


class MainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "sign_in_button": ("XPATH", "//div[@class='user-info']/a")
    }

    def click_sign_in_button(self):
        self.sign_in_button.click()
