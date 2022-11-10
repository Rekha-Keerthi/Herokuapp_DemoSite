def example():
    # Click on Fashion menu option from the menu bar
    menu_list = homepage.get_menulist()
    for option in menu_list:
        name = option.text
        if name == "Fashion":
            option.click()
            break

    self.driver.execute_script("window.scrollBy(0,1500);")
