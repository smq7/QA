from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    def test_rozetka_search(self):
          search_request = 'игрушки'
          url = 'https://www.moyo.ua/ua/'

          browser = webdriver.Chrome(ChromeDriverManager().install())
          browser.implicitly_wait(10)

          browser.get(url)

          browser.find_element_by_css_selector('[name="q"]').send_keys(search_request)
          browser.find_element_by_css_selector('[name="q"]').send_keys(Keys.ENTER)
          
          actualResult = browser.find_element_by_css_selector('[class="search_title"]').text
          expectedResult = 'Результати пошуку : '+ search_request
          assert expectedResult in actualResult

          browser.close()

