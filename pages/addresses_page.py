from seleniumpagefactory.Pagefactory import PageFactory


class AddressesPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "alias_field_txt": ("ID", "field-alias"),
        "address_field_txt": ("ID", "field-address1"),
        "city_field_txt": ("ID", "field-city"),
        "postcode_field_txt": ("ID", "field-postcode"),
        "phone_field_txt": ("ID", "field-phone"),
        "save_address_btn": ("CSS", ".btn.btn-primary.form-control-submit"),
        "saved_address_message": ("CSS", ".alert.alert-success"),
        "removed_address_message": ("CSS", ".alert.alert-success"),
        "delete_address_button": ("XPATH", "//a[@data-link-action='delete-address']")
    }

    def enter_alias(self, alias):
        self.alias_field_txt.clear()
        self.alias_field_txt.send_keys(alias)

    def enter_address(self, address):
        self.address_field_txt.clear()
        self.address_field_txt.send_keys(address)

    def enter_city(self, city):
        self.city_field_txt.clear()
        self.city_field_txt.send_keys(city)

    def enter_postcode(self, postcode):
        self.postcode_field_txt.clear()
        self.postcode_field_txt.send_keys(postcode)

    def enter_phone(self, phone):
        self.phone_field_txt.clear()
        self.phone_field_txt.send_keys(phone)

    def save_new_address(self):
        self.save_address_btn.click()

    def verify_new_address_is_saved(self):
        success_message = self.saved_address_message.text
        expected_message = "Address successfully added!"
        assert success_message == expected_message

    def verify_address_removed(self):
        success_message = self.removed_address_message.text
        expected_message = "Address successfully deleted!"
        assert success_message == expected_message
