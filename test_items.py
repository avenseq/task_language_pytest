import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test_lang():
    def test_l1(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(5)
        button = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
        assert button, "Элемента кнопки добавления в корзину на странице нет"


