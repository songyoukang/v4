import time

from  selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from base.get_driver import DriverUtil
from tool.filepath import BASE_DIR, PROJECT_DIR, LC_FILE_PATH, error_file


class Base():
    """基类"""
    def __init__(self,driver):
         self.driver=driver
        # self.driver=webdriver.Chrome()
    #查找元素方法"""
    def base_find_element(self,loc,timeout=30):
       return WebDriverWait(self.driver,timeout=timeout,poll_frequency=0.5).until(lambda x:x.find_element(*loc))
    #"""点击方法"""
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
    #获取本文方法
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    #截图方法
    def base_get_img(self):
        self.driver.get_screenshot_as_file("../../v4/xiangcun_img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
    #验证码
    def base_code(self, loc):
       return self.base_find_element(loc)
    #元素是否存在

