import time

from selenium.webdriver import ActionChains

from POM.Homepage import HomePage
from utilities.Baseclass import BaseClass


class TestExcersie(BaseClass):

    def test_e2eflow(self):
        log = self.getLogger()
        # creating object for HomePage page object class
        homepage = HomePage(self.driver)
        plp_pages = homepage.Best_Sellers()
        log.info("Fetching the PLP page")

        bags_wallet = plp_pages.BagsWallet()

        self.driver.implicitly_wait(5)
        for bags in bags_wallet:
            pla_pages = bags.text

            if pla_pages == "Bags, Wallets and Luggage":

                bags.click()
                break



        product_search = plp_pages.search_product()


        for product in product_search:
            product_name = product.text
            #print(product_name)

            if product_name == "NAPA HIDE Tan Crunch Leather Wallet for Men":

                product.click()
                time.sleep(3)
                pdp_product = plp_pages.select_product()
                action = ActionChains(self.driver)
                action.move_to_element().perform()

                pdp_product.PDP_Image().click()
                pdp_product.close_video().click()
                time.sleep(3)
                self.driver.execute_script("window.scrollBy(0,800);")
                pdp_product.sponsered_products().click()

                break















