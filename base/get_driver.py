from selenium import webdriver
class DriverUtil():
    """获取浏览器对象"""
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome() #定义chrome浏览器驱动
            cls.driver.get("https://digitalvillagecs.szrcbank.com/") #定义访问环境地址
            cls.driver.maximize_window() #窗口最大化
            cls.driver.implicitly_wait(10) #隐式等待10s

        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None
if __name__ == '__main__':
    # DriverUtil().get_driver()
    # sleep(2)
    # # DriverUtil().login()
    # DriverUtil().quit_driver()
    DriverUtil.get_driver()

