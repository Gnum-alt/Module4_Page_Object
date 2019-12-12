from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #login_link.click()
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        #alert = self.browser.switch_to.alert
        #alert.accept()

    def should_be_login_link(self):
        # elf.browser.find_element(By.CSS_SELECTOR, "#login_link")
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"