import time
import requests
import json
import re
from urllib.request import urlretrieve
import os

headers = {
    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 8 Lite MIUI/V10.0.8.0.ODTCNFH)",        
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip"
}
def getWeather():
    headers = {"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control":"no-cache",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Host":"d1.weather.com.cn",
    "Connection":"keep-alive",
    "Referer":"http://www.weather.com.cn/weather1d/101280101.shtml",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

    url =  "http://d1.weather.com.cn/weather_index/101280101.html?_=" 
    tm = int(time.time() )
    url = url + str( tm)
    html = requests.get(url, headers=headers)
    content = html.content

    rc = re.compile(b"var cityDZ =({.*});var alarmDZ")
    js = rc.search(  content).groups()
    dct = json.loads(*js)
    return dct
# {'weatherinfo': {'city': '101280101', 'cityname': '广州', 'temp': '29℃', 'tempn': '21℃', 'weather': '多云', 'wd': '西南风转微风',
#  'ws': '<3级', 'weathercode': 'd1', 'weathercoden': 'n1', 'fctime': '201910221800'}} 

def getMiWeather():
    host = { "Host":"weatherapi.market.xiaomi.com" }
    headers.update( host)
    url =  "https://weatherapi.market.xiaomi.com/wtr-v3/weather/all?latitude=23.112111&longitude=113.553917&isLocated=true&locationKey=weathercn%3A101280111&days=15&appKey=weather20151024&sign=zUFJoAR2ZVrDy1vF3D07&romVersion=V10.0.8.0.ODTCNFH&appVersion=10000500&alpha=false&isGlobal=false&device=platina&modDevice=&locale=zh_cn HTTP/1.1"
    html = requests.get(url, headers=headers)
    dct = html.json()
    return dct


def geChelaile():
    host = {"Host":"api.chelaile.net.cn" }
    headers.update( host)
    url =  "https://api.chelaile.net.cn/bus/line!tsfRealInfos.action?sign=AgZKshID7EG9ApVQPI%2Bszw%3D%3D&nw=MOBILE_LTE&language=1&cityId=040&AndroidID=045d9a9cee2c99ea&mac=C2%3A00%3AF3%3A99%3A6B%3A1D&lineStn=020-03220-1%2C020-1416%3B020-02140-1%2C020-1416%3B020-05713-0%2C020-1416%3B020-05710-0%2C020-1416%3B020-04390-1%2C020-16690%3B020-03300-0%2C020-13424%3B020-04370-1%2C020-9260%3B020-05730-1%2C020-9260%3B020-03220-1%2C020-1416%3B020-05713-0%2C020-1416%3B020-02140-1%2C020-1416%3B020-05710-0%2C020-1416%3B020-04360-0%2C020-9814%3B&phoneBrand=Xiaomi&lchsrc=icon&udid=9fd7f400-3b90-4516-9457-dc919f08248e&system_push_open=1&deviceType=MI+8+Lite&geo_type=gcj&push_open=1&sv=8.1.0&geo_lac=550.0&first_src=app_xiaomi_store&reqSrc=1&vc=146&userId=unknown&geo_lt=4&s=android&last_src=app_xiaomi_store&geo_lng=113.552414&geo_lat=23.112867&v=3.79.2&wifi_open=0&imei=unknown HTTP/1.1"
    html = requests.get(url, headers=headers)
    rc = re.compile(br"YGKJ({.*})YGKJ")
    js = rc.search(  html.content).groups()
    dct = json.loads(*js)
    return dct

def hero_imgs_download():
    headers = {'Accept-Charset': 'UTF-8',
            'Accept-Encoding': 'gzip,deflate',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Host': 'gamehelper.gm825.com'}
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    req = requests.get(url = heros_url, headers = headers).json()
    lst = req['list']
    hero_images_path = 'images'
    return lst
def downloadsWzryCover(lst , hero_images_path):
    for each_hero in lst :
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'
        filename = hero_images_path + '/' + hero_name
        if hero_images_path not in os.listdir():
            os.makedirs(hero_images_path)
        urlretrieve(url = hero_photo_url, filename = filename)



def main(args):
    handle = {"chelaile":geChelaile, "weather":getWeather, "xiaomiweather":getMiWeather,
         "wzryHeroList":hero_imgs_download}
    dct = handle[args.url]()
    print( dct)
    if args.url == "wzryHeroList":
        downloadsWzryCover(dct , args.savepath)
    print("______________________finished____________________")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog='requests')
    parser.add_argument('url',choices=['chelaile','weather','xiaomiweather','wzryHeroList' ], help='argument setting ')
    parser.add_argument('--set','-s', default=[],action='append', help='setting')
    parser.add_argument('--output','-o', default="images",dest='savepath', action='append', help='output')
    parser.set_defaults(handle = main ) 
    args  = parser.parse_args()      
    if hasattr(args,'handle'):        
        args.handle( args)

