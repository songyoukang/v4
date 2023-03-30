from base.base import Base
from page.page_login import Page_login
from page.page_xxfb import Page_xxfb


class Page_in(Base):
    def __init__(self,driver):
         self.driver=driver
    #获取登录对象
    def get_page_login(self):
        return Page_login(self.driver)
    #获取信息发布对象
    def get_page_xxfb(self):
        return Page_xxfb(self.driver)
