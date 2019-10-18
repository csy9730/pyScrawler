# baidumusic

歌曲列表: http://music.taihe.com/artist
歌手首页：http://music.taihe.com/artist/1098
歌手歌曲翻页，： ajax="http://music.taihe.com/data/user/getsongs?start=75&size=15&ting_uid=1098&.r=0.422275327513574441571378745809"
单曲页： ajax= "https://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172004889092848486731_1571381005554&songid=595643&from=web&_=1571381008551"
mp3资源url： ajax：

```
//span[@class="songname"]/a/text()

//div[@id="songList"]//li//div[@class="songlist-inline songlist-title"]//span[@class="songname"]/a/@title

//span[@class="songname"]/a/@href

//div[@class="songlist-inline songlist-album overdd"]//a/text()

//div[@class="songlist-inline songlist-time"]//text()
```

