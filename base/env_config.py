# -*- encoding: utf-8 -*-
"""
@File    :  env_config.py

"""

import configparser
import logging
import os
import sys
from functools import lru_cache

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

base_dir = os.path.dirname(os.path.dirname(__file__))
envfile = os.environ.get("env_file")
logger = logging.getLogger(__name__)


class BASE_URL:
    base_url: str = ""


class USERINFO:
    username: str = ""
    password: str = ""
    authcode: str = ""


class ENV_VARS:

    def __init__(self):
        # 要与ini配置文件一一对应
        self.base_url = BASE_URL()
        self.userinfo = USERINFO()
        #这是一个对象 将io转为类的对象 可以使用 . 调用
        generate_env_instances()


@lru_cache()
def read_conf_file():
    """
    读取配置文件
    """
    env_file_path = "{}/{}".format(base_dir, envfile)
    cf = configparser.ConfigParser()
    cf.read(env_file_path)
    return cf


def set_attr(clz, f_dict):
    for k, v in f_dict.items():
        setattr(clz, k, v)
    return clz


def generate_env_instances():
    """
    将配置文件转化为类对象
    """
    env_confs = read_conf_file()
    for section in env_confs.sections():
        model_name = section
        values = env_confs.items(model_name)
        value_dict = dict(values)
        model_obj = getattr(sys.modules[__name__], model_name.upper())
        set_attr(model_obj, value_dict)


@lru_cache()
def generate_obj():
    env_vars = ENV_VARS()
    logger.info("读取的环境参数为：{}".format(env_vars.__dict__))
    return env_vars


ENV_CONF = generate_obj()

print("环境配置文件为 ：{}".format(envfile))
print("base_url :{}".format(ENV_CONF.base_url.base_url))
print(ENV_CONF.userinfo.username)
# print(os.environ.get("env_file"))
