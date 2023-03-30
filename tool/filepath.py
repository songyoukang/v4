import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 获取当前base路径
PROJECT_DIR = os.path.join(BASE_DIR,"v4")
LC_DIR = os.path.join(PROJECT_DIR, "xiangcun_img")

error_file = os.path.join(PROJECT_DIR, "error.png")
LC_FILE_PATH =os.path.join(LC_DIR, "img.png")
print(LC_FILE_PATH)
print(error_file)