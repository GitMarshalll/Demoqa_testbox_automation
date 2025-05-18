import time

from base.base_page import BasePage
from utils.driver import get_driver
from pages.text_box import Text_Box_Page

def test_kirill():
    driver = get_driver("https://demoqa.com/text-box")
    time.sleep(2)
    base_page = BasePage(driver)
    text_box_page = Text_Box_Page(driver)

    username = "Али Алиев"
    email = "ali@mail.com"
    currentadd = "Тошкент, Чилонзор"
    permanentadd = "Юнусобод 9"

    text_box_page.enter_username(username)
    base_page.logger.info("username kiritildi")
    base_page._take_screenshot()

    text_box_page.enter_email(email)
    base_page.logger.info("email kiritildi")
    base_page._take_screenshot()

    text_box_page.enter_currentadd(currentadd)
    base_page.logger.info("currentadd kiritildi")
    base_page._take_screenshot()

    text_box_page.enter_permanentadd(permanentadd)
    base_page.logger.info("permanentadd kiritildi")
    base_page._take_screenshot()

    text_box_page.click_submit_button()


    driver.quit()