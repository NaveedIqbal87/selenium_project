import time
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import allure



def setup_function():
    global driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.maximize_window()

def teardown_function():
    driver.quit()
def my_credential():
    return[
        ('abdealidodia@gmail.com', 'abdeali@123'),
        ('ali@gmail.com', 'ali@123'),
        ('abdali@gmail.com', 'abd@123')
    ]
@pytest.mark.parametrize("username,password",my_credential())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.ID,"user-name").send_keys(username)
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(2)

