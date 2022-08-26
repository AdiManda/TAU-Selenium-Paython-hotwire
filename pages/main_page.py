from selenium.webdriver.common.by import By


class MainPage:
    # locators
    LOGO = (By.ID, "hotwire-logo")
    # CARS = (By.ID, "farefinder-option-cars")
    # FLIGHTS = (By.ID, "farefinder-option-flights")
    # BUNDLES = (By.ID, "farefinder-option-bundles")

    # URL
    URL = "https://www.hotwire.com/"

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def logo(self):
        self.browser.find_element(*self.LOGO)

