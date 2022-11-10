from selenium.webdriver.common.by import By

from POM.PLPPage import PLP_Page


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    bestseller = (By.LINK_TEXT,"Best Sellers")
    menuoptions = (By.XPATH,"//div[@id='nav-xshop']//a")


    def Best_Sellers(self):
        self.driver.find_element(*HomePage.bestseller).click()
        plp_page = PLP_Page(self.driver)
        return plp_page

    def get_menulist(self):
        return self.driver.find_elements(*HomePage.menuoptions)
