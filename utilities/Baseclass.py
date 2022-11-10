import inspect
import logging
from logging import Logger

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger

    def verfiyproductdisplay(self,text):
        self.wait = WebDriverWait(self.driver,5)
        self.wait.until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,text)))

    def verifydynamiccontrols(self, text):
        self.wait = WebDriverWait(self.driver,6)
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, text)))