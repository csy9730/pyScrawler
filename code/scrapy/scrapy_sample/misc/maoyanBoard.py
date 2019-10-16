# coding = utf-8
__author__ = 'wardseptember'
__date__ = '18-10-26'
import json
import requests
from requests.exceptions import RequestException
from lxml import etree

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open('scr_maoyan.html','w',encoding='utf-8') as f1:
                f1.write(response.text)
                f1.close()
            print("写入成功")
        else:
            print("写入失败",response.status_code)
    except RequestException:
        print("写入失败")

def parse_one_page():
    result=etree.parse('scr_maoyan.html',etree.HTMLParser(encoding='utf-8'))
    result_id=result.xpath('//div[@class="main"]//dl//dd/i/text()')
    result_title=result.xpath('//div[@class="main"]//dl//dd/a/@title')
    result_img=result.xpath('//div[@class="main"]//dl//dd//a//img[2]/@data-src')
    result_star=result.xpath('//div[@class="main"]//dl//dd//p[@class="star"]/text()')
    result_time=result.xpath('//div[@class="main"]//dl//dd//p[@class="releasetime"]/text()')
    result_score1=result.xpath('//div[@class="main"]//dl//dd//i[@class="integer"]//text()')
    result_score2=result.xpath('//div[@class="main"]//dl//dd//i[@class="fraction"]//text()')
    '''
    print(result_id)
    print(result_title)
    print(result_img)
    print(result_star[0].strip()[3:])
    print(result_time)
    print(result_score1)
    print(result_score2)
    '''
    for i in range(10):
        yield {
            'index': result_id[i],
            'image': result_img[i],
            'title': result_title[i],
            'actor': result_star[i].strip()[3:],
            'time': result_time[i].strip()[5:],
            'score': result_score1[i]+result_score2[i]
        }


def write_to_file(content):
    with open('scr_result_xpath.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    get_one_page(url)

    for item in parse_one_page():
        #print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)