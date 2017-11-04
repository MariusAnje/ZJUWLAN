#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Kt Qiu
# @Time     : 17/11/1 0:07
# @Contact  : kitty666ball@gmail.com
# @GitHub   : https://github.com/KtQiu

import urllib
from urllib import parse, request
import socket
import os
import subprocess
import time
import re


class ZJUWIFI:
    def __init__(self):
        # 自己填写自己的账号和密码
        self.userid = 'xxxxxxxxx'
        self.passwd = 'xxxxxxxxx'
        self.ip_pre = '10.189'

    def login(self):
        print('正在认证浙大无线网.....')
        data = {
            'action': 'login',
            'username': self.userid,
            'password': self.passwd,
            'ac_id': '3',
            'user_ip': '',
            'nas_ip': '',
            'user_mac': '',
            'save_me': '0',
            'ajax': '1',
        }
        headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'en - US, en;q = 0.9, zh - CN;q = 0.8, zh;q = 0.7',
            'Connection': 'keep - alive',
            'Content - Length': '103',
            'Content - Type': 'application/x-www-form-urlencoded',
            'Host': 'net.zju.edu.cn',
            'Origin': 'https: // net.zju.edu.cn',
            'Referer': 'https://net.zju.edu.cn/srun_portal_pc.php?&ac_id=3',
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
            'X - Requested - With': 'XMLHttpRequest',
        }
        post_data = parse.urlencode(data).encode()
        login_url = 'https://net.zju.edu.cn/srun_portal_pc.php?&ac_id=3'
        req = request.Request(login_url, post_data, headers)
        respon = request.urlopen(req)
        content = respon.read().decode('gbk')
        self.getResultLogin(content)

        # isconnect = self.isConnect()
        # if not isconnect:
        #     print('ZJUWLAN可以上网了！不需要去认证登录！')
        # else:
        #     print('发现ZJUWLAN还暂时不能上网...')
        #     print('正在认证浙大无线网.....')
        #     data = {
        #         'action': 'login',
        #         'username': self.userid,
        #         'password': self.passwd,
        #         'ac_id': '3',
        #         'user_ip': '',
        #         'nas_ip': '',
        #         'user_mac': '',
        #         'save_me': '0',
        #         'ajax': '1',
        #     }
        #     headers = {
        #         'Accept': '* / *',
        #         'Accept - Encoding': 'gzip, deflate, br',
        #         'Accept - Language': 'en - US, en;q = 0.9, zh - CN;q = 0.8, zh;q = 0.7',
        #         'Connection': 'keep - alive',
        #         'Content - Length': '103',
        #         'Content - Type': 'application/x-www-form-urlencoded',
        #         'Host': 'net.zju.edu.cn',
        #         'Origin': 'https: // net.zju.edu.cn',
        #         'Referer': 'https://net.zju.edu.cn/srun_portal_pc.php?&ac_id=3',
        #         'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        #         'X - Requested - With': 'XMLHttpRequest',
        #     }
        #     post_data = parse.urlencode(data).encode()
        #     login_url = 'https://net.zju.edu.cn/srun_portal_pc.php?&ac_id=3'
        #     req = request.Request(login_url, post_data, headers)
        #     # Res = self.isConnect()
        #     # if not Res:
        #     #     print("Login successfully!")
        #     # else:
        #     #     print("False:(  Plz try again!")
        #     respon = request.urlopen(req)
        #     content = respon.read().decode('gbk')
        #     self.getResultLogin(content)

            # isconnect = self.isConnect()
            # if not isconnect:
            #     print('ZJUWLAN可以上网了！不需要去认证登录！')
            # else:
            #     print('发现ZJUWLAN还暂时不能上网...')

    def getResultLogin(self, content):
        if 'login_ok' in content:
            print('Login successfully！')
        else:
            print('Something wrong! :( \n Plz try again!')

    # 获取本机无线上网的IP
    def getIP(self):
        local_iP = socket.gethostbyname(socket.gethostname())
        if self.ip_pre in str(local_iP):
            return str(local_iP)
        ip_lists = socket.gethostbyname_ex(socket.gethostname())

        for ip_list in ip_lists:
            if isinstance(ip_list, list):
                for i in ip_list:
                    if self.ip_pre in str(i):
                        return str(i)
            elif isinstance(ip_list, str):
                if self.ip_pre in ip_list:
                    return ip_list

    def isConnect(self):
        # 判断是不是已经连接上ZJUWLAN
        denull = open(os.devnull, 'w')
        result = subprocess.call('ping www.baidu.com', shell=True, stdout=denull, stderr=denull)
        # 关闭设备
        denull.close()
        # 0代表着连接上网络，1代表没有连接上
        return result

    def main(self):
        print('欢迎使用Kitty的ZJUWlan简易登录系统')
        # self.userid = input('请输入账号：')
        # self.passwd = input('请输入密码：')
        # self.login()
        while True:
            nowIP = self.getIP()
            # print(nowIP)
            if not nowIP:
                print('还未连接ZJUWLAN!')
            else:
                print('已连接ZJUWLAN,正在登陆账号密码，请不要关闭！')
                self.login()
                # time.sleep(10)
                return False  # 登陆上就退出程序


ZJULogin = ZJUWIFI()
ZJULogin.main()
