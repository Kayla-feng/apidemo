import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR, 'database','user.int')
# 测试用例py文件目录
Test_Case_DIR = os.path.join(BASE_DIR,'testcases')
# 测试数据文件
Test_Data = os.path.join(BASE_DIR,'data')
# 日志目录
Log_DIR = os.path.join(BASE_DIR,'logs')