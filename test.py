﻿# coding: utf-8
'''
Created on 2012-7-3

@author: lihao
'''
import top.api

'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了

'''
top.setDefaultAppInfo("25623067", "441fe0124c3ec4f0c0fc2b4b030b0d17")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com",80)

使用自定义的域名（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com")

使用默认的配置（调用线上环境）
a = top.api.UserGetRequest()

'''
a = top.api.TbkUatmFavoritesGetRequest()


'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(top.appinfo("25623067","441fe0124c3ec4f0c0fc2b4b030b0d17"))
'''


a.fields="favorites_title,favorites_id,type"

try:
    f= a.getResponse()
    print(f)
except Exception,e:
    print(e)

