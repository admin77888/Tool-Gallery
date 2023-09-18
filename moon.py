import requests
import os
import socket
import time


def domain_scanner(domain_name, is_scanning=False):
    if is_scanning:
        print('----正在扫描，请稍后----')
        print('----天启实验室----')



if __name__ == '__main__':
    domain_name = input("请输入你需要查询的域名：")
    domain_scanner(domain_name, is_scanning=True)
    for zym_data in open(r'C:\Users\Administrator\Desktop\子域名爆破1.0\dic.txt'):
        zym_data = zym_data.replace('\n', '')
        url = zym_data + '.' + domain_name
        try:
            ip = socket.gethostbyname(url)
            print(url + '-->' + ip)
            time.sleep(0.1)
        except Exception as e:
            pass
