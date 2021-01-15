__all__ = ["Session"]

from constants import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Session:
    def __init__(self):
        self.browser = webdriver.Chrome("./chromedriver")
        self.browser.get("https://web.whatsapp.com/")

    def generate_session(self):
        sessionfilename = "session_file.wa"
        print("Waiting for QR code scan", end="... ")
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR)
        print(f'{STRINGS.CHECK_CHAR} Done')
        session = self.browser.execute_script(GET_SESSION)
        with open(sessionfilename, 'w',
                  encoding='utf-8') as sessionfile:
            sessionfile.write(str(session))
        print('Your session file is saved to: ' + sessionfilename)
        self.browser.quit()

    def open_session(self):
        sessionfilename = "session_file.wa"
        session = None
        with open(sessionfilename, "r", encoding="utf-8") as sessionfile:
            try:
                session = sessionfile.read()
            except:
                raise IOError('"' + sessionfilename + '" is invalid file.')
        print("Injecting session", end="... ")
        self._wait_for_presence_of_an_element(SELECTORS.QR_CODE)
        self.browser.execute_script(
            PUT_SESSION,
            session,
        )
        self.browser.refresh()
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR)
        print(f'{STRINGS.CHECK_CHAR} Done')

    def _wait_for_presence_of_an_element(self, selector):
        element = None
        try:
            element = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.presence_of_element_located(selector)
            )
        except:
            pass
        finally:
            return element
