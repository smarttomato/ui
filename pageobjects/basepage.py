from selenium import webdriver
from configs.config import img_dir, driver_dir
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyzbar.pyzbar as pyzbar
from PIL import Image


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def add_cookies(self, cookies):
        # print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    # 等待元素存在
    def wait_elePresence(self, locator, by=By.XPATH, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((by, locator)))

    # 等待元素可见
    def wait_eleVisible(self, locator, by=By.XPATH, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((by, locator)))

    # 查找并返回一个元素
    def get_element(self, locator, by=By.XPATH, wait_time=10):
        try:
            self.wait_eleVisible(locator, by, wait_time)
            ele = self.driver.find_element(by, locator)
            return ele
        except TimeoutError as e:
            raise e

    # 查找并返回多个元素
    def get_elements(self, locator, by=By.XPATH, wait_time=10):
        try:
            self.wait_eleVisible(locator, by, wait_time)
            ele = self.driver.find_elements(by, locator)
            return ele
        except TimeoutError as e:
            raise e

    # 向下滑动页面至元素可见
    def move_to_ele(self, locator, by=By.XPATH, height=100):
        js = 'window.scrollBy(0,{})'.format(height)
        ActionChains(self.driver).move_to_element(self.driver.find_element(by, locator)).perform()
        self.wait_eleVisible(locator=locator, by=by)
        self.driver.execute_script(js)

    # 滚动至页面最顶部
    def move_to_top(self):
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    # 滚动至页面最底部
    def move_to_bottom(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)

    # 切换页面并获取当前页url
    def get_new_page_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_page_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return new_page_url

    # 解析二维码
    def read_qrcode(self, img_file):
        img = Image.open(img_dir+'/'+img_file)
        return pyzbar.decode(img)[0].data.decode('utf-8')

    # 保存图片
    def save_img(self, img_name):
        self.driver.save_screenshot(img_dir+'/'+img_name)


if __name__ == '__main__':
    pass