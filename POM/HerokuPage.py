from datetime import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Heroku_Page:

    def __init__(self,driver):
        self.driver= driver

    checkbox_link = (By.XPATH,"//div/div[@id='content']/ul/li/a")
    checkbox_page = (By.XPATH,"//form/input")
    context_menu = (By.ID,"hot-spot")
    dropdown = (By.ID,"dropdown")
    dynamiccontrols = (By.XPATH, "//form[@id='checkbox-example']/p")
    entry_ad_close = (By.XPATH,"//p[text()='Close']")
    file_upload = (By.ID, "file-upload")

    def get_checkbox(self):
        return self.driver.find_elements(*Heroku_Page.checkbox_link)

    def Check_checkbox(self):
        return self.driver.find_elements(*Heroku_Page.checkbox_page)

    def Context_Menu(self):
        return self.driver.find_element(*Heroku_Page.context_menu)

    def drag_and_drop(self):
        block_a = self.driver.find_element(By.CSS_SELECTOR, "#column-a")
        block_b = self.driver.find_element(By.CSS_SELECTOR, "#column-b")
        actions = ActionChains(self.driver)
        return actions.drag_and_drop(block_b, block_a).perform()

    def get_dropdown(self):
        return self.driver.find_element(*Heroku_Page.dropdown)

    def dynamic_controls(self):
        return self.driver.find_element(*Heroku_Page.dynamiccontrols)

    def Entry_AD_Close(self):
        return  self.driver.find_element(*Heroku_Page.entry_ad_close)

    def Fil_Upload(self):
        return  self.driver.find_element(*Heroku_Page.file_upload)

