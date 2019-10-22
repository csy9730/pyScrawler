import time
import requests
import json
import re

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
    headers = {
        "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 8 Lite MIUI/V10.0.8.0.ODTCNFH)",
        "Host":"weatherapi.market.xiaomi.com",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip"
    }
    url =  "https://weatherapi.market.xiaomi.com/wtr-v3/weather/all?latitude=23.112111&longitude=113.553917&isLocated=true&locationKey=weathercn%3A101280111&days=15&appKey=weather20151024&sign=zUFJoAR2ZVrDy1vF3D07&romVersion=V10.0.8.0.ODTCNFH&appVersion=10000500&alpha=false&isGlobal=false&device=platina&modDevice=&locale=zh_cn HTTP/1.1"
    html = requests.get(url, headers=headers)
    dct = html.json()
    return dct


def geChelaile():
    headers = {
        "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 8 Lite MIUI/V10.0.8.0.ODTCNFH)",
        "Host":"api.chelaile.net.cn",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip"
    }
    url =  "https://api.chelaile.net.cn/bus/line!tsfRealInfos.action?sign=AgZKshID7EG9ApVQPI%2Bszw%3D%3D&nw=MOBILE_LTE&language=1&cityId=040&AndroidID=045d9a9cee2c99ea&mac=C2%3A00%3AF3%3A99%3A6B%3A1D&lineStn=020-03220-1%2C020-1416%3B020-02140-1%2C020-1416%3B020-05713-0%2C020-1416%3B020-05710-0%2C020-1416%3B020-04390-1%2C020-16690%3B020-03300-0%2C020-13424%3B020-04370-1%2C020-9260%3B020-05730-1%2C020-9260%3B020-03220-1%2C020-1416%3B020-05713-0%2C020-1416%3B020-02140-1%2C020-1416%3B020-05710-0%2C020-1416%3B020-04360-0%2C020-9814%3B&phoneBrand=Xiaomi&lchsrc=icon&udid=9fd7f400-3b90-4516-9457-dc919f08248e&system_push_open=1&deviceType=MI+8+Lite&geo_type=gcj&push_open=1&sv=8.1.0&geo_lac=550.0&first_src=app_xiaomi_store&reqSrc=1&vc=146&userId=unknown&geo_lt=4&s=android&last_src=app_xiaomi_store&geo_lng=113.552414&geo_lat=23.112867&v=3.79.2&wifi_open=0&imei=unknown HTTP/1.1"
    html = requests.get(url, headers=headers)
    rc = re.compile(br"YGKJ({.*})YGKJ")
    js = rc.search(  html.content).groups()
    dct = json.loads(*js)
    return dct

def main():
    dct = geChelaile()
    print( dct)
if __name__ == "__main__":
    main()

