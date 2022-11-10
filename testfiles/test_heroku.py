import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from POM.HerokuPage import Heroku_Page
from utilities.Baseclass import BaseClass


class Test_Herokuapp(BaseClass):

    def test_e2eheroku(self):
        #log = self.getLogger()

        heroku_obj = Heroku_Page(self.driver)

        page_list = heroku_obj.get_checkbox()
        for item in page_list:
            actions = ActionChains(self.driver)
            if item.text == "Checkboxes":
                item.click()

                checkboxes = heroku_obj.Check_checkbox()
                for checkbox in checkboxes:
                    checkbox.click()
                time.sleep(4)
                self.driver.back()

                continue
            elif item.text == "Context Menu":
                item.click()

                actions.context_click(heroku_obj.Context_Menu()).click().perform()
                alert_popup = self.driver.switch_to.alert
                print(alert_popup.text)
                alert_popup.accept()
                self.driver.refresh()
                self.driver.back()

                continue
            elif item.text == "Drag and Drop":
                item.click()
                self.driver.back()
                continue

            elif item.text == "Dropdown":
                item.click()
                dropdown_options = Select(heroku_obj.get_dropdown())

                dropdown_options.select_by_visible_text("Option 2")
                self.driver.implicitly_wait(2)
                dropdown_options.select_by_index(1)
                self.driver.back()
                continue

            elif item.text == "Dynamic Controls":
                item.click()
                self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
                time.sleep(2)
                self.driver.find_element(By.XPATH,"//button[text()='Remove']").click()
                self.driver.implicitly_wait(5)
                assert "gone!" in heroku_obj.dynamic_controls().text
                print(heroku_obj.dynamic_controls().text)
                self.driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button").click()
                self.driver.find_element(By.CSS_SELECTOR,"form[id='input-example'] button").click()
                time.sleep(5)
                self.driver.find_element(By.CSS_SELECTOR,"form[id='input-example'] input").send_keys("Rekha Keerthi")
                self.driver.find_element(By.CSS_SELECTOR, "form[id='input-example'] button").click()
                break
        #self.driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")


