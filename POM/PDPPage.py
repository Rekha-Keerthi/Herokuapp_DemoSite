from selenium.webdriver.common.by import By


class PDP_Page:

    def __init__(self,driver):
        self.driver = driver

    pdp_product = (By.XPATH,"(//div[@id='altImages']/ul/li/span/span/span/input)[3]")
    close_button = (By.XPATH, "//button[@data-action='a-popover-close']")

    spons_products = (By.XPATH, "(//div[@class='a-carousel-row-inner']//a//span//i//span)[2]")

    def PDP_Image(self):
        return self.driver.find_element(*PDP_Page.pdp_product)

    def close_video(self):
        return self.driver.find_element(*PDP_Page.close_button)

    def sponsered_products(self):
        return self.driver.find_element(*PDP_Page.spons_products)

