## \file ../src/suppliers/aliexpress/api/skd/__init__.py
## \file src/suppliers/aliexpress/api/skd/__init__.py
'''
Created on 2012-6-29

@author: lihao
'''
from .api.base import sign



class appinfo(object):
    def __init__(self,appkey,secret):
        self.appkey = appkey
        self.secret = secret

def getDefaultAppInfo():
    pass


def setDefaultAppInfo(appkey,secret):
    default = appinfo(appkey,secret)
    global getDefaultAppInfo
    getDefaultAppInfo = lambda: default

