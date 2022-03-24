from utils.yamlutil import YamlReader
from configs.conf_dir import common_dir
import os


def get_headers(env):
    return YamlReader(common_dir+os.sep+"headers.yaml").get_data()[env]


if __name__ == '__main__':
    print(get_headers("online"))