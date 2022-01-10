# -*- coding: utf-8 -*-


# @Author : qishan


import logging
import os

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings:


    # 获取项目所在的绝对路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 用例模块所在的目录路径
    CASE_DIR = os.path.join(BASE_DIR, "testcases")

    # 用例数据所在的目录路径
    DATA_DIR = os.path.join(BASE_DIR, "testdata")

    # allure xml目录地址
    XML_DIR = os.path.join(BASE_DIR, 'output/xml')

    # 测试报告所在的目录路径
    REPORT_DIR = os.path.join(BASE_DIR, "output/html")

    # 日志文件所在的目录路径
    LOG_DIR = os.path.join(BASE_DIR, "log")

    # 获取项目的配置文件路径
    data_config_path = os.path.join(BASE_DIR, "config/settings.ini")








settings = Settings()



