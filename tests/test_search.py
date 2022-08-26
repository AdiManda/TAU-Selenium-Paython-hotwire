from pages.search_page import SearchPage

def test_search_hotels(browser):
    check_hotels = SearchPage(browser)
    check_hotels.loadPage()
    check_hotels.click_hotels()

def test_search_cars(browser):
    check_cars = SearchPage(browser)
    check_cars.loadPage()
    check_cars.click_cars()

def test_search_flights(browser):
    check_flights = SearchPage(browser)
    check_flights.loadPage()
    check_flights.click_flights()

def test_search_bundles(browser):
    check_bundles = SearchPage(browser)
    check_bundles.loadPage()
    check_bundles.click_bundles()
