from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(url):
    service = ChromeService(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--force-device-scale-factor=0.70")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver