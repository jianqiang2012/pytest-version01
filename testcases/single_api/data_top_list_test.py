# -*- coding: utf-8 -*-

# @Time :
# @Author : qishan

import allure
import jsonpath
from data.login_data import login_data_assert
from common.logger import Logger
from base.base_request import RequestsMethod
from base.base_url import Base_URL

from base.configs import get_token
from base.base_url import base_request_url
base_url=  Base_URL().get_base_url()
loggger = Logger("data")()
url =base_url +  base_request_url["dataportlist"]


tokens = get_token()
@allure.epic('data')
class TestDataTopList:

    def setup(self):
        pass

    def teardown(self):
        pass

    @allure.title('这是一个list')
    def test_data_top_list_test(self):

        with allure.step('data'):
            data = RequestsMethod.get(self,headers= None,url= url)
            success_ststus = jsonpath.jsonpath(data,"$..{}".format("success"))
            code_status = jsonpath.jsonpath(data,"$..{}".format("code"))
            assert login_data_assert["success"] == success_ststus
            assert login_data_assert["code"] == code_status

