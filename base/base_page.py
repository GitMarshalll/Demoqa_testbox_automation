import logging
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self._configure_logging()

    # ---------------- Asosiy funksiyalar ----------------

    def click(self, locator):
        element = self._element_to_be_clickable(locator)
        self._scroll_to_element(element)
        self._click(element)

    def input_text(self, locator, text):
        element = self._visibility_of_element_located(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self._visibility_of_element_located(locator)
        return element.text

    def wait_for_element_visible(self, locator):
        return self._visibility_of_element_located(locator)

    # ---------------- Yordamchi funksiyalar ----------------

    def _click(self, element):
        element.click()

    def _element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator))

    def _visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator))

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def _take_screenshot(self, file_name=None):
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")
        if not file_name:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"screenshots/screenshot_{timestamp}.png"
        else:
            file_name = f"screenshots/{file_name}.png"
        self.driver.save_screenshot(file_name)
        self.logger.info(f"Screenshot saved: {file_name}")

    def _configure_logging(self):
        if not os.path.exists("logs"):
            os.mkdir("logs")

        self.logger = logging.getLogger("BasePageLogger")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler("logs/test_log.txt")
            formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)