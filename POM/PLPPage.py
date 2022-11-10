from selenium.webdriver.common.by import By

from POM.PDPPage import PDP_Page


class PLP_Page:

    def __init__(self,driver):
        self.driver = driver

    bagsandwallets = (By.XPATH, "(//div[@id='zg_left_col2']/div/div/div/div)")
    products = (By.XPATH,"(//div[@id='gridItemRoot']/div/div[2]/div/span/div)")
    products_display = (By.XPATH,"//a[@class='a-link-normal']/span/div")

    def BagsWallet(self):
        return  self.driver.find_elements(*PLP_Page.bagsandwallets)

    def select_product(self):
        self.driver.find_element(*PLP_Page.products_display).click()
        pdp_product = PDP_Page(self.driver)
        return pdp_product

    def search_product(self):
        return self.driver.find_elements(*PLP_Page.products)