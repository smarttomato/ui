from selenium.webdriver.common.by import By
import allure
from pageobjects.basepage import BasePage


@allure.feature("登录")
class TestLogin:

    @allure.story("打开首页")
    def test_open_browser(self, chrome_driver):
        bp = BasePage(chrome_driver)
        chrome_driver.get("https://36kr.com")
        assert bp.get_element(locator="首页", by=By.LINK_TEXT)


