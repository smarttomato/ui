from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from configs.config import urls
from configs.config import driver_dir
from pageobjects.basepage import BasePage
from pageobjects.g7s.login_page import LoginPage
from testdata.g7s.login_data import LoginData
import allure
import os

s = Service(driver_dir + os.sep + "chromedriver")
login_url = urls["test"]["g7s"]["login"]
lp = LoginPage()
ld = LoginData()


@allure.feature("g7s登录")
class TestG7sLogin:
    @allure.story("登录")
    def test_check_content(self, chrome_driver):
        bp = BasePage(chrome_driver)
        chrome_driver.get(login_url)

        with allure.step("输入用户名"):
            bp.get_element(locator=lp.username_xpath, by=By.XPATH).send_keys("youpin_bs10")
        with allure.step("输入密码"):
            bp.get_element(locator=lp.password_xpath, by=By.XPATH).send_keys("ht2A6066")
        with allure.step("登录"):
            bp.get_element(locator=lp.login_button_xpath, by=By.XPATH).click()
        with allure.step("取消蒙层"):
            bp.wait_eleVisible(locator=lp.shadow_cancel_xpath, wait_time=20)
            bp.get_element(locator=lp.shadow_cancel_xpath).click()
        with allure.step("获取机构名称并断言"):
            assert bp.get_element(locator=lp.organization_name_xpath).text.lower() == ld.organization_name
