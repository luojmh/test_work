#coding:utf-8
import yaml


class Calculator:
    def add(self,a,b):
        return a+b+a

    def div(self,a,b):
        return a/b

    def getdatas(self):
        with open("./data/result.yml") as f:
            datas = yaml.safe_load(f)
        return datas["add"]["add"]
