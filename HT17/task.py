from pathlib import Path
import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

from read_csv_order import data_order


class RobotPlacer:
    dir = f'{Path.cwd()}/output'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    url = 'https://robotsparebinindustries.com/'

    def __int__(self):
        self.driver = self.__init_driver()

    def placer_order_robot(self, order):
        self.open_site()  # open site
        self.click_button('[class="nav-link"]')  # move Order your robot

        for data in order:
            print(data)
            self.click_button('.btn-dark')  # close pop-up click "ok"
            self.fill_order(data)
            self._wait_for_element('[id="preview"]').click()
            self.go_order()  # go_order (click button)
            self.screenshot_preview(self.number_check())  # save check
            self._wait_for_element('[id="order-another"]').click()  # next order

    def open_site(self):
        self.driver.get(self.url)
        self._wait_for_element('.nav-link')

    def click_button(self, selector: str):
        elem = self._wait_for_element(selector)
        elem.click()
        return elem

    def fill_order(self, params: list):
        # head
        head_field = self._wait_for_element('[id="head"]')
        head_field.click()
        for _ in range(int(params[1])):
            head_field.send_keys(Keys.ARROW_DOWN)
        head_field.send_keys(Keys.ENTER)
        # body
        body_field = self._wait_for_element(f'[for="id-body-{params[2]}"]')
        body_field.click()
        # legs
        legs_field = self._wait_for_element('[type="number"]')
        legs_field.click()
        legs_field.send_keys(params[3])
        legs_field.send_keys(Keys.ENTER)
        # address
        address_field = self._wait_for_element('[type="text"]')
        address_field.click()
        address_field.send_keys(params[4])
        address_field.send_keys(Keys.ENTER)

    def screenshot_preview(self, name):
        p = f'{Path.cwd()}/output'
        preview = self._wait_for_element('[id="robot-preview-image"]')
        preview.screenshot(str(Path(p, f'{name}_preview.png')))

    def go_order(self):
        self._wait_for_element('[id="order"]').click()
        try:
            self._wait_for_element('.alert-danger', timeout=0)
        except TimeoutException:
            self._wait_for_element('[id="parts"]')
        else:
            self.go_order()

    def number_check(self):
        selector = self._wait_for_element('.badge-success')
        number = selector.text.split('-')[-1]
        return number

    def _wait_for_element(self, selector: str, by: By = By.CSS_SELECTOR, timeout: int = 10) -> WebElement:
        condition = EC.presence_of_element_located((by, selector))
        element = WebDriverWait(self.driver, timeout).until(condition)
        return element

    def __enter__(self):
        self.driver = self.__init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def __init_driver(self):
        service = Service(ChromeDriverManager().install())
        browser_options = ChromeOptions()
        service_args = [
            '--start-maximized',
            '--no-sandbox',
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--hide-scrollbars',
            '--disable-setuid-sandbox',
            '--profile-directory=Default',
            '--ignore-ssl-errors=true',
            '--disable-dev-shm-usage'
        ]
        for arg in service_args:
            browser_options.add_argument(arg)

        browser_options.add_experimental_option(
            'excludeSwitches', ['enable-automation']
        )
        browser_options.add_experimental_option('prefs', {
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_settings.popups': 0
            })

        driver = Chrome(service=service, options=browser_options)
        return driver


if __name__ == '__main__':
    with RobotPlacer() as placer:

        placer.placer_order_robot(data_order)
