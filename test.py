from selenium.webdriver.common.by import By
from .pages.sbis_pages import SbisMainPage


def test_case_1(browser):
    link = "https://sbis.ru/"
    sbis_main_page = SbisMainPage(browser, link)
    sbis_main_page.open()
    sbis_main_page.open_contact_menu()
    sbis_contact_page = sbis_main_page.open_contact_page()
    tensor_main_page = sbis_contact_page.open_tensor_page()    
    tensor_main_page.should_be_power_in_people_blog()
    tensor_about_page = tensor_main_page.open_about_page()   
    tensor_about_page.check_url()
    tensor_about_page.check_size_images()

def test_case_2(browser):
    link = "https://sbis.ru/"
    sbis_main_page = SbisMainPage(browser, link)
    sbis_main_page.open()
    sbis_main_page.open_contact_menu()
    sbis_contact_page = sbis_main_page.open_contact_page()
    sbis_contact_page.check_region_and_list_partners()
    sbis_contact_page.change_region()
    sbis_contact_page.check_new_region_title_url()

def test_case_3(browser):
    link = "https://sbis.ru/"
    sbis_main_page = SbisMainPage(browser, link)
    sbis_main_page.open()
    sbis_download_page = sbis_main_page.open_download_page()
    sbis_download_page.download_plugin_web()
    

      
