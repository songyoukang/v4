import time

import page
from base.base import Base
import urllib.request
import ddddocr
from tool.filepath import LC_FILE_PATH
ocr = ddddocr.DdddOcr()
class Page_xxfb(Base):
    """页面层"""
    #点击公共服務
    def page_button_gongongfuwu(self):
        self.base_click(page.gonggongfuwu_loc)
    def page_button_tongzhigongao(self):
        self.base_click(page.tongzhigongao_loc)
    def page_button_xinxifabu(self):
        self.base_click(page.xinxifabu_loc)
    def page_create(self):
        self.base_click(page.create_loc)
    #获取异常信息
    def page_info_text(self):
        self.base_get_text(page.tongzhigongao_loc)
    #页面截图
    def page_image(self):
        self.base_get_img()

    def page_element_exist(self):
       return self.base_check_element_exist()
    #刷新页面
    def page_refresh(self):
        self.driver.refresh()

    # 元素是否存在
    def page_check_element_exist(self):
        try:
            self.base_find_element(page.login_info, timeout=2)
            return True
        except:
            return False


    #组合业务
    def page_xxfb(self):

        self.base_click(page.gonggongfuwu_loc)

        self.base_click(page.tongzhigongao_loc)

        self.base_click(page.xinxifabu_loc)
        time.sleep(3)
        self.base_click(page.create_loc)