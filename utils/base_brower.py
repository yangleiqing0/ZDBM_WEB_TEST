from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


class BaseBrowser:

    def __init__(self, driver):
        self.interval_time = 15
        if isinstance(driver, str):
            if driver.lower() == "chrome":
                self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(self.interval_time)

    def by_id(self, _id):
        return self.driver.find_element_by_id(_id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_names(self, name):
        return self.driver.find_elements_by_name(name)

    def by_xpath(self, xpath, t=1):
        count = 10
        if t:
            time.sleep(t)
        while count > 0:
            try:
                return self.driver.find_element_by_xpath(xpath)
            except ElementClickInterceptedException:
                time.sleep(1)
                count -= 1
                continue
        raise ElementClickInterceptedException

    def by_xpaths(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def get(self, url, t=0):
        if t:
            self.driver.get(url)
        return self.driver.get(url)

    def is_has(self, content, css="p", xpath=False):
        try:
            if xpath:
                self.by_xpath(content)
            else:
                self.by_xpath("//{}[text()='{}']".format(css, content))
            return True

        except NoSuchElementException:
            return False

    def wait_for(self, seconds, fuc, *args, **kwargs):
        count = seconds//self.interval_time + 1
        while count > 0:
            if fuc(*args, **kwargs):
                return True
            count -= 1
            self.driver.refresh()
        return False

    def until_for(self, seconds, fuc, *args, **kwargs):
        count = seconds // self.interval_time + 1
        while count > 0:
            if fuc(*args, **kwargs):
                return True
            count -= 1
        return False

    @staticmethod
    def clear(element):
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)

    @staticmethod
    def sleep(t):
        time.sleep(t)
