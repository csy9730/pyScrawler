

#导入框架(模块/库)

import requests
from lxml import etree

import json


#确定URL地址
url = 'http://music.taihe.com/top/dayhot'
base_url ='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='

#请求
reuslt = requests.get(url).text

#删除数据（xpath）
dom = etree.HTML(reuslt)
song_ids = dom.xpath('//a[contains(@href,"/song/")]/@href')[1:]
print( song_ids )
for index,song_id in enumerate(song_ids):
    song_id_string = song_id.split('/')[2]
    song_url = requests.get(base_url + song_id_string).text

    dict_url = json.loads(song_url)
    mp3_url=dict_url['bitrate']['show_link']
    print(mp3_url)
    mp3 = requests.get(mp3_url).content

#保存
    with open(f'{index}.mp3','wb') as file:
        file.write(mp3)