# -*- coding: utf-8 -*-

# @Author : qishan

import  json as jn
import requests
from common.logger import Logger
from base.get_path import Settings
from api.logins_temples import Login_api
from base.base_url import Base_URL
from base.env_config import ENV_CONF




class RequestsMethod():
    def __init__(self):
        self.session = requests.session()
        self.root_url = Base_URL().get_base_url()


    # 封装get 请求
    def get(self, url, headers=None, params=None, **kwargs):
        return requests.get(url=url, headers=headers, params=params)

    # 封装post 请求
    def post(self,url,headers=None,data=None,**kwargs):
        return requests.post(url= url,headers = headers ,json = data)

    """
    这里再给出一个方案，当请求封装的请求方式不够用的时候，我们提供了request 方法，为了让使用人可以自己封装
    """

    def request(self,url,method,data= None,json = None,**kwargs):
        url = self.root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files") # 文件上传和下载
        cookies = dict(**kwargs).get("cookies")

        self.request_log(url,method,data,json,params,headers,files,cookies)

        if method == "GET":
            return self.session.get(url,**kwargs)
        if method == "POST":
            return self.session.get(url,data,json,**kwargs)
    #登录请求
    def logins(self):
        login_api = Login_api.login.value
        root_base = Base_URL().get_base_url()
        url = root_base + login_api

        data =  {
        "authCode":ENV_CONF.userinfo.authcode, # 要和后端约定好一个，方便后面的接口关联
        "password": ENV_CONF.userinfo.password,
        "userName": ENV_CONF.userinfo.username,

        }
        return requests.post(url= url ,json = data)



    def request_log(self,url,method,data = None,json = None,headers = None,files = None, cookies = None ,**kwargs):
        logger.info("请求地址-->{0}".format(url))
        logger.info("请求方法-->{0}".format(method))
        logger.info("请求头-->{0}".format(jn.dumps(headers,indent=4,ensure_ascii=False)))



# resquestmothed = RequestsMethod()


