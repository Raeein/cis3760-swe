import platform
import random
import time

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver


def get_firefox_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("""
                            user-agent=Mozilla/5.0
                            (Windows NT 10.0; Win64; x64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/121.0.0.0 Safari/537.36
                        """.replace("\n", "").replace(" ", ""))
    gecko_driver_path = ''
    if platform.machine() == 'aarch64':
        gecko_driver_path = '/usr/bin/geckodriver-arm'
    else:
        gecko_driver_path = '/usr/bin/geckodriver'
    try:
        service = Service(gecko_driver_path)
        driver = webdriver.Firefox(service=service, options=options)
        driver.execute_script(
            "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"
        )
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        print(f"Error initializing Firefox WebDriver: {e}")
        exit()


def stall_driver(driver: webdriver.Firefox):
    driver.implicitly_wait(random.randint(10, 20))
    time.sleep(random.randint(2, 5))
