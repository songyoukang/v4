import pytest

from page.page_in import Page_in
from page.page_login import Page_login
import time
from base.get_driver import DriverUtil
from tool.read_yaml import read_yaml


class Testlogin():
    """业务层"""
    def setup(self):
        #获取driver
        driver=DriverUtil.get_driver()
        #获取统一入口类
        self.login=Page_in(driver).get_page_login()

    def teardown(self):
        DriverUtil.quit_driver()
    @pytest.mark.parametrize("username,passwd",read_yaml("login.yaml"))
    def testlogin(self, username,passwd):
    #调用登录方法
        self.login.page_login(username,passwd)
        if self.login.page_check_element_exist():
            print("登录成功")
            time.sleep(3)
            try:
                assert self.login.page_info_text()=="下午好，宋友康，1祝你开心每一天！"
            except:
                self.login.page_get_img()
        else:
            print("验证码识别错误，重新登录")
            self.login.page_refresh()
            self.testlogin()