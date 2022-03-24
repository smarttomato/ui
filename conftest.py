import pytest
from selenium import webdriver
from configs.config import driver_dir
import os
import time


@pytest.fixture(scope="class")
def chrome_driver():
    driver = webdriver.Chrome(executable_path=driver_dir+os.sep+"chromedriver")
    yield driver
    time.sleep(1)
    driver.close()
    driver.quit()

