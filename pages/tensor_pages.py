from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .locators import TensorMainPageLocators, TensorAboutPageLocators

class TensorMainPage(BasePage):    
    
    def should_be_power_in_people_blog(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(TensorMainPageLocators.POWER_IN_PEOPLE_BLOG))

    def open_about_page(self):
        about_link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(TensorMainPageLocators.LINK_ABOUT_PAGE))
        about_link.click()
        return TensorAboutPage(browser=self.browser, url=self.browser.current_url)
    

class TensorAboutPage(BasePage):

    def check_url(self):
        assert self.browser.current_url == 'https://tensor.ru/about', "Wrong page opened"

    def check_size_images(self):
        images = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TensorAboutPageLocators.CHAPTER_WORK)).find_elements(By.TAG_NAME,"img")
                
        height = {image.get_attribute('height') for image in images}
        width = {image.get_attribute('width') for image in images}
        assert len(height) == 1 and len(width) == 1, "Image sizes vary" 