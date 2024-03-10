from seleniumpagefactory.Pagefactory import PageFactory


class RegisterPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "social_title_man": ("ID", "field-id_gender-1"),
        "social_title_female": ("ID", "field-id_gender-2"),
        "name_field": ("ID", "field-firstname"),
        "lastname_field": ("ID", "field-lastname"),
        "reg_email_field": ("ID", "field-email"),
        "reg_password_field": ("ID", "field-password"),
        "birthday_field": ("ID", "field-birthday"),
        "terms_and_cond_checkbox": ("NAME", "psgdpr"),
        "customer_privacy_checkbox": ("NAME", "customer_privacy"),
        "save_button": ("XPATH", "//*[@id='customer-form']/footer/button")
    }

    def fill_the_registration_form(self, name, lastname, email, password, birthday):
        self.social_title_man.click()
        # self.social_title_female.click()
        self.name_field.send_keys(name)
        self.lastname_field.send_keys(lastname)
        self.reg_email_field.send_keys(email)
        self.reg_password_field(password)
        self.birthday_field(birthday)

    def mark_the_checkboxes(self):
        self.terms_and_cond_checkbox.click()
        self.customer_privacy_checkbox.click()

    def save_registration(self):
        self.save_button.click()
