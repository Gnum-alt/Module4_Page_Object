from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not found"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form.well"), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form.well"), "Register form is not presented"
        assert True