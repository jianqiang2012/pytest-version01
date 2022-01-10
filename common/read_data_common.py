# -*- coding: utf-8 -*-

# @Time :  这里是读取文件数据的一些封装
# @Author : qishan
import json
from configparser import ConfigParser

import yaml

from common.logger import Logger

logger = Logger("loggins")()


class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr: str) -> str:
        return optionstr


class ReadFileDataCommon():
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("读取{} ".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        logger.info("读取数据===> {}".format(data))
        return data

    def load_json(self, file_path):
        logger.info("读取{} ".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        logger.info("读取数据===> {}".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("读取{} ".format(file_path))
        conf = ConfigParser()
        data = conf.read(file_path)

        return data
