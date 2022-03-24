import datetime
import os

# 目录配置
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_path, "configs")
img_dir = os.path.join(root_path, "images")
common_dir = os.path.join(root_path, "common")
driver_dir = os.path.join(root_path, "driver")
testdata_dir = os.path.join(root_path, "testdata")
testcase_dir = os.path.join(root_path, "testcase")
log_dir = os.path.join(root_path, "logs")
report_dir = os.path.join(root_path, "report")

# 日志配置
log_info = {
    "log_level": "info",
    "log_file": os.path.join(log_dir, datetime.datetime.now().strftime("%Y-%m-%d") + ".log")
}

# url配置
urls = {
    "test": {
        "g7s": {
            "login": "https://g7s.test.chinawayltd.com/"
        }
    }
}

# 数据库配置
xxx_db = {
    'host': '',
    'port': 3306,
    'user': '',
    'password': '',
    'database': '',
}