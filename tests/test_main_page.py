from assertpy import assert_that
from pages.main_page import MainPage


def logo_present(browser):
    main_page = MainPage(browser)
    main_page.loadPage()
    main_page.logo() == True