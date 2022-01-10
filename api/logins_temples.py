# -*- coding: utf-8 -*-

import os

from enum import Enum

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")


class Login_api(Enum):
    # 注意不能加逗号
    login = "/api/v1/front/user/loginGovernment"
    dataportlist = "/api/v1/front/open-data/list"
