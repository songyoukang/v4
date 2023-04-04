#定义函数
import yaml
import os
from tool.filepath import PROJECT_DIR


def read_yaml(filename):
    #读取文件路径
    file_path=PROJECT_DIR + os.sep +'data' +os.sep + filename
    print(file_path)
    #定义空列表，组装测试数据
    arr=[]
    #获取文件流
    with open(file_path,'r',encoding='utf-8') as f :
        for datas in yaml.safe_load(f).values():
          arr.append(tuple(datas.values()))
    return arr

if __name__ == '__main__':
    print(read_yaml("login.yaml"))


#获取文件流
