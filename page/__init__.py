"""页面数据元素信息"""
from selenium.webdriver.common.by import By
#login
login_name=By.XPATH,"//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[1]/div/div/input"
login_passwd=By.XPATH,"//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[2]/div/div/input"
login_code_img =By.XPATH,"//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/img"
login_code=By.XPATH,"//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[3]/div/div[1]/input"
login_button= By.XPATH,"//span[contains(text(),'登录')]"
login_info = By.XPATH,'//*[@class="s-userName"]'

#xxfb
gonggongfuwu_loc=By.XPATH,'//span[contains(text(),"公共服务")]'
tongzhigongao_loc =By.XPATH, "//*[@id='app']/section/section/aside/div/div[1]/ul/li[7]/ul/li[1]/div"
xinxifabu_loc =By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/ul/li[7]/ul/li[1]/ul/li[1]/span'
create_loc =By.XPATH, "//span[contains(text(),'新 增')]"
