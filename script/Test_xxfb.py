import time

from page.page_in import Page_in
from base.get_driver import DriverUtil
import time
class Testxxfb():
    def setup(self):
        # 获取driver
        driver = DriverUtil.get_driver()
        # 获取统一入口类
        self.page_in=Page_in(driver)
        self.page_in.get_page_login().page_login_xxfb()

        self.xxfb = self.page_in.get_page_xxfb()
    def teardown(self):
        DriverUtil.quit_driver()

    def testcreat(self):
        # 调用登录方法
        num=0
        while True:
            if self.xxfb.page_check_element_exist():
                print("登录成功")
                time.sleep(3)
                self.xxfb.page_xxfb()
                assert self.xxfb.page_info_text== "下午好，宋友康，祝你开心每一天！"
                text=self.xxfb.page_info_text()
                print(text)
                break
            else:
                num+=1
                print("验证码识别错误{}次，重新登录".format(num))
                self.xxfb.page_refresh()
                self.page_in.get_page_login().page_login_xxfb()







