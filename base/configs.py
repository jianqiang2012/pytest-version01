# -*- coding: utf-8 -*-
# @Author : qishan

import jsonpath

from base.base_request import RequestsMethod

"""
这里要注意 当登录要验证码的时候 请和后端接口的同学商量怎么给你验证码 机器识别不可能那么准确

"""


# @pytest.fixture(scope="ssesion")
def get_token():
    response = RequestsMethod().logins()
    # 如果返回的是个json 这里就需要转了 如果不是那就转成 json格式
    # response =res.json()
    if response == True:
        access_token = jsonpath.jsonpath(response, "$..{}".format("token"))  # jsonpath 语法

    else:
        # response = RequestsMethod().logins()

        access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiIwNTQ3ODk2MDZhMWI0ZjY5YTZkYjk0MGVkMjM0YzY1YSIsInN1YiI6ImFkbWluIiwiaXNzIjoiMDk4ZjZiY2Q0NjIxZDM3M2NhZGU0ZTgzMjYyN2I0ZjYiLCJpYXQiOjE2NDE3ODUzODAsImF1ZCI6InJlc3RhcGl1c2VyIiwiZXhwIjoxNjQxNzg4OTgwLCJuYmYiOjE2NDE3ODUzODB9.At-rbpnWXIJrd2mLgXf239BWxJJlp4m1rzo8BagCovU"

    return access_token
