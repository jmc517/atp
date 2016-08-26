# -*- coding: utf-8 -*-
import json
import os
import requests
from configparser import ConfigParser

class GetData:
    
    def get_request_url(self):
        cf = self.get_app_conf()
        host = str(cf.get('baseconf', 'serverIp'))
        port = str(cf.get('baseconf', 'serverPort'))

        url = 'http://' + host + ':' + port
        return url
    def get_step_all(self):
        r = requests.get(self.get_request_url() + '/atp/steps/all')
        return r.json()

    def get_step_params(self, step):
        res = requests.get(self.get_request_url() + '/atp/steps/params/' + step)
        return res.json()
    def get_feature_all(self):
        res = requests.get(self.get_request_url() + '/atp/features/all')
        return res.json()

    def save_feature(self, data):
        res = requests.post(self.get_request_url() + '/atp/feature/save', json=data)
        print(res.text)

    def get_feature_info(self, scn_name):
        res = requests.get(self.get_request_url() + '/atp/feature/info/' + scn_name)
        print(res.text)
        return res.json()
        # return res.json()

    def get_feature_info_by_id(self, feature_id):
        res = requests.get(self.get_request_url() + '/atp/feature/info/id=' + str(feature_id))
        print(res.text)
        return res.json()

    def get_featrue_step_relationship(self, scen_name):
        res = requests.get(self.get_request_url() + '/atp/feature/featureStepsRelationShip/' + scen_name)

        return res.json()
    def get_step_info_by_id(self, id):
        res = requests.get(self.get_request_url() + '/atp/steps/info/' + str(id))
        return res.json()
    def del_feature(self, feature_id):
        res = requests.get(self.get_request_url() + '/atp/feature/del/' + str(feature_id))
        return res.json()

    def save_task_history(self, data):
        res = requests.post(self.get_request_url() + '/atp/task/save', json=data)
        # print(res.json())
        return res.json()

    def get_task_history(self):
        res = requests.get(self.get_request_url() + '/atp/task/all')
        return res.json()

    def update_task_status(self, id):
        res = requests.get(self.get_request_url() + '/atp/task/status/update/' + str(id))
        return res.json()

    def get_app_conf(self):
        # 获取当前用户目录
        curUserDir = os.path.expanduser('~')
        # 读取用户工程路径位置
        appConfigPath = os.path.join(curUserDir, '.atp.ini')
        if not os.path.exists(appConfigPath):
            raise Exception('应用配置文件不存在， 请先设置应用配置')

        cf = ConfigParser()
        cf.read(appConfigPath)
        return cf

getter = GetData()

