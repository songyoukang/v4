import time

import page
from base.base import Base
import urllib.request
import ddddocr
from tool.filepath import LC_FILE_PATH
ocr = ddddocr.DdddOcr()
class Page_login(Base):
    """页面层"""
    #输入用户名
    def page_input_name(self,username):
        self.base_input(page.login_name,username )
    #输入密码
    def page_input_password(self, passwd):
        self.base_input(page.login_passwd,passwd)
    #输入验证码
    def page_input_code(self):
        #识别验证码
        pic = self.base_code(page.login_code_img)
        # 获取验证码的src属性
        pic_url = pic.get_attribute('src')
        # 保存验证码图片到指定路径
        urllib.request.urlretrieve(pic_url, LC_FILE_PATH)
        with open(LC_FILE_PATH, 'rb') as f:
            img_bytes = f.read()
        code = ocr.classification(img_bytes)
        print(code)
        #输入
        self.base_input(page.login_code,code)
    #点击登录
    def page_button(self):
        self.base_click(page.login_button)
    #获取异常信息
    def page_info_text(self):

        return self.base_get_text(page.login_info)
    #页面截图
    def page_get_img(self):
        self.base_get_img()
    #刷新页面
    def page_refresh(self):
        self.driver.refresh()
    #元素是否存在
    def page_check_element_exist(self):
        try:
            self.base_find_element(page.login_info,timeout=2)
            return True
        except:
            return False
    #登录组合业务
    def page_login(self,username,passwd):
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_input_code()
        self.page_button()
    #信息发布 调用登录组合业务
    def page_login_xxfb(self,username="15606292280", passwd="a1234567"):
        self.page_input_name(username)
        self.page_input_password(passwd)
        time.sleep(3)
        self.page_input_code()
        self.page_button()