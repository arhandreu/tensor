from selenium.webdriver.common.by import By

class TensorMainPageLocators():
    POWER_IN_PEOPLE_BLOG = (By.XPATH, "//p[text()='Сила в людях' and @class='tensor_ru-Index__card-title tensor_ru-pb-16']")
    LINK_ABOUT_PAGE = (By.CSS_SELECTOR, "a[href='/about']")


class TensorAboutPageLocators():
    CHAPTER_WORK = (By.CLASS_NAME, "tensor_ru-container.tensor_ru-section.tensor_ru-About__block3")


class SbisMainPageLocators():
    CONTACT_MENU_LINK = (By.CSS_SELECTOR, "div.sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover")
    CONTACT_PAGE_LINK = (By.CSS_SELECTOR, "div.sbisru-Header-ContactsMenu__items.sbisru-Header-ContactsMenu__items-visible a.sbisru-link.sbis_ru-link")
    DOWNLOAD_PAGE_LINK = (By.CSS_SELECTOR, "a.sbisru-Footer__link[href='/download']")


class SbisContactPageLocators():
    TENSOR_PAGE_LINK = (By.CSS_SELECTOR, "a[title='tensor.ru']")
    CHOOSE_REGION = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative span.sbis_ru-Region-Chooser__text.sbis_ru-link")
    LIST_PARTNERS = (By.CSS_SELECTOR,"div[data-qa='item'] div.sbisru-Contacts-List__name.sbisru-Contacts-List--ellipsis.sbisru-Contacts__text--md.pb-4.pb-xm-12.pr-xm-32")


class SbisDownloadPageLocators():
    CHOOSEN_PLUGIN_MENU = (By.CSS_SELECTOR, ".controls-Checked__checked[data-id='plugin']")
    CHOOSE_PLUGIN_MENU = (By.CSS_SELECTOR, "[data-id='plugin']")