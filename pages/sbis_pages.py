import os
import time
from .tensor_pages import TensorMainPage
from .base_page import BasePage
from .locators import SbisMainPageLocators, SbisContactPageLocators, SbisDownloadPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import logging

LOGGER = logging.getLogger(__name__)

class SbisMainPage(BasePage):
    def open_contact_menu(self):
        contact_element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPageLocators.CONTACT_MENU_LINK))
        contact_element.click()
                              
    def open_contact_page(self):
        contact_link = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable(SbisMainPageLocators.CONTACT_PAGE_LINK))
        contact_link.click()
        return SbisContactPage(browser=self.browser, url=self.browser.current_url)
    
    def open_download_page(self):
        download_page_link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPageLocators.DOWNLOAD_PAGE_LINK), message="Element not found")
        download_page_link.click()

        return SbisDownloadPage(browser=self.browser, url=self.browser.current_url)
        
class SbisContactPage(BasePage):
    
    set_partners = {}

    def open_tensor_page(self):
        contact_element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactPageLocators.TENSOR_PAGE_LINK), message="Element not found")
        contact_element.click()
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)        
        return TensorMainPage(browser=self.browser, url=self.browser.current_url)    

    def check_region_and_list_partners(self):
        assert self.find_region_element().text == "Республика Башкортостан"

        self.set_partners = self.find_list_partners()
        
        assert len(self.set_partners) > 0

    def find_region_element(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(SbisContactPageLocators.CHOOSE_REGION))

    def find_list_partners(self):
        partners = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, "contacts_list"))).find_elements(*SbisContactPageLocators.LIST_PARTNERS)    
        
        return {partner.text for partner in partners}


    def change_region(self):
        previos_region = self.find_region_element()        
        previos_region.click()
        new_region = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Камчатский край']")))
                
        ActionChains(self.browser).move_to_element(new_region).click().pause(1).perform()       

    def check_new_region_title_url(self):
        region = self.find_region_element()     
        region_name = region.text
        assert region_name == "Камчатский край"     
        assert self.browser.title == "СБИС Контакты — Камчатский край"
        assert self.browser.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
        previous_partners = self.set_partners
        self.set_partners = self.find_list_partners()        
        assert previous_partners != self.set_partners, f"Партнеры {self.set_partners}"         

class SbisDownloadPage(BasePage):
    def download_plugin_web(self):
        try:
            plugin_element = self.browser.find_element(*SbisDownloadPageLocators.CHOOSEN_PLUGIN_MENU)
        except NoSuchElementException:
            plugin_element = self.browser.find_element(*SbisDownloadPageLocators.CHOOSE_PLUGIN_MENU)
            plugin_element.click()

        link = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe'
        file_name = link.split('/')[-1]
        file_path = os.path.join(os.getcwd(),file_name)    
        
        download_link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"[href='{link}']")), message="Element not found")
        download_link.click()

        file_size_in_site = float(download_link.text.split(" ")[-2])

        time.sleep(10)

        try:
            file_size_in_folder = round(os.path.getsize(file_path) / 1048576, 2)
            os.remove(file_path)
            assert  file_size_in_folder == file_size_in_site, LOGGER.error("Неверные размеры")
        except FileNotFoundError as e:
            LOGGER.error(e)
            raise FileNotFoundError           
            
           
