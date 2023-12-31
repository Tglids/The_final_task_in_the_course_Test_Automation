from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math


class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_url(self):
        return self.browser.current_url

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = int(alert.text.split(" ")[2])
        try:
            res = str(math.log(abs((12 * math.sin(float(x))))))
            print(f"Your code: {res}")
            alert.send_keys(res)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            return False
        return True

