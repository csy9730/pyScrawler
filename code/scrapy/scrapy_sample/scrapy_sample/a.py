#-*- coding: UTF-8 -*-
from urllib.request import urlretrieve
import requests
import os

"""
函数说明:下载《英雄联盟盒子》中的英雄图片

Parameters:
    heros_url - GET请求地址，通过Fiddler抓包获取
    header - header信息
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_imgs_download(heros_url,header):
    req = requests.get(url = heros_url, headers = header).json()
    hero_num = len(req['list'])
    print('一共有%d个英雄' % hero_num)
    hero_images_path = 'images'
    for each_hero in req['list']:
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'
        filename = hero_images_path + '/' + hero_name
        if hero_images_path not in os.listdir():
            os.makedirs(hero_images_path)
        urlretrieve(url = hero_photo_url, filename = filename)

if __name__ == '__main__':   
    headers = {'Accept-Charset': 'UTF-8',
            'Accept-Encoding': 'gzip,deflate',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Host': 'gamehelper.gm825.com'}
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    hero_imgs_download(heros_url,headers)