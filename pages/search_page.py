from selenium.webdriver.common.by import By


class SearchPage:
    # locators
    HOTELS = (By.ID, "farefinder-option-hotels")
    CARS = (By.ID, "farefinder-option-cars")
    FLIGHTS = (By.ID, "farefinder-option-flights")
    BUNDLES = (By.ID, "farefinder-option-bundles")

    # URL
    URL = "https://www.hotwire.com/"

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def click_hotels(self):
        self.browser.find_element(*self.HOTELS).click()

    def click_cars(self):
        self.browser.find_element(*self.CARS).click()

    def click_flights(self):
        self.browser.find_element(*self.FLIGHTS).click()

    def click_bundles(self):
        self.browser.find_element(*self.BUNDLES).click()
