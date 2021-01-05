# -*- coding: utf-8 -*-
# author:liucong

import base64

import requests

from core.AutoWeb import AutoWeb


# 获取jenkins打包时间及分支信息
def jenkins_lastBuild_info():
    jenkins_url = AutoWeb.get_jenkins_url()
    jenkins_url = jenkins_url + '/api/json'
    username = "XXXX@XXXXX.com"
    password = "XXXXX"
    auth = username + ":" + password
    headers = {"Content-Type": "application/json", 'Connection': 'close',
               "Authorization": "Basic " + base64.b64encode(auth.encode(encoding="utf-8")).decode(encoding='utf-8')}
    response = requests.get(jenkins_url, headers=headers, verify=False)
    res = response.json()
    jenkins_branch = res['displayName']
    last_url = 'http://staging-ops.xxxx.com' + \
               res['lastBuild']['url'].replace('http://jenkins.situdata.com', '') + 'api/json'
    response = requests.get(last_url, headers=headers, verify=False)
    res = response.json()
    timestamp = res['timestamp']

    return jenkins_branch, timestamp
