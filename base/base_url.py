# -*- coding: utf-8 -*-


# @Author : qishan

# log = Logger("logins")()
from api.logins_temples import Login_api
from base.env_config import ENV_CONF


class Base_URL:

    def __init__(self):
        pass

    def get_base_url(self):
        base_url = ENV_CONF.base_url.base_url

        return base_url


base_request_url = {
    "dataportlist": Login_api.dataportlist.value

}
