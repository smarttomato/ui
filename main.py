import pytest
from configs.config import report_dir
import time
import subprocess

current_time = time.strftime('%Y-%m-%d-%H-%M-%S')
report_name = report_dir + '/interface_autotest_{}'.format(current_time)
pytest.main([
             '-s', '-q',
             '-p', 'no:warnings',
             '--alluredir', report_name,
            ])

# 生成报告
# subprocess.call("allure generate {} -o report/allure_report_{}".format(report_name, current_time), shell=True)